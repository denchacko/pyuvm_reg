from pyuvm import *
import cocotb

from bfm import *

class Monitor(uvm_component):
    def __init__(self, name, parent, method_name = "monitor"):
        super().__init__(name, parent)
        self.method_name = method_name

        self.intf = cocotb.top # TODO pass interface handle from env

        # Declaring instance variables initialised in other functions
        # Not required, just keeping all instance variables in __init__()
        self.ap = None
        self.bfm = None
        self.run_method = None

    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)
        self.bfm = Bfm(self.intf)
        self.run_method = getattr(self.bfm, self.method_name)

    async def run_phase(self):
        while True:
            datum = await self.run_method()
            self.logger.info(f"MONITORED {datum}")
            self.ap.write(datum)
