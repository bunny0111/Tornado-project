import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado!")

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, This is PostHandler in Tornado!</h1>")

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler)
    ],
    debug = True,
    autoreload = True)

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is listening on localhost on port {8888}")
    # to start the server on current thread
    tornado.ioloop.IOLoop.current().start()