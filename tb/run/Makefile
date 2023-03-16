CWD=$(shell pwd)
export COCOTB_REDUCED_LOG_FMT = 1
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# A list of the Verilog source files to include. Paths can be absolute or relative; 
# if relative, they are interpreted as relative to the Makefile’s location.
VERILOG_SOURCES =$(CWD)/../../hdl/memory_model.sv

# Augment the default search path for module files
PYTHONPATH = ../src
export PYTHONPATH
$(info PYTHONPATH="$(PYTHONPATH)")

# The name of the Python module(s) to search for test functions - 
# if your tests are in a file called test_mydesign.py, MODULE would be set to test_mydesign.
MODULE := test

# Use this to indicate the instance in the hierarchy to use as the DUT.
TOPLEVEL = memory_model

GHDL_ARGS := --ieee=synopsys
COCOTB_HDL_TIMEUNIT = 1us
COCOTB_HDL_TIMEPRECISION = 1us
include $(shell cocotb-config --makefiles)/Makefile.sim

export COVERAGE = 1

#export COCOTB_SCHEDULER_DEBUG = 1

# when using gtkwave, the LXT output format is faster and most compact. 
# Use the "-lxt2" extended argument to activate LXT output
#SIM_ARGS += -lxt2

#PLUSARGS += | tee $(SIM_BUILD)/sim.log
