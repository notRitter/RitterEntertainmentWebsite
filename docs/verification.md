# Website verification

## Content and assets

- Four game pages and eight development-tool pages. Map Transform and Active Item System each link to their separate MV and MZ editions.
- Deathwake and Hand of God are labeled in development. Their title treatments use typography and decorative geometry. Approved cover art, gameplay captures, and trailers can be added later.
- The Endless Math Challenge guide preserves all 24 subject/difficulty rewards and the completion-bonus hint in text. The legacy URLs are backed by a static forwarding page at `/emc` and the guide at `/emc-info`.
- The site uses `Craig@RitterEntertainment.com` as its studio contact. Link verification checks the mailto address, while live delivery belongs to the owner’s cutover check.
- Media source pages, image credits, and font notices are in [Media sources](media-sources.md). The optimized media is served locally with the site.

## Build and browser checks

| Check | Result |
| --- | --- |
| Static builds | Production root and temporary GitHub Pages subpath builds generated 19 HTML pages each. |
| Type and content checks | Astro reported zero errors, warnings, and hints. |
| Paths and SEO | The static output checker passed for both builds. It checks local routes, anchors, asset files, image alt attributes, titles, descriptions, canonical and Open Graph URLs, sitemap entries, and deployment-specific robots metadata. |
| External links | All 17 unique published HTTPS links returned HTTP 200 on November 23, 2026. This checks reachability of the listing, documentation, credit, and demo pages. |
| Responsive layout | Chrome desktop presentation was visually reviewed. The homepage, Event Spawner page, unlock guide, and contact page were checked at 320, 390, and 768 CSS pixels with no horizontal overflow. |
| Keyboard and accessibility | Keyboard focus reached the skip link and Enter moved focus to the page’s main region. Navigation labels, headings, representative text contrast, visible focus styling, image descriptions, and reduced-motion styles were reviewed. |
| Dependencies | npm audit reported zero known advisories on November 23, 2026, after updating Astro. |
| Hosting and data | Static output, no required server-side or paid services, no on-site checkout, and no private game source or credentials in the staged site. |

## Production cutover

The [migration guide](domain-migration.md) covers the owner’s DNS, HTTPS, canonical redirect, and Google Workspace checks. Those checks require the production cutover. The Squarespace and live domain settings are unchanged.
