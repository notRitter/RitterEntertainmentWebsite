import { sitePath } from '../lib/site';
import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
  const sitemap = new URL(sitePath('sitemap-index.xml'), site);
  const content = site?.hostname.endsWith('.github.io')
    ? 'User-agent: *\nAllow: /\n'
    : `User-agent: *\nAllow: /\nSitemap: ${sitemap}\n`;
  return new Response(content, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
