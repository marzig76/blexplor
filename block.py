import datetime
from blockutil import *


class block(object):

    magic_number = ''
    block_size = ''
    version = ''
    prev_hash = ''
    merkel_root = ''
    time = ''
    target = ''
    nonce = ''
    txcount = ''

    def __init__(self, blockstream):
        self.magic_number = parse_int(blockstream, 4)
        self.block_size = parse_int(blockstream, 4)
        self.version = parse_int(blockstream, 4)
        self.prev_hash = parse_hash(blockstream)
        self.merkel_root = parse_hash(blockstream)
        self.time = parse_int(blockstream, 4)
        self.target = parse_int(blockstream, 4)
        self.nonce = parse_int(blockstream, 4)
        self.txcount = ord(blockstream.read(1))

    def __str__(self):
        return (
            'Magic Number:\t' + hex(self.magic_number) +
            '\nBlock Size:\t' + str(self.block_size) +
            '\nVersion:\t' + str(self.version) +
            '\nPrevious Hash:\t' + self.prev_hash +
            '\nMerkel Root:\t' + self.merkel_root +
            '\nTime:\t' + (
                datetime.datetime.fromtimestamp(
                    self.time
                ).strftime('%Y-%m-%d %H:%M:%S')) +
            '\nTarget:\t' + hex(self.target) +
            '\nNonce:\t' + str(self.nonce) +
            '\nTransactions:\t' + str(self.txcount)
        )
