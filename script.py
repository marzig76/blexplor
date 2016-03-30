import struct
from opcode import opcode


class script(object):

    opcodes = opcode().opcodes

    def __init__(self, bytes):
        self.bytes = bytes

    def __str__(self):

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
                data_len = parse_int(self.bytes[byte_count+1:byte_count+3], 2)
                # set the skip counter to 2, plus however many bytes are coming
                skip_count = (2 + data_len)
                # set a flag to not display the next 2 bytes either.
                print_skip = 2
            elif byte == 0x4e:
                # the next four bytes tells us how many bytes of data follows
                data_len = parse_int(self.bytes[byte_count+1:byte_count+5], 4)
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
