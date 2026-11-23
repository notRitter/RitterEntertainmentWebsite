# Ritter Entertainment LLC website

Static Astro website for the studio’s games and RPG Maker tools. GitHub Pages serves the generated files, and the official itch.io listings handle play, downloads, and purchases.

- [GitHub Pages review site](https://notritter.github.io/RitterEntertainmentWebsite/)
- [Domain migration and rollback](docs/domain-migration.md)
- [Verification report](docs/verification.md)
- [Media sources and third-party notices](docs/media-sources.md)

## Run locally

Install Node.js 24 LTS and npm. If you use nvm, run `nvm use` in the repository.

```sh
npm ci
npm run dev
```

Open the local address printed by Astro. Use `npm run check` for type and content validation. `npm run build` produces the production site in `dist/`. Run `npm run preview` to serve the build. The optional `npm run check:output` command uses Python 3.9 or later to validate the generated links, assets, metadata, and sitemap.

To reproduce the project-subpath build without replacing the production output:

```sh
export PAGES_ORIGIN=https://notritter.github.io
export PAGES_BASE=/RitterEntertainmentWebsite
npm run build -- --outDir dist-preview
npm run check:output -- --dir dist-preview
unset PAGES_ORIGIN PAGES_BASE
```

## Edit the catalog

| What to edit | Where |
| --- | --- |
| Games | `src/content/games/` |
| Plugins and utilities | `src/content/tools/` |
| Endless Math Challenge rewards | `src/content/guides/endless-math-unlocks.md` |
| Images | `public/media/` |
| Studio contact and shared links | `src/lib/site.ts` |

Each Markdown file is one page. The filename is its URL slug. For example, `src/content/games/jumpy-cat.md` generates `/games/jumpy-cat/`. The section between the `---` lines holds page settings, and the Markdown below it is the page body. Keep existing filenames stable to preserve links.

To add a project, copy a similar entry, give it a new lowercase, hyphenated filename, then edit its fields and replace the body. The catalog and route will build automatically. A new in-development game can start with:

```yaml
---
title: Your game name
summary: One sentence describing what the player does.
category: Strategy
status: In development
order: 50
featured: false
accent: blue
---

## Overview

Describe the game here.
```

- Required fields are `title`, `summary`, `category`, `status`, and an integer `order`. Tool entries also need `engines`, for example `[MV, MZ]`. Catalogs sort by ascending `order`.
- `status` is `In development` or `Released`. For a release, update the status and add a `releaseNote` and verified storefront link. Versions are optional and should be quoted, such as `version: "2.1"`.
- Set `featured: true` to promote a project. The first featured game by order leads the home page. The next three game cards prioritize featured entries, then catalog order. The first three tools by order among featured entries appear on the home page.
- `accent` accepts `blue`, `violet`, `gold`, `mint`, or `rose`. With no `cover`, the template renders a typographic title treatment.
- Put approved, optimized images in `public/media/`, then add `cover` or `gallery` entries with `file` and descriptive `alt`. Gallery entries can have a `caption`. WebP is a good default for screenshots. Aim for roughly 1,000–1,600 pixels across and under 250 KB per image where practical.
- Each `storefronts`, `documentation`, or `demos` entry takes a `label` and HTTPS `url`. For a trailer, use a `demos` entry. For a development update, add a dated heading and copy in the project body.
- `related` links to projects by their Markdown filenames without `.md`. Keep these names unique across the game and tool directories.
- Use `##` for body headings because the template already supplies the page title.

You can upload an approved image and edit the Markdown through GitHub’s **Add file** and pencil controls. Commit to a branch, open a pull request, and merge after the build passes. The [Actions tab](https://github.com/notRitter/RitterEntertainmentWebsite/actions) shows the deployment.

## Deployment

In repository **Settings → Pages**, use **GitHub Actions** as the source. The workflow builds pull requests and publishes from `main` after verification. It reads the registered Pages origin and base path for deployments, so the same templates work under the temporary repository subpath and the eventual canonical domain. A manual rerun from `main` is available through **Actions → Build and deploy website → Run workflow**.

Copyright © 2026 Ritter Entertainment LLC. All rights reserved.
