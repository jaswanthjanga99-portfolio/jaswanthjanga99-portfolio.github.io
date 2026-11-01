"""Render the Flask portfolio into a portable static site for production."""
from pathlib import Path
from shutil import copytree

from app import app


def export():
    root = Path(__file__).resolve().parent
    output = root / "dist"
    output.mkdir(exist_ok=True)
    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise RuntimeError(f"Portfolio rendering failed: {response.status_code}")
        (output / "index.html").write_bytes(response.data)
    copytree(root / "static", output / "static", dirs_exist_ok=True)
    (output / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print(f"Exported production portfolio to {output}")


if __name__ == "__main__":
    export()
