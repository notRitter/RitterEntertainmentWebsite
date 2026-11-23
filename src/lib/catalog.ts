import { getCollection, type CollectionEntry } from 'astro:content';
import { sitePath } from './site';

export type Project = CollectionEntry<'games'> | CollectionEntry<'tools'>;

const sortProjects = (a: Project, b: Project) =>
  a.data.order - b.data.order || a.data.title.localeCompare(b.data.title);

export async function getCatalog() {
  const [games, tools] = await Promise.all([getCollection('games'), getCollection('tools')]);
  return { games: games.sort(sortProjects), tools: tools.sort(sortProjects) };
}

export function projectUrl(project: Project) {
  return sitePath(`${project.collection}/${project.id}/`);
}
