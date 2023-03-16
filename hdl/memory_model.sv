//------------------------------------------------------------------------
//				Memory Model RTL - www.verificationguide.com
//------------------------------------------------------------------------
/*
              -----------------
              |               |
    addr ---->|               |
              |               |------> rdata
              | Memory Model  |
   wdata ---->|               |
              |               | 
              -----------------
                   ^     ^
                   |     |
                wr_en  rd_en

-------------------------------------------------------------------------- */
module memory_model
    #(  parameter ADDR_WIDTH = 4,
        parameter DATA_WIDTH = 8 
    )
    (
        input clk,
        input reset,
    
        //control signals
        input [ADDR_WIDTH-1:0]  addr,
        input                   wr_en,
        input                   rd_en,
        
        //data signals
        input  [DATA_WIDTH-1:0] wdata,
        output [DATA_WIDTH-1:0] rdata
    ); 
  
    reg [DATA_WIDTH-1:0] rdata;

    //Memory
    reg [DATA_WIDTH-1:0] mem [2**ADDR_WIDTH];

    //Reset 
    always @(posedge reset) 
        for(int i=0;i<2**ADDR_WIDTH;i++) mem[i]=8'hFF;

    // Write data to Memory
    always @(posedge clk) 
        if (wr_en)    mem[addr] <= wdata;

    // Read data from memory
    always @(posedge clk)
        if (rd_en) rdata <= mem[addr];

    // the "macro" to dump signals
    `ifdef COCOTB_SIM
        initial begin
            $dumpfile ("memory.vcd");
            $dumpvars (0, memory_model);
            #1;
        end
    `endif
endmodule
