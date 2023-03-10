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
