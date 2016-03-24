import struct
import datetime
from blockutil import *

blockfile = '/home/marzig76/.bitcoin/blocks/blk00000.dat'

blockstream = open(blockfile, 'rb')

print 'Magic Number: ', hex(parse_int(blockstream))
print 'Block size: ', parse_int(blockstream)

print 'Version: ', parse_int(blockstream)
print 'Prev Hash: ', parse_hash(blockstream)
print 'Merkel Root: ', parse_hash(blockstream)
print 'time: ', (
    datetime.datetime.fromtimestamp(
        parse_int(blockstream)
        ).strftime('%Y-%m-%d %H:%M:%S'))


print 'target: ', hex(parse_int(blockstream))
print 'nonce: ', parse_int(blockstream)

print 'txcount: ', ord(blockstream.read(1))

#print blockstream.read(32).encode("hex")
