import SimpleHTTPServer
import SocketServer
import sys
PORT = int(sys.argv[1]);
class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass
Handler.extensions_map['.wasm'] = 'application/wasm'
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
