
# config OP Codes
op_codes = {}
op_codes['OP_FALSE'] = 0x00
op_codes['OP_NOP'] = 0x61
op_codes['OP_IF'] = 0x63
op_codes['OP_ELSE'] = 0x67
op_codes['OP_ENDIF'] = 0x68

# input
value = 0x61

# push data to stack
if 0x01 <= value <= 0x4b:
    data = stream.read(value)
elif value == 0x4c:
    data = stream.read(stream.read(1))
elif value == 0x4d:
    data = stream.read(stream.read(2))
elif value == 0x4e:
    data = stream.read(stream.read(4))
elif value in op_codes.values():
    for key in op_codes:
        if op_codes[key] == value:
            print key
else:
    print False
