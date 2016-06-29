"""
This module contains classes to interperet scriptpubkeys and scriptSigs.

Author: Mike Marzigliano
"""
import struct
from opcode import opcode


class script(object):
    """
    This class is for interpereting bitcoin scriptPubKeys.

    Define the existing OP Codes by creating an instance of the op_code class.
    """

    opcodes = opcode().opcodes

    def __init__(self, bytes):
        """
        Take the given bytes and call the interpereter.

        Arguemnts:
        bytes - the data to interperet (scriptPubKey)
        """
        self.bytes = bytes
        self.stack = self.interperet()

    def interperet(self):
        """
        Interperet data into OP Codes.

        Loop through each byte.  Either read the appropriate number of bytes
        as data, or simply translate the byte into its corresponding OP code.
        """
        # set up some counters
        byte_count = 0
        skip_count = 0
        print_skip = 0
        stack = ''

        # build the script
        

        return stack

    def __str__(self):
        """Return a string representing the scriptpubkey."""
        return self.stack


class scriptSig(object):
    """This class is for interpereting bitcoin scriptSigs."""

    signature = ''
    pubkey = ''

    def __init__(self, bytes):
        """
        Take the scriptSig and extract the signature and public key.

        Arguemnts:
        bytes - the data to interperet (scriptSig)
        """
        sigbytes_hex = bytes[:1].encode('hex')
        sigbytes = int(sigbytes_hex, 16)
        self.signature = bytes[1:sigbytes+1]

        pos = sigbytes+1
        pubkeybytes_hex = bytes[pos:pos+1].encode('hex')
        if pubkeybytes_hex != '':
            pubkeybytes = int(pubkeybytes_hex, 16)
            pos += 1
            self.pubkey = bytes[pos:pos+pubkeybytes]
