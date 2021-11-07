#!/bin/sh
ROM_PATH="../stock roms/F1ACAD13 Quadra 650.rom"

~/src/Retro68-build/toolchain/bin/m68k-apple-macos-as build/out.S -o build/out.elf
~/src/Retro68-build/toolchain/bin/m68k-apple-macos-objcopy --only-section=.text -O binary build/out.elf build/out.rom
./calc-apply-checksum.py build/out.rom

srec_cat build/out.rom -binary -split 4 1 -o build/U3.bin -binary
srec_cat build/out.rom -binary -split 4 2 -o build/U2.bin -binary
srec_cat build/out.rom -binary -split 4 3 -o build/U1.bin -binary
srec_cat build/out.rom -binary -split 4 0 -o build/U4.bin -binary

