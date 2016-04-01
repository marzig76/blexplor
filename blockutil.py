"""
This module contains functions to parse bitcoin blocks.

Author: Mike Marzigliano
"""

import struct


def parse_int(blockstream, bytes):
    """
    Parse an integer value from a data stream.

    Based on the number of bytes, determine the appropriate struct format.

    Arguments:
    blockstream - the stream of data to parse
    bytes - the number of bytes to read
    """
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
    """
    Simply return the 32 byte hexidecimal hash from the stream.

    Reverse the bytes before encoding it in hex.

    Arguments:
    blockstream - the stream of data to parse
    """
    return blockstream.read(32)[::-1].encode("hex")


def compact_size(blockstream):
    """
    Return a variable length parsed integer.

    Read the appropriate number of bytes based on the values of the first byte.
    Use the above parse_int function to do the work.

    Arguments:
    blockstream - the stream of data to parse
    """
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
