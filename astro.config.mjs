import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const canonicalOrigin = 'https://www.ritterentertainment.com';
const site = process.env.PAGES_ORIGIN || canonicalOrigin;
const base = process.env.PAGES_BASE || '/';

export default defineConfig({
  site,
  base,
  output: 'static',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
  integrations: [
    sitemap({
      filter: (url) => !/\/(?:emc|404(?:\.html)?)\/?$/.test(new URL(url).pathname),
    }),
  ],
});
