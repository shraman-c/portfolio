import os
import re
import glob

pages_dir = r"d:\Documents\GitHub\portfolio\src\pages"
astro_files = glob.glob(os.path.join(pages_dir, "*.astro"))

watcher_og_snippet = """    <!-- Open Graph Tags for LinkedIn/Social Previews -->
    <meta property="og:title" content="Watcher | Python Desktop File-Watcher" />
    <meta property="og:description" content="An open-source, CPU-efficient file-watching desktop application built with Python and Tkinter." />
    <meta property="og:url" content="https://shramanc.pages.dev/watcher/" />
    <!-- Optional: Add a screenshot link if you have one -->
    <!-- <meta property="og:image" content="https://shramanc.pages.dev/watcher/preview.png" /> -->"""

watcher_title = '<title>Watcher - File-Watching Desktop App</title>'

def get_tag_content(html, tag_name):
    # e.g., <title>...</title>
    match = re.search(f'<{tag_name}[^>]*>(.*?)</{tag_name}>', html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_meta_content(html, name_attr):
    match = re.search(f'<meta\\s+name=[\'"]{name_attr}[\'"]\\s+content=[\'"]([^\'"]+)[\'"]', html, re.IGNORECASE)
    if match:
        return match.group(1)
    
    # Try with single quotes or no quotes for content? 
    # Or maybe it has dynamic content like content={siteConfig.description}
    match = re.search(f'<meta\\s+name=[\'"]{name_attr}[\'"]\\s+content={{([^}}]+)}}', html, re.IGNORECASE)
    if match:
        return f"{{{match.group(1)}}}"
        
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    slug = filename.replace('.astro', '')
    if slug == 'index':
        url = "https://shramanc.pages.dev/"
    else:
        url = f"https://shramanc.pages.dev/{slug}/"

    # Remove existing OG and Twitter blocks, including the optional commented image tag
    content = re.sub(r'<!-- Open Graph.*?-->\s*(<meta property="og:.*?>\s*)*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!-- Twitter.*?-->\s*(<meta property="twitter:.*?>\s*)*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!-- Optional: Add a screenshot link if you have one -->\s*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!-- <meta property="og:image".*?-->\s*', '', content, flags=re.IGNORECASE)

    # For watcher.astro, use exactly what user requested
    if filename == 'watcher.astro':
        # Replace title
        content = re.sub(r'<title>.*?</title>', watcher_title, content, flags=re.IGNORECASE | re.DOTALL)
        
        # Add the snippet before </head>
        content = re.sub(r'(\s*)</head>', f'\n{watcher_og_snippet}\\1</head>', content, flags=re.IGNORECASE)

    else:
        # Get title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else f"{slug.title()} - {{siteConfig.name}}"
        
        # Determine title string for OG (handle JS expressions if needed)
        # Convert simple interpolation {var} into proper Astro expressions `{...}`
        if '{' in title and '}' in title:
            # Reconstruct as JS template string inside JSX curlies
            # e.g., "BSG Notes - {siteConfig.name}" -> "{`BSG Notes - ${siteConfig.name}`}"
            js_expr = re.sub(r'\{(.*?)\}', r'${\1}', title)
            og_title_content = f'{{`{js_expr}`}}'
        else:
            og_title_content = f'"{title}"'

        # Get description
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=(["\']?.*?["\']?|{.*?})\s*/?>', content, re.IGNORECASE | re.DOTALL)
        desc_raw = desc_match.group(1) if desc_match else '""'

        og_snippet = f"""    <!-- Open Graph Tags for LinkedIn/Social Previews -->
    <meta property="og:title" content={og_title_content} />
    <meta property="og:description" content={desc_raw} />
    <meta property="og:url" content="{url}" />
    <!-- Optional: Add a screenshot link if you have one -->
    <!-- <meta property="og:image" content="https://shramanc.pages.dev/{slug}/preview.png" /> -->"""
        
        content = re.sub(r'(\s*)</head>', f'\n{og_snippet}\\1</head>', content, flags=re.IGNORECASE)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in astro_files:
    process_file(filepath)
    print(f"Processed {os.path.basename(filepath)}")
