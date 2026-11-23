---
title: Ritter Boundary System
summary: Define fixed or moving map zones and stream events around the player when paired with Ultimate Event Spawner.
category: Event streaming
status: Released
order: 20
featured: true
accent: mint
engines: [MV, MZ]
version: "1.6"
cover:
  file: boundary-system.webp
  alt: Ritter Boundary System official banner
gallery:
  - file: boundary-visualizer.webp
    alt: RPG Maker map with colored overlays showing two spatial boundaries
    caption: Boundaries displayed with the developer visualizer.
storefronts:
  - label: View Boundary System on itch.io
    url: https://notritter.itch.io/ritter-boundary-system-rpg-maker-mz
documentation:
  - label: Read the Boundary System guide
    url: https://notritter.github.io/SpawnerDocs/Guides/Boundary/introduction.html
related: [event-spawner, spawn-map-designer, jumpy-cat]
---

## Work inside a defined area

Create zones at a fixed point or let them follow the player or another event. Query the tiles inside or along the edge of a boundary and select eligible tiles by region ID. Zones can drive mechanics such as hazards, encounter placement, or proximity checks.

## Stream nearby events

Combine it with a compatible Ultimate Event Spawner to spawn or remove events based on their position, preload event populations, and restore saved events when the player comes back. The documented saved-event system provides persistent Boundary Event IDs and per-event variables.
