#!/usr/bin/env python3
import sys

# a mac ROM has a simple checksum stored in the first four bits
# it's calculated by adding up every pair of bytes (skipping first four bytes)
# and then taking the bottom 32 bits of that sum

rom_file = './build/out.rom' if len(sys.argv) == 1 else sys.argv[-1]

checksum = 0
file_length = 0

# read ROM
with open(rom_file, mode="rb") as f:
	# skip first four bytes
	byte = f.read(4)
	file_length += 4

	byte = f.read(2)
	while byte != b"":
		file_length += 2
		checksum += int.from_bytes(byte, byteorder="big")
		byte = f.read(2)

checksum &= 0xFFFFFFFF
checksum_string = f"{checksum:#0{10}X}".replace("X","x")[2:]

print("calculated checksum: " + checksum_string)

# write checksum into file
with open(rom_file, mode="r+b") as f:
	f.seek(0)
	f.write(checksum.to_bytes(4, byteorder="big"))

# warn if the ROM is an unexpected size
if file_length != 1048576:
	print(f"your ROM isn't exactly 1MB! ({file_length} != 1048576)")

