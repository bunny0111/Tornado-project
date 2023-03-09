import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado!")

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Helo, This is PostHandler in Tornado!</h1>")

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = "Hot!" if degree > 20 else "cold!"
        drink = "Have some Cold Drink" if degree > 20 else "You need Coffee"
        self.render("weather.html", output = output, drink = drink)

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler),
        (r"/weather", WeatherHandler)
    ],
    debug=True,
    autoreload=True)

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is listening on localhost on port {8888}")
    tornado.ioloop.IOLoop.current().start()