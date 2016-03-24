from blockutil import *

class tx(object):

    version = ''
    tx_in_count = ''
    tx_in = ''
    tx_out_count = ''
    tx_out = ''
    lock_time = ''

    def __init__(self, blockstream):
        self.version = parse_int(blockstream, 4)
        self.tx_in_count = compact_size(blockstream)


    def __str__(self):
        return 'finish me!'
