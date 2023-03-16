from pyuvm import *
import cocotb

from bfm import *

class Driver(uvm_driver):
    def __init__(self, name, parent, method_name = "drive"):
        super().__init__(name, parent)
        self.method_name = method_name

        self.intf = cocotb.top # TODO pass interface handle from env

        # Declaring instance variables initialised in other functions
        # Not required, just keeping all instance variables in __init__()
        self.bfm = None
        self.run_method = None

    def build_phase(self):
        self.bfm = Bfm(self.intf)
        self.run_method = getattr(self.bfm, self.method_name)

    async def run_phase(self):
        await self.bfm.reset()
        while True:
            req = await self.seq_item_port.get_next_item()
            await self.run_method(req) # Will default to drive(req)
            self.seq_item_port.item_done()
