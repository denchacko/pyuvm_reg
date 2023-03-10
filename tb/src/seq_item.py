from pyuvm import *
import random

from commons import *

class SeqItem(uvm_sequence_item):

    def __init__(self, name, addr = None, opcode = None, data = None, wdata = 8, waddr = 4):
        super().__init__(name)
        self.wdata = wdata
        self.waddr = waddr
        self.addr = addr
        self.opcode = Opcode(opcode) if opcode else None # Consider opcode only if its not "None"
        self.data = data

    def randomize(self):
        '''
        Only randomise variables that are "None".
        Before calling this function, set variables that are not intended to be randomised
        '''
        # Iterating over all class variables
        for var, value in self.__dict__.items():
            if(value is None):
                match var:
                    case "addr" : self.addr = random.randint(0, pow(2, self.waddr)-1)
                    case "opcode" : self.opcode = random.choice(list(Opcode))
                    case "data" : self.data = random.randint(0, pow(2, self.wdata)-1)

    def make_none(self):
        '''
        To make all the randomisable fields their default value of "None"
        '''
        self.addr = None
        self.opcode = None
        self.data = None

    # This does the same thing as do_compare()
    # It returns True if the items are equal.
    # This method works with the == operator.
    def __eq__(self, other):
        pass

    # This does the same thing as convert2string().
    # It returns a string version of the item.
    # The print function calls this method automatically
    def __str__(self):
        return (f"{self.get_name()} : wdata: {self.wdata} waddr: {self.waddr} addr: "
                f"0x{self.addr:x} opcode: {self.opcode.name} ({self.opcode.value}) data: 0x{self.data:x}")
