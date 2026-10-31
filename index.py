"""Vercel entrypoint: the API (blend/server.py) and the built dashboard (web/dist) as one FastAPI app."""

from pathlib import Path

from blend.server import create_app

ROOT = Path(__file__).resolve().parent
app = create_app(ROOT / "bundles", ROOT / "web" / "dist")
