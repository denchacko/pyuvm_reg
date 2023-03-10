from pyuvm import *

class Sequence(uvm_sequence):
    num_trans = 1

    async def body(self):
        for i in range(self.num_trans):
            req = SeqItem("req")
            await self.start_item(req)
            req.randomize()
            await self.finish_item(req)
