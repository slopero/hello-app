from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 32777


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = "Hello, World!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    print(f"Server started on port {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
