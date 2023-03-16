from pyuvm import *

from agent import *

class Env(uvm_env):

    def build_phase(self):
        self.agent = Agent("agent", self)
