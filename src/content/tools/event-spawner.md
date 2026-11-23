---
title: Ritter Ultimate Event Spawner
summary: Spawn, recycle, transform, and persist events at runtime in RPG Maker MV and MZ.
category: Event management
status: Released
order: 10
featured: true
accent: blue
engines: [MV, MZ]
version: "2.1"
cover:
  file: event-spawner.webp
  alt: Ritter Ultimate Event Spawner official banner
gallery:
  - file: event-spawner-demo.webp
    alt: RPG Maker map displaying the event spawner’s test counter
    caption: Still from the event recycling demonstration.
storefronts:
  - label: View Event Spawner on itch.io
    url: https://notritter.itch.io/ritter-ultimate-event-spawner-rpg-maker-mv
documentation:
  - label: Event Spawner documentation
    url: https://notritter.github.io/SpawnerDocs/
demos:
  - label: Play the Jumpy Cat demo on itch.io
    url: https://notritter.itch.io/jumpy-cat
related: [boundary-system, spawn-map-designer, jumpy-cat]
---

## Place events from templates

Keep reusable event templates on separate spawn maps and instantiate them at coordinates, by region ID, or by terrain tag. A live event can also be transformed using another template.

## Choose what gets recycled or saved

Recycle temporary event objects and sprites for repeated spawning. Saved events can retain their identity and state when the player returns to a map or loads a save. The documentation explains when to choose each lifecycle.

## Build a streaming system

Pair the spawner with the Boundary System to activate nearby encounters, hazards, or NPCs as the player moves around a map. Use Spawn Map Designer to organize the templates behind those systems.

The same plugin works in MV and MZ. Script calls are available in both engines, and MZ has dedicated plugin commands.
