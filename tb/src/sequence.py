from pyuvm import *

from seq_item import *

class Sequence(uvm_sequence):

    async def body(self):
        num_trans = 50

        for i in range(num_trans):
            req = SeqItem("req")
            await self.start_item(req)
            req.randomize()
            await self.finish_item(req)
