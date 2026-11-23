import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const media = z.object({
  file: z.string().regex(/^[\w-]+\.(avif|webp|png|jpe?g)$/),
  alt: z.string().min(1),
  caption: z.string().optional(),
});

const link = z.object({
  label: z.string().min(1),
  url: z.url().refine((url) => url.startsWith('https://')),
});

const slug = z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/);
const project = z.object({
  title: z.string().min(1),
  summary: z.string().min(1),
  category: z.string().min(1),
  status: z.enum(['In development', 'Released']),
  order: z.number().int(),
  featured: z.boolean().default(false),
  accent: z.enum(['blue', 'violet', 'gold', 'mint', 'rose']).default('blue'),
  cover: media.optional(),
  gallery: z.array(media).default([]),
  storefronts: z.array(link).default([]),
  documentation: z.array(link).default([]),
  demos: z.array(link).default([]),
  related: z.array(slug).default([]),
  releaseNote: z.string().optional(),
});

export const collections = {
  games: defineCollection({
    loader: glob({ pattern: '*.md', base: './src/content/games' }),
    schema: project.extend({
      platform: z.string().optional(),
      unlockGuide: z.boolean().default(false),
    }),
  }),
  tools: defineCollection({
    loader: glob({ pattern: '*.md', base: './src/content/tools' }),
    schema: project.extend({
      engines: z.array(z.enum(['MV', 'MZ'])).min(1),
      platform: z.string().optional(),
      version: z.string().optional(),
    }),
  }),
  guides: defineCollection({
    loader: glob({ pattern: '*.md', base: './src/content/guides' }),
    schema: z.object({
      title: z.string().min(1),
      summary: z.string().min(1),
    }),
  }),
};
