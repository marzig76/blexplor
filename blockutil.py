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


def compact_size(blockstream):
    size = ord(blockstream.read(1))

    if size < 0xfd:
        return size
    elif size == 0xfd:
        bytes = 2
    elif size == 0xfe:
        bytes = 4
    elif size == 0xff:
        bytes = 8
    else:
        return False

    return parse_int(blockstream, bytes)
