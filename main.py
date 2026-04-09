import os
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

        if self.path.startswith('/data/'):
            local_path = os.path.join(os.getcwd(), self.path[1:])
            
            if os.path.exists(local_path) and os.path.isfile(local_path):
                self.send_response(200)
                if self.path.lower().endswith(('.jpg', '.jpeg')):
                    self.send_header('Content-Type', 'image/jpeg')
                elif self.path.lower().endswith('.png'):
                    self.send_header('Content-Type', 'image/png')
                
                self.end_headers()
                with open(local_path, 'rb') as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, "File Not Found")
                return

        super().do_GET()

if __name__ == '__main__':
    handler = BlogHandler
    port = 5556
    with socketserver.TCPServer(('', port), handler) as httpd:
        print(f'http://localhost:{port}')
        httpd.serve_forever()
