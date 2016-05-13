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
        for i in self.bytes:
            byte = ord(i)

            # Either find a corresponding opcode
            # or read the number of appropriate bytes of data.
            # If just reading bytes, skip checking them as opcodes
            if byte == 0x6a:
                # 0x6a (OP_RETURN) the rest of the script is just data.
                # skip it all
                skip_count = len(self.bytes)
            elif skip_count > 0:
                if print_skip == 0:
                    stack += i.encode('hex')
                else:
                    print_skip -= 1
                skip_count -= 1
                if skip_count == 0:
                    stack += ' '
            elif 0x01 <= byte <= 0x4b:
                # this byte tells us how many bytes of data follows
                # set the skip counter - don't check the next bytes for opcodes
                skip_count = byte
            # elif byte == 0x4c:
                # nothing to do for 0x4c (OP_PUSHDATA1)
                # nothing will be processed and
                # the next byte will contain the number of bytes of data
            elif byte == 0x4d:
                # the next 2 bytes tells us how many bytes of data follows
                data_len = struct.unpack(
                    '>H', self.bytes[byte_count+1:byte_count+3]
                    )[0]
                # set the skip counter to 2, plus however many bytes are coming
                skip_count = (2 + data_len)
                # set a flag to not display the next 2 bytes either.
                print_skip = 2
            elif byte == 0x4e:
                # the next four bytes tells us how many bytes of data follows
                data_len = struct.unpack(
                    '>I', self.bytes[byte_count+1:byte_count+5]
                    )[0]
                # set the skip counter to 4, plus however many bytes are coming
                skip_count = (4 + data_len)
                # # set a flag to not display the next 4 bytes either.
                print_skip = 4
            # else, just look up the opcode
            elif byte in self.opcodes.values():
                for key in self.opcodes:
                    if self.opcodes[key] == byte:
                        stack += key + ' '

            byte_count += 1

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
