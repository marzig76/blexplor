import struct

tx_string = "0100000001e89d4e89c3d4acf86ecf5be939865b191185084eb78085faab492bb0d2d5955d000000006a47304402207780db6e98b5dd232ef7098e2461167e90793214d8e6831c03ec27ae6058428e02203e61edfad7446fc59b76e7d012d3f9888a2f99b0b2aebc4446f6b7f1590d65f90121038480b6c99e9bff2861a6dc4cb5195781b386b1561f9ad6f1cfdb51a9f6dc8e1affffffff02e9960000000000001976a914fb96940932cc00274cf61e423623e0eb0aa326cf88ac31aa0000000000001976a91417bc025365153025a45c0ae41b4d582334e79a3488ac00000000"
decoded = tx_string.decode("hex")
#tx = bytearray(decoded)

pos = 0

# version
version_len = 4
version = struct.unpack("I", decoded[pos:version_len])
pos += version_len

print version