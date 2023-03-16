from driver import *
from monitor import *

class Agent(uvm_component):
    def __init__(self, name, parent):
        super().__init__(name, parent)

    def build_phase(self):
        self.sequencer = uvm_sequencer("sequencer", self)
        self.driver = Driver("driver", self)
        self.monitor = Monitor("monitor", self)

    def connect_phase(self):
        self.driver.seq_item_port.connect(self.sequencer.seq_item_export)
