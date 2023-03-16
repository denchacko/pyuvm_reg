#!/usr/bin/python3

import argparse

from test_func import *
from commons import *

parser = argparse.ArgumentParser()

mandatory = parser.add_argument_group("Mandatory Arguments")
mandatory.add_argument("-o", "--op", type = int, required = True, help = "Specify one of the following options: \
                                                                            op 0 : test_seq_item(), \
                                                                            op 1 : test_op_enum(), \
                                                                            op 2 : test_inst_var()")

args = parser.parse_args()

match args.op:
    case 0 : test_seq_item()
    case 1 : test_op_enum()
    case 2 : test_inst_var()
    case _ : fatal_exit("Select a valid option")
