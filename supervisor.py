import otp
from utils import log, plog
from example import Config


def start_supervisor():
    supervisor = otp.Supervisor()
    supervisor.start([
        Config
    ])


if __name__ == '__main__':
    start_supervisor()
    Config.emit('hello')
