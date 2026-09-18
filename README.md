# View Source

An escape-room-like reading experience, a spin-off from the *Spaces Left Blank*
trilogy by Jade Q Wang. Deployed to **viewsource.cc**; the main collection lives
at [spacesleftblank.com](https://spacesleftblank.com).

Static pages, no build step. Served as Cloudflare Workers assets.

    npx wrangler deploy

There is no index page by design — `viewsource.cc/` returns 404. Readers reach
the sequence from spacesleftblank.com.

© 2026 Jade Q Wang. Licensed under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
