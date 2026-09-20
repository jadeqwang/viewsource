# View Source

An escape-room-like reading experience, a spin-off from the *Spaces Left Blank*
trilogy by Jade Q Wang. Deployed to **viewsource.cc**; the main collection lives
at [spacesleftblank.com](https://spacesleftblank.com).

Static pages, no build step. Served as Cloudflare Workers assets.

    npx wrangler deploy

For a local preview with the same extensionless HTML routes as Cloudflare:

    python3 scripts/serve.py

Then open `http://localhost:8777/`. For example, `/safe-harbor` resolves to
`public/safe-harbor.html`.

`viewsource.cc/` is the front door: the poem *bios*, and a console riddle that
gates the rest of the sequence (`answer("banach tarski banach tarski")`). That
riddle used to live on spacesleftblank.com; repoint or retire that redirect when
convenient. `preview-convergence.html` is the previous entry point and still
works.

See `docs/NOTES.md` for the page order, the forks, and how the terminal page is
put together.

© 2026 Jade Q Wang. Licensed under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
