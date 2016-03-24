import struct
import datetime
from tx import tx
from block import block
from blockutil import *

blockfile = '/home/marzig76/.bitcoin/blocks/blk00000.dat'

blockstream = open(blockfile, 'rb')

parsed_block = block(blockstream)
print parsed_block
