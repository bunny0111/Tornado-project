# importing the main event loop
import tornado.ioloop
# for HTTP requesthandlers(to map the requests to request handlers)
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, Tornado!')

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler)
    ],
    debug=True,
    autoreload=True)

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is listening on localhost on port {8888}")
    # to start the server on current thread
    tornado.ioloop.IOLoop.current().start()