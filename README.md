wombat-hacks
============
This is a repository for information and code to push the capabilities of the codename "Wombat" machines (the Centris 650, Quadra 650, and Quadra 800) as far as possible.

Some project goals:
* stable and functional overclock beyond 40 MHz
* support for 64MB and 128MB RAM SIMMs

current project status
----------------------
Overclocks to 45 MHz have been achieved.  Faster speeds remain elusive.  bbraun has successfully experimented with allowing larger SIMMs via a custom ROM with hardcoded large-SIMM bits.

ultra-wombat-hax-tool
---------------------
This is a simple program that reads and pretty-prints data from the djmemc memory controller registers.  Useful for figuring out how the ROM is configuring the machine.

external docs
-------------
Reference copies of various useful documents and notes.

stock roms
----------
Reference copies of the two Wombat ROMs I'm aware of: checksum F1A6F343 (Centris 650?) and F1ACAD13 (Quadra 650, Quadra 800?).  Supposedly these were also used for the Centris/Quadra 610 machines.
