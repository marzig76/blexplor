import struct


def reverse_bytes(bytes):
    reversed = ""
    for i in range(0, len(bytes), 2):
        reversed = bytes[i:i+2] + reversed
    return reversed


def parse_int(blockstream):
    return struct.unpack('I', blockstream.read(4))[0]


def parse_hash(blockstream):
    return reverse_bytes(blockstream.read(32).encode("hex"))
