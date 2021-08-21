#!/bin/sh
ROM_PATH="../stock roms/F1ACAD13 Quadra 650.rom"

mkdir -p build
./disassemble.py "$ROM_PATH" > build/out.S
