from blockutil import *
from script import script

class tx_output(object):


    def __init__(self, blockstream):
        self.value = parse_int(blockstream, 8)
        self.script_pk_bytes = compact_size(blockstream)
        self.script_pk = blockstream.read(self.script_pk_bytes)


    def __str__(self):
        script_pk = script(self.script_pk)

        return (
            '\nValue:\t' + str(self.value) +
            '\nPK Script Bytes:\t' + str(self.script_pk_bytes) +
            #'\nPKScript:\t' + self.script_pk.encode('hex')
            '\nScriptPubKey:\t' + str(script_pk)
        )
