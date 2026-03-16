# Shraman Chaudhuri Portfolio

Personal portfolio site built with Astro and Tailwind CSS v4, with configuration-first content management and several custom pages beyond the main portfolio view.

## Tech Stack

- Astro 5
- Tailwind CSS v4 (via Vite plugin)
- TypeScript
- React (used for the glowing effect UI component)
- Astro integrations: sitemap

## Current Site Features

- Single-page portfolio home with these sections:
  - Hero (with typewriter phrases)
  - About + Skills
  - Projects
  - Achievements
  - Certifications
  - Education
  - Experience (optional)
  - Classroom Notes
- Theme toggle (light and dark) persisted in local storage
- Accent color system driven from config
- Dedicated standalone routes for:
  - Connect links page
  - Caesar cipher tool page
  - Catalyst product page
  - Watcher product page
  - Bharat Scouts and Guides notes page
  - Generic coming soon page

## Routes

- / -> Main portfolio page
- /connect -> Link hub page
- /caesar-cipher -> Caesar cipher utility
- /catalyst -> Catalyst project showcase
- /watcher -> Watcher project showcase
- /bsg_notes -> Bharat Scouts and Guides notes
- /coming-soon -> Placeholder page

## Configuration

All portfolio content is managed from src/config.ts.

The current config shape includes:

- name, title, description, accentColor
- typewriterPhrases
- social
- aboutMe
- skills
- projects
- achievements
- certifications
- experience
- education
- classroomNotes

Conditional rendering rules:

- Projects, Experience, Education, Achievements, Certifications, and Classroom Notes sections render only when corresponding arrays contain data.

## Local Development

1. Install dependencies:

```bash
npm install
```

2. Start dev server:

```bash
npm run dev
```

3. Build production output:

```bash
npm run build
```

4. Preview production build locally:

```bash
npm run preview
```

## Project Structure (Current)

```text
.
|- src/
|  |- config.ts
|  |- components/
|  |  |- Hero.astro
|  |  |- About.astro
|  |  |- Projects.astro
|  |  |- Achievements.astro
|  |  |- Certifications.astro
|  |  |- Education.astro
|  |  |- Experience.astro
|  |  |- ClassroomNotes.astro
|  |  |- ThemeToggle.astro
|  |  |- Header.astro
|  |  |- Footer.astro
|  |  |- ui/
|  |     |- glowing-effect.tsx
|  |- pages/
|  |  |- index.astro
|  |  |- connect.astro
|  |  |- caesar-cipher.astro
|  |  |- catalyst.astro
|  |  |- watcher.astro
|  |  |- bsg_notes.astro
|  |  |- coming-soon.astro
|  |  |- rss.xml.ts
|  |- styles/
|     |- global.css
|     |- links.css
|- public/
|  |- images/
|- astro.config.mjs
|- package.json
|- tailwind.config.js
```

## Deployment Notes

- Astro site URL is currently set in astro.config.mjs as https://shramanc.pages.dev.
- Static output can be deployed to Netlify, Cloudflare Pages, Vercel, GitHub Pages, or any other static host.

## License

MIT. See LICENSE.md.
