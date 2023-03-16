from pyuvm import *
import pyuvm
from cocotb.clock import Clock

from env import *
from sequence import *

@pyuvm.test()
class Test(uvm_test):
    def build_phase(self):
        self.env = Env("env", self)

    def end_of_elaboration_phase(self):
        self.sequence = Sequence.create("sequence")

    async def run_phase(self):
        self.raise_objection()
        # Start 1ns clock concurrently
        cocotb.start_soon(Clock(cocotb.top.clk, 2, units='us').start())
        # Start the sequence
        await self.sequence.start(self.env.agent.sequencer)
        self.drop_objection()
