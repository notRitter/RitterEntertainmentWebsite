export const studio = {
  name: 'Ritter Entertainment LLC',
  title: 'Ritter Entertainment',
  description: 'Independent game studio creating original games and development tools for RPG Maker MV and MZ.',
  email: 'Craig@RitterEntertainment.com',
  store: 'https://notritter.itch.io/',
  docs: 'https://notritter.github.io/SpawnerDocs/',
  copyright: 'Copyright © 2026 Ritter Entertainment LLC. All rights reserved.',
};

export function sitePath(path = '/') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\/+/, '')}`;
}

export function mediaPath(file: string) {
  return sitePath(`media/${file}`);
}
