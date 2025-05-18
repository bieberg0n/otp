import otp
from utils import log


class Methods:
    test = 'test'
    set_test = 'set_test'
    hello = 'hello'


class Config(otp.Service):
    name: str = 'test'
    m = Methods

    def __init__(self):
        super(Config, self).__init__()

        self.bind(Methods.test)

        self.handle_map = {
            **self.handle_map,
            Config.m.hello: self.hello,
        }
        self.states[Methods.test] = 'hello world'


    def hello(self):
        log('test hello world')
