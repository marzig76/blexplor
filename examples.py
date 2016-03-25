from block import block

blockfile = '/home/marzig76/.bitcoin/blocks/blk00000.dat'

blockstream = open(blockfile, 'rb')

parsed_block = block(blockstream)
print parsed_block
