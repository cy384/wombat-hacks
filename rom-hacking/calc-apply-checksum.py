#!/usr/bin/env python3
import sys

rom_file = './build/out.rom' if len(sys.argv) == 1 else sys.argv[-1]

checksum = 0

with open(rom_file, mode="rb") as f:
	# skip first four bytes
	byte = f.read(4)

	while byte != b"":
		byte = f.read(2)
		checksum += int.from_bytes(byte, byteorder="big")

checksum &= 0b11111111111111111111111111111111

print("calculated checksum: " + f"{checksum:#0{10}X}".replace("X","x")[2:])

with open(rom_file, mode="r+b") as f:
	f.seek(0)
	f.write(checksum.to_bytes(4, byteorder="big"))
