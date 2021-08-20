djMEMC Information
==================

from [the mac68k confluence page](https://mac68k.info/wiki/display/mac68k/djMEMC+Information), with some formatting tweaks

The djMEMC is the name of the memory controller in the Centris and Quadra 610, 650, and 800 machines.  The Quadra 605 has a djMEMC derived memory controller and a lot of the information presented here is applicable to that machine as well.

The djMEMC is located at physical address 0x50F0E000 on all of the above machines.  It supports 10 banks of RAM, two are for the soldered on memory, and two per SIMM slot.  On the 610 machines that only have 2 SIMM slots, the last 4 banks are empty.

Additionally, the djMEMC supports interleaving of banks that are the same size.  Only 2 sequential banks can be interleaved, for example banks 0 & 1 can be interleaved, banks 2 & 3, 4 & 5, etc.  Interleaving gives a slight performance boost of around 10% to memory access.

The 610, 650, and 800 machines came with options of either 4 or 8MB of soldered memory.  In all cases, bank 0 had the first 4MB, and 8MB machines just had 4MB populated in bank 1 as well.  As a result, machines with 8MB of soldered memory can be interleaved and have a slightly faster memory access time than machines with 4MB of soldered memory.
Configuration registers:

All configuration registers are 32bits wide.  Unused bits default to 1 when read, but should be written as 0's.

0x50F0E000	Interleave Configuration Register
Bits 0-4 indicate which banks should have interleaving enabled

0: banks 0 & 1

1: banks 2 & 3

2: banks 4 & 5

3: banks 6 & 7

4: banks 8 & 9

Note that because odd numbered SIMM banks are empty on 610's, interleaving of RAM SIMMs is not available.

0x50F0E004	Bank 0 Configuration Register
Bit 8 indicated bank size. If bit 8 is 0, a bank size of 32MB or smaller will be used. If bit 8 is 1, a 64MB bank size will be used.
Bits 7-0 are address bits 29-22 for where the bank should appear in the physical address space. This also means the minimum bank size is 4MB (4MB = 0x400000, A22 is 1)

0x50F0E008	Bank 1 Configuration Register
This bank is empty on machines with 4MB soldered

0x50F0E00C	Bank 2 Configuration Register	As above

0x50F0E010	Bank 3 Configuration Register As above
This bank is empty on 610 machines

0x50F0E014	Bank 4 Configuration Register	As above

0x50F0E018	Bank 5 Configuration Register As above
This bank is empty on 610 machines

0x50F0E01C	Bank 6 Configuration Register	As above

0x50F0E020	Bank 7 Configuration Register As above
This bank is empty on 610 machines

0x50F0E024	Bank 8 Configuration Register	As above

0x50F0E028	Bank 9 Configuration Register As above
This bank is empty on 610 machines

0x50F0E02C	Memory Size Register
Bits 7-0 contain the address bits 29-22 for the end of physical memory.


Configuration Example
---------------------

Here is an example with 8MB soldered memory and some random RAM SIMM configuration: djmemcbankex1.png

In this case, the interleave config register should be set with 0x05, which indicates banks 0&1 should be interleaved, and banks 4&5 should be interleaved, and the rest not interleaved.  The memory size register should be set to 0x2E, which is bank 5's configuration register value + the size of bank 5.


Mac ROM Initialization
----------------------

The Mac ROM will only ever initialize the djMEMC with bank configuration registers bit 8 set to 1.  This means each bank will be limited to 32MB in size.  The RAM will be organized contiguously, as in the above example.  This means the configuration register for bank 0 will always have bits 7-0 set to 0, and all subsequent banks will be set to start immediately after the previous bank ends, also as show in the above example.  This presents a single contiguous chunk of physical RAM to the processor, rather than leaving holes in between banks.  If a bank is set to start before the previous bank ends, the overlapping space in the previous bank is "gone".  It isn't addressable on the bus since the subsequent bank is occupying its address space.  This is the case with a bank being populated with 64MB, but the Mac ROM only configuring it for 32MB.
Reconfiguring the controller:

Reconfiguring the controller when executing from RAM (or you care about RAM contents at all).  In order to grow a bank, you need to move all subsequent banks out by the amount you're adding to the current bank.  Here's an example of a system with two 128MB SIMMs installed, as configured by the Mac OS ROM, and you want to grow it out to utilize the full 64MB/bank: djmemcbankex2.png

This shows where each bank was in the physical address space as the Mac ROM configured it, then "inserting" 32MB/bank in order to support each bank being 64MB in size.  On the right side, it shows each bank's configuration register after reconfiguration, and the new physical address of each bank.  Notice that existing memory locations have moved out, so if you have anything pointing to those addresses, the pointer now points to the wrong place in memory.  If you're executing from any of the relocated banks, your instruction pointer is now invalid and you'll crash.

