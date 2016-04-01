"""
This module contains a class for parsing bitcoin tx outputs.

Author: Mike Marzigliano
"""
from blockutil import *
from script import script


class tx_output(object):
    """This class is for parsing bitcoin tx inputs."""

    def __init__(self, blockstream):
        """
        Initialize the class.

        Parse the values for all fields in each tx output.

        Arguemnts:
        blockstream - the stream of data to parse
        """
        self.value = parse_int(blockstream, 8)
        self.script_pk_bytes = compact_size(blockstream)
        self.script_pk = blockstream.read(self.script_pk_bytes)

    def __str__(self):
        """Build and return a string representing tx output data."""
        script_pk = script(self.script_pk)

        return (
            '\nValue:\t' + str(self.value) +
            '\nPK Script Bytes:\t' + str(self.script_pk_bytes) +
            # '\nPKScript:\t' + self.script_pk.encode('hex')
            '\nScriptPubKey:\t' + str(script_pk)
        )
