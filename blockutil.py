import struct

def parse_int(blockstream, bytes):
    if bytes == 2:
        format = 'H'
    elif bytes == 4:
        format = 'I'
    elif bytes == 8:
        format = 'Q'
    else:
        return False
    return struct.unpack(format, blockstream.read(bytes))[0]


def parse_hash(blockstream):
    return blockstream.read(32)[::-1].encode("hex")
