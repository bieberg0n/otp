import otp
from utils import log, plog
from example import Config
from example_app import WebServer


def start_supervisor():
    supervisor = otp.Supervisor()
    supervisor.start([
        Config,
        WebServer,
    ])


if __name__ == '__main__':
    start_supervisor()
    Config.emit('hello')
