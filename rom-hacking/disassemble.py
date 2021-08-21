#!/usr/bin/env python3
import sys

rom_file = '../stock roms/F1ACAD13 Quadra 650.rom' if len(sys.argv) == 1 else sys.argv[-1]

with open(rom_file, mode="rb") as f:
	byte = f.read(4)

	while byte != b"":
		byte_val = int.from_bytes(byte, byteorder="big")
		print(f".int {byte_val:#0{10}x}")
		byte = f.read(4)

