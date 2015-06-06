import web
import view
import socket
from view import render

urls = (
    '/', 'index'
)

namehost = socket.gethostname()
ip = socket.gethostbyname(namehost)

class index:
    def GET(self):
    	htmlContent = "hostname: " + namehost + " <br />"
    	htmlContent = htmlContent + "ip: " + ip + "<br />"
        return render.base(htmlContent, "Server details")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()