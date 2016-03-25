from blockutil import *

class tx_output(object):


    def __init__(self, blockstream):
        self.value = parse_int(blockstream, 8)
        self.pk_script_bytes = compact_size(blockstream)
        self.pk_script = blockstream.read(self.pk_script_bytes)


    def __str__(self):
        return (
            '\nValue Hash:\t' + str(self.value) +
            '\nPK Script Bytes:\t' + str(self.pk_script_bytes) +
            '\nPKScript:\t' + self.pk_script.encode('hex')
        )
