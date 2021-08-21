#!/bin/sh
ROM_PATH="../stock roms/F1ACAD13 Quadra 650.rom"

~/src/Retro68-build/toolchain/bin/m68k-apple-macos-as build/out.S -o build/out.elf
~/src/Retro68-build/toolchain/bin/m68k-apple-macos-objcopy --only-section=.text -O binary build/out.elf build/out.rom
./calc-apply-checksum.py build/out.rom

