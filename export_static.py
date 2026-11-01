"""Render the Flask portfolio into a portable static site for production."""
import argparse
from pathlib import Path
from shutil import copytree

from app import app


def export(directory="dist"):
    root = Path(__file__).resolve().parent
    output = root / directory
    output.mkdir(exist_ok=True)
    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise RuntimeError(f"Portfolio rendering failed: {response.status_code}")
        # Relative asset links work both at a domain root and a Pages project path.
        html = response.get_data(as_text=True).replace('="/static/', '="static/')
        (output / "index.html").write_text(html, encoding="utf-8")
    copytree(root / "static", output / "static", dirs_exist_ok=True)
    (output / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    (output / ".nojekyll").touch()
    print(f"Exported production portfolio to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", choices=("dist", "docs"), default="dist")
    export(parser.parse_args().output)
