import time
import BaseHTTPServer
import get_data

HOST_NAME = '127.0.0.1'  # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9090  # Maybe set this to 9000.


# noinspection PyArgumentList
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        username, password = get_data.get_username_and_password()
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Vecino Project</title></head>")
        self.wfile.write(""
                      "<body bgcolor=LemonChiffon>"
                      "<head>"
                      "<style>header, footer "
                      "{padding: 1em;"
                      "color: LemonChiffon;"
                      "background-color: black"
                      ";clear: left"
                      ";text-align: center;}"
                      "article "
                      "{margin-left: 170px"
                      ";border-left: 1px solid gray;"
                      "padding: 1em;overflow: hidden;}"
                      "</style>"
                      "</head>"
                      "<body>"
                    "<header>"
                      "<h2>Output from Vecino </h2>"
                        "</header>"
                        "<article>"
        "<h3>"
        "<font color=black>Username: %s</font>"
        "</h3>"
        "<h3>"
        "<font color=black>Password: %s</font>"
        "<h3>"
        "</article>"
        "<footer></footer>" 
                      "" % (username, password))
        self.wfile.write("</body></html>")



if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
