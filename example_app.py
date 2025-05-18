from flask import Flask
# from flask_cors import CORS
import otp
from otp import log


class WebServer(otp.Service):
    name = 'webserver'

    def __init__(self):
        super(WebServer, self).__init__()
        self.app = Flask(__name__)
        # CORS(self.app)
        self.route()

    def get_app(self):
        return self.app

    def index(self):
        return 'HELLO WORLD', 200

    def route(self):
        self.app.add_url_rule('/', methods=['GET'], view_func=self.index)

    def run_app(self):
        self.app.run(host='0.0.0.0')

    def run(self):
        otp.spawn(target=self.run_app)
        super(WebServer, self).run()
