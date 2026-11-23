# Website hosting migration

**Current review address:** [notritter.github.io/RitterEntertainmentWebsite](https://notritter.github.io/RitterEntertainmentWebsite/)

**Production canonical:** [www.ritterentertainment.com](https://www.ritterentertainment.com/). The apex `ritterentertainment.com` should redirect to `www`.

The owner performs cutover after accepting the review site. Schedule enough time before the December 6, 2026 Squarespace website renewal for DNS propagation and the Pages HTTPS certificate. GitHub says the HTTPS setting can take up to 24 hours to become available.

## Before cutover

1. Review the GitHub Pages site and confirm that the latest `main` deployment succeeded. Save its commit SHA and the last known-good deployment SHA in case a rollback is needed.
2. Export or securely record the current Squarespace DNS zone values and TTLs. Note which records serve the current website at `@` and `www`. Record the existing Google Workspace MX, SPF, DKIM, and DMARC records as a before/after reference. Keep this export outside the public repository.
3. Keep domain registration, nameservers, and the Google Workspace subscription active. Preserve all MX records plus existing SPF, DKIM, DMARC, other verification TXT records, and unrelated DNS records. If Squarespace groups the web records as one default set, confirm the group contains only web records before removing it.
4. In the GitHub account’s **Settings → Pages**, begin domain verification for `ritterentertainment.com`. Add the exact verification TXT name and value GitHub supplies to the Squarespace zone, complete verification in GitHub, and retain the TXT record. [GitHub domain verification guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)

## Cut over website records

1. In the **RitterEntertainmentWebsite** repository’s **Settings → Pages**, enter `www.ritterentertainment.com` as the custom domain. Keep **GitHub Actions** as the source. GitHub Actions reads the hosting target from Pages settings. [GitHub custom-domain procedure](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
2. In Squarespace DNS, replace the conflicting apex and `www` records that point to Squarespace hosting. Add the following values and compare them with GitHub’s current instructions at cutover.

   | Host | Type | Value |
   | --- | --- | --- |
   | `@` | A | `185.199.108.153` |
   | `@` | A | `185.199.109.153` |
   | `@` | A | `185.199.110.153` |
   | `@` | A | `185.199.111.153` |
   | `www` | CNAME | `notritter.github.io` |

   For IPv6 at the apex, add all four GitHub AAAA records alongside the A records. Use `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, and `2606:50c0:8003::153`. Remove any obsolete apex website AAAA records pointing at Squarespace. The `www` target is the GitHub account host with no repository path.

3. In **Actions → Build and deploy website**, run the workflow from `main` after the repository has the custom domain setting. This rebuilds links, asset URLs, social URLs, and the sitemap for the production root.
4. Wait for the Pages DNS check and certificate to succeed, then turn on **Enforce HTTPS**. Both domains should reach the same site with `www` as canonical. [GitHub HTTPS guide](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)

## Verify before changing the Squarespace hosting subscription

- Open both HTTPS hostnames. Confirm the apex redirects to the canonical `www` host and check a deep link.
- Open `/games/`, a tool page, `/emc`, `/emc-info`, `/robots.txt`, and `/sitemap-index.xml`. Check that assets load and a non-existent path renders the custom 404.
- Open the Spawner documentation at its existing address. Follow at least one game and tool link to itch.io.
- Compare the DNS zone with the snapshot. Verify MX, SPF, DKIM, and DMARC values. Send mail to and from `Craig@RitterEntertainment.com` using an external mailbox and confirm both messages arrive.
- When the website and mail checks pass, the owner can manage the **website hosting subscription** separately from the active domain registration and Workspace subscriptions.

## Roll back

- **Website code issue:** Revert the offending commit through a pull request, then verify that the new deployment from `main` succeeds. The current Pages URL configuration will be picked up automatically.
- **DNS cutover issue:** While the Squarespace site is active, restore the previous apex and `www` website records from the snapshot. Check that both hosts again reach Squarespace after propagation. Remove the custom domain in the GitHub repository Pages settings after the old web records are restored, and run the workflow from `main` to serve the repository-subpath build again.
- Keep the Google Workspace records and domain registration active throughout rollback. Preserve the GitHub domain-verification TXT record for a future retry.
