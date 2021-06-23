"""
run test server

http://localhost:8000/
"""

import http.server

print("run server")
server_address = ("", 8000)
handler_class = http.server.CGIHTTPRequestHandler
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()
