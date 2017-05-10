"""A simple module housing Bitcoin Script OP Code values."""


class opcode(object):
    """Define Bitcoin Script OP Code values."""

    opcodes = {}

    # Constants
    opcodes['OP_FALSE'] = 0x00
    opcodes['OP_1NEGATE'] = 0x4f
    opcodes['OP_TRUE'] = 0x51
    opcodes['OP_2'] = 0x52
    opcodes['OP_3'] = 0x53
    opcodes['OP_4'] = 0x54
    opcodes['OP_5'] = 0x55
    opcodes['OP_6'] = 0x56
    opcodes['OP_7'] = 0x57
    opcodes['OP_8'] = 0x58
    opcodes['OP_9'] = 0x59
    opcodes['OP_10'] = 0x5a
    opcodes['OP_11'] = 0x5b
    opcodes['OP_12'] = 0x5c
    opcodes['OP_13'] = 0x5d
    opcodes['OP_14'] = 0x5e
    opcodes['OP_15'] = 0x5f
    opcodes['OP_16'] = 0x60

    # Flow Control
    opcodes['OP_NOP'] = 0x61
    opcodes['OP_IF'] = 0x63
    opcodes['OP_NOTIF'] = 0x64
    opcodes['OP_ELSE'] = 0x67
    opcodes['OP_ENDIF'] = 0x68
    opcodes['OP_VERIFY'] = 0x69
    opcodes['OP_RETURN'] = 0x6a

    # Stack
    opcodes['OP_TOALTSTACK'] = 0x6b
    opcodes['OP_FROMALTSTACK'] = 0x6c
    opcodes['OP_IFDUP'] = 0x73
    opcodes['OP_DEPTH'] = 0x74
    opcodes['OP_DROP'] = 0x75
    opcodes['OP_DUP'] = 0x76
    opcodes['OP_NIP'] = 0x77
    opcodes['OP_OVER'] = 0x78
    opcodes['OP_PICK'] = 0x79
    opcodes['OP_ROLL'] = 0x7a
    opcodes['OP_ROT'] = 0x7b
    opcodes['OP_SWAP'] = 0x7c
    opcodes['OP_TUCK'] = 0x7d
    opcodes['OP_2DROP'] = 0x6d
    opcodes['OP_2DUP'] = 0x6e
    opcodes['OP_3DUP'] = 0x6f
    opcodes['OP_2OVER'] = 0x70
    opcodes['OP_2ROT'] = 0x71
    opcodes['OP_2SWAP'] = 0x72

    # Splice
    opcodes['OP_CAT'] = 0x7e
    opcodes['OP_SUBSTR'] = 0x7f
    opcodes['OP_LEFT'] = 0x80
    opcodes['OP_RIGHT'] = 0x81
    opcodes['OP_SIZE'] = 0x82

    # Bitwise logic
    opcodes['OP_INVERT'] = 0x83
    opcodes['OP_AND'] = 0x84
    opcodes['OP_OR'] = 0x85
    opcodes['OP_XOR'] = 0x86
    opcodes['OP_EQUAL'] = 0x87
    opcodes['OP_EQUALVERIFY'] = 0x88

    # Arithmetic
    opcodes['OP_1ADD'] = 0x8b
    opcodes['OP_1SUB'] = 0x8c
    opcodes['OP_2MUL'] = 0x8d
    opcodes['OP_2DIV'] = 0x8e
    opcodes['OP_NEGATE'] = 0x8f
    opcodes['OP_ABS'] = 0x90
    opcodes['OP_NOT'] = 0x91
    opcodes['OP_0NOTEQUAL'] = 0x92
    opcodes['OP_ADD'] = 0x93
    opcodes['OP_SUB'] = 0x94
    opcodes['OP_MUL'] = 0x95
    opcodes['OP_DIV'] = 0x96
    opcodes['OP_MOD'] = 0x97
    opcodes['OP_LSHIFT'] = 0x98
    opcodes['OP_RSHIFT'] = 0x99
    opcodes['OP_BOOLAND'] = 0x9a
    opcodes['OP_BOOLOR'] = 0x9b
    opcodes['OP_NUMEQUAL'] = 0x9c
    opcodes['OP_NUMEQUALVERIFY'] = 0x9d
    opcodes['OP_NUMNOTEQUAL'] = 0x9e
    opcodes['OP_LESSTHAN'] = 0x9f
    opcodes['OP_GREATERTHAN'] = 0xa0
    opcodes['OP_LESSTHANOREQUAL'] = 0xa1
    opcodes['OP_GREATERTHANOREQUAL'] = 0xa2
    opcodes['OP_MIN'] = 0xa3
    opcodes['OP_MAX'] = 0xa4
    opcodes['OP_WITHIN'] = 0xa5

    # Crypto
    opcodes['OP_RIPEMD160'] = 0xa6
    opcodes['OP_SHA1'] = 0xa7
    opcodes['OP_SHA256'] = 0xa8
    opcodes['OP_HASH160'] = 0xa9
    opcodes['OP_HASH256'] = 0xaa
    opcodes['opcodeSEPARATOR'] = 0xab
    opcodes['OP_CHECKSIG'] = 0xac
    opcodes['OP_CHECKSIGVERIFY'] = 0xad
    opcodes['OP_CHECKMULTISIG'] = 0xae
    opcodes['OP_CHECKMULTISIGVERIFY'] = 0xaf

    # Locktime
    opcodes['OP_CHECKLOCKTIMEVERIFY'] = 0xb1
    opcodes['OP_CHECKSEQUENCEVERIFY'] = 0xb2

    # Pseudo-words
    opcodes['OP_PUBKEYHASH'] = 0xfd
    opcodes['OP_PUBKEY'] = 0xfe
    opcodes['OP_INVALIDOPCODE'] = 0xff

    # Reserved words
    opcodes['OP_RESERVED'] = 0x50
    opcodes['OP_VER'] = 0x62
    opcodes['OP_VERIF'] = 0x65
    opcodes['OP_VERNOTIF'] = 0x66
    opcodes['OP_RESERVED1'] = 0x89
    opcodes['OP_RESERVED2'] = 0x8a
    opcodes['OP_NOP1'] = 0xb0
    opcodes['OP_NOP4'] = 0xb3
    opcodes['OP_NOP5'] = 0xb4
    opcodes['OP_NOP6'] = 0xb5
    opcodes['OP_NOP7'] = 0xb6
    opcodes['OP_NOP8'] = 0xb7
    opcodes['OP_NOP9'] = 0xb8
    opcodes['OP_NOP10'] = 0xb9
