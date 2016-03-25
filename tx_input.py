from blockutil import *

class tx_input(object):


    def __init__(self, blockstream):
        self.prev_hash = parse_hash(blockstream)
        self.index = parse_int(blockstream, 4)
        self.script_bytes = compact_size(blockstream)
        self.sigscript = blockstream.read(self.script_bytes)
        self.sequence = parse_int(blockstream, 4)


    def __str__(self):
        return (
            '\nPrevious Hash:\t' + str(self.prev_hash) +
            '\nIndex:\t' + str(self.index) +
            '\nScript Bytes:\t' + str(self.script_bytes) +
            '\nSigScript:\t' + self.sigscript.encode('hex') +
            '\nSequence:\t' + str(self.sequence)
        )
