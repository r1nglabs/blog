import http.server
import socketserver

class BlogHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='./www', **kwargs)

    def do_GET(self):
        if self.path == '/api':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(b'api is good.\n')
            self.wfile.flush()
            return

        super().do_GET()

if __name__ == '__main__':
    handler = BlogHandler
    with socketserver.TCPServer(('', 5555), handler) as httpd:
        print('http://localhost:5555')
        httpd.serve_forever()
