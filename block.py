import struct

blockfile = '/home/marzig76/.bitcoin/blocks/blk00255.dat'

with open(blockfile, 'rb') as blockstream:
    block = blockstream.read(1024)
