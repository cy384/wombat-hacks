rom hacking
===========
Horrible hacks.  This is a "toolchain" in the loosest sense.  Read the (short) scripts before running them.

* disassemble.py is the absolute worst disassembler possible, seriously just the worst
* degenerate-rom.bash runs it on the original ROM to create an assembly file
* calc-apply-checksum.py calculates a new checksum for a ROM's data (everything after the first four bytes) and updates the checksum in it (first four bytes)
* generate-rom.bash compiles the assembly into a ROM using Retro68's m68k assembler, and runs calc-apply-checksum.py on it

So by running degenerate-rom.bash and then generate-rom.bash the output is a file that is exactly the same as the original ROM.  Why do this?  We can take the assembly "code" (again, it's the worst disassembly possible) and mess with it to make something new.

how to do anything
------------------
* read the scripts and make sure the paths are correct for your system (esp. Retro68 stuff)
* don't run hastily written scripts without reading them
* run degenerate-rom.bash
* optionally, mess with annotated-rom.S (try searching for djConfigTable), then copy to build/out.S
* run generate-rom.bash

now you'll have build/out.rom, which you can hopefully use to boot a real Wombat

things done so far to annotated-rom.S
-------------------------------------
* put the djMEMC config values with comments, based on Universal.a from the SuperMario source
* disassembled the djmemc memory sizing code, again based on the SuperMario source

