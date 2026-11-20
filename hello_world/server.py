#!/usr/bin/env python3
"""Hello world page for the Home Assistant ingress proxy."""

import html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

INGRESS_PORT = 8099
SUPERVISOR_ADDRESS = "172.30.32.2"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.client_address[0] != SUPERVISOR_ADDRESS:
            self.send_error(403, "Forbidden")
            return

        name = (
            self.headers.get("X-Remote-User-Display-Name")
            or self.headers.get("X-Remote-User-Name")
            or "world"
        )
        body = page(name).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} - {fmt % args}", flush=True)


def page(name: str) -> str:
    safe_name = html.escape(name, quote=True)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello world</title>
  <style>
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      font-family: system-ui, sans-serif;
      background: #111;
      color: #f5f5f5;
    }}
    main {{ text-align: center; }}
    p {{ color: #bdbdbd; }}
  </style>
</head>
<body>
  <main>
    <h1>Hello {safe_name}!</h1>
    <p>This page is served by the Hello world Home Assistant app.</p>
  </main>
</body>
</html>
"""


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", INGRESS_PORT), Handler)
    print(f"Listening on {INGRESS_PORT}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
