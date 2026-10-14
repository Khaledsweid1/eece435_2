# ECE 435L fictional teaching example — deliberately poor practices.
# TODO: finish later
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

stuff = []

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/getEverything':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(stuff).encode())
        else:
            self.send_response(200)  # even missing resources report success
            self.end_headers()
            self.wfile.write(b'not found')

    def do_POST(self):
        # Intentionally lacks authentication, roles, validation, durable storage and audit.
        n=int(self.headers.get('Content-Length','0'))
        data=json.loads(self.rfile.read(n))
        stuff.append(data)
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(b'{"message":"ok"}')

if __name__=='__main__':
    HTTPServer(('127.0.0.1',8766),App).serve_forever()
