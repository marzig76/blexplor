from blockutil import *
from tx_input import tx_input
from tx_output import tx_output

class tx(object):


    def __init__(self, blockstream):
        self.version = parse_int(blockstream, 4)
        self.tx_input_count = compact_size(blockstream)
        self.tx_inputs = []

        for i in range(0, self.tx_input_count):
            self.tx_inputs.append(tx_input(blockstream))

        self.tx_output_count = compact_size(blockstream)
        self.tx_outputs = []

        for i in range(0, self.tx_output_count):
            self.tx_outputs.append(tx_output(blockstream))

        self.lock_time = parse_int(blockstream, 4)

    def __str__(self):
        txstring = (
            '\n-------------------------------------' +
            '\nTx Version:\t' + str(self.version) +
            '\nInput Count:\t' + str(self.tx_input_count) +
            '\nInputs:'
        )

        for i in self.tx_inputs:
            txstring += str(i)

        txstring += (
            '\nOutput Count:\t' + str(self.tx_output_count) +
            '\nOutputs:'
        )

        for i in self.tx_outputs:
            txstring += str(i)

        txstring += '\nLock Time:\t' + str(self.lock_time)
        txstring += '\n-------------------------------------'
        return txstring
