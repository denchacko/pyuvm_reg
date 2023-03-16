from pyuvm import *
from cocotb.triggers import RisingEdge

from commons import *
from seq_item import *

class Bfm:
    def __init__(self, intf, wdata = 8, waddr = 4):
        self.intf = intf
        self.wdata = wdata
        self.waddr = waddr

    # Driver functions
    async def reset(self):
        await RisingEdge(self.intf.clk)
        self.intf.reset.value = 1
        self.intf.addr.value = 0
        self.intf.wr_en.value = 0
        self.intf.rd_en.value = 0
        self.intf.wdata.value = 0

        await RisingEdge(self.intf.clk)
        self.intf.reset.value = 0
        await RisingEdge(self.intf.clk)

    async def drive(self, req):
        self.intf.wr_en.value = 0
        self.intf.rd_en.value = 0

        await RisingEdge(self.intf.clk)
        self.intf.addr.value = req.addr

        if(req.opcode == Opcode.READ):
            self.intf.rd_en.value = 1
        elif(req.opcode == Opcode.WRITE):
            self.intf.wr_en.value = 1
            self.intf.wdata.value = req.data

        await RisingEdge(self.intf.clk)
        self.intf.wr_en.value = 0
        self.intf.rd_en.value = 0

    # Monitor functions
    async def monitor(self):
        mon_trans = SeqItem("mon_trans")

        while True:
            await RisingEdge(self.intf.clk)
            mon_trans.wr_en = get_int(self.intf.wr_en)
            mon_trans.rd_en = get_int(self.intf.rd_en)
            mon_trans.addr = get_int(self.intf.addr)

            if(mon_trans.wr_en == 1):
                mon_trans.opcode = Opcode.WRITE
                mon_trans.data = get_int(self.intf.wdata)
                return mon_trans
            elif(mon_trans.rd_en == 1):
                await RisingEdge(self.intf.clk)
                mon_trans.opcode = Opcode.READ
                mon_trans.data = get_int(self.intf.rdata)
                return mon_trans
