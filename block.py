"""
This module contains a class for parsing a bitcoin block.

Author: Mike Marzigliano
"""

import datetime
from tx import tx
from blockutil import *


class block(object):
    """This class is for parsing the block header and block data fields."""

    def __init__(self, blockstream):
        """
        Initialize the class.

        Parse the values for all fields in the the block header and block.

        Arguemnts:
        blockstream - the stream of data to parse
        """
        self.magic_number = parse_int(blockstream, 4)
        self.block_size = parse_int(blockstream, 4)
        self.version = parse_int(blockstream, 4)
        self.prev_hash = parse_hash(blockstream)
        self.merkel_root = parse_hash(blockstream)
        self.time = parse_int(blockstream, 4)
        self.target = parse_int(blockstream, 4)
        self.nonce = parse_int(blockstream, 4)
        self.txcount = compact_size(blockstream)
        self.txs = []

        for i in range(0, self.txcount):
            self.txs.append(tx(blockstream))

    def __str__(self):
        """Build and return a string representing the block data."""
        blockstring = (
            '\nMagic Number:\t' + hex(self.magic_number) +
            '\nBlock Size:\t' + str(self.block_size) +
            '\nBlock Version:\t' + str(self.version) +
            '\nPrevious Hash:\t' + self.prev_hash +
            '\nMerkel Root:\t' + self.merkel_root +
            '\nTime:\t' + (
                datetime.datetime.fromtimestamp(
                    self.time
                ).strftime('%Y-%m-%d %H:%M:%S')) +
            '\nTarget:\t' + hex(self.target) +
            '\nNonce:\t' + str(self.nonce) +
            '\nTransaction Count:\t' + str(self.txcount)
        )

        for i in self.txs:
            blockstring += str(i)

        return blockstring
