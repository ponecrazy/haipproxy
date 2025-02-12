"""
This module is used to provide web api for other languages
"""
import argparse

from haipproxy.api import app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()
    app.run(port=args.port, host=args.host)
