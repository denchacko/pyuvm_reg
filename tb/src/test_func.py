from seq_item import *
from commons import *

def test_op_enum():
    '''
    To test enum class opcode
    '''
    print(f"list(Opcode): {list(Opcode)}")
    print(f"Opcode(1): {Opcode(1).name} ({Opcode(1).value})")

def test_seq_item():
    '''
    To test SeqItem instance creation, randomization & printing
    '''
    seq_item = SeqItem(name = "seq_item")
    seq_item.randomize()
    print(f'SeqItem(name = "seq_item") : {seq_item.convert2string()}')

    seq_item.make_none()
    seq_item.addr = 0xa
    seq_item.randomize()
    print(f'SeqItem addr fixed: {seq_item.convert2string()}')

    seq_item = SeqItem(name = "seq_item", opcode = Opcode.READ)
    seq_item.randomize()
    print(f'SeqItem opcode fixed: {seq_item.convert2string()}')

    seq_item.make_none()
    seq_item.addr = 0xa
    seq_item.opcode = Opcode.WRITE
    seq_item.data = 0xcc
    seq_item.randomize()
    print(f'SeqItem all fixed: {seq_item.convert2string()}')

def test_inst_var():
    '''
    To test instance variable scope
    '''
    class Class:
        def __init__(self):
            self.A = 10

        def initialise(self, val = 20):
            self.B = val

        def print_var(self):
            print(f"A: {self.A} B: {self.B}")

    inst = Class()
    inst.initialise()

    inst_2 = Class()
    inst_2.initialise(30)
    inst_2.print_var()
    inst.print_var()
