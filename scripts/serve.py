#!/usr/bin/env python3
"""Serve public/ locally with Cloudflare-style extensionless HTML routes."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PUBLIC_DIR = Path(__file__).resolve().parent.parent / "public"


class ExtensionlessHTMLHandler(SimpleHTTPRequestHandler):
    """Resolve /page to /page.html when the HTML file exists."""

    def translate_path(self, path: str) -> str:
        translated = Path(super().translate_path(path))
        if not translated.exists() and translated.suffix == "":
            html_path = translated.with_name(f"{translated.name}.html")
            if html_path.is_file():
                return str(html_path)
        return str(translated)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8777)
    args = parser.parse_args()

    handler = partial(ExtensionlessHTMLHandler, directory=PUBLIC_DIR)
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {PUBLIC_DIR} at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
