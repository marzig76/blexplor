import struct
import datetime

blockfile = '/home/marzig76/.bitcoin/blocks/blk00000.dat'

blockstream = open(blockfile, 'rb')

def reverse_bytes(bytes):
    reversed = ""
    for i in range(0, len(bytes), 2):
        reversed = bytes[i:i+2] + reversed
    return reversed


print 'Magic Number: ', hex(struct.unpack('I', blockstream.read(4))[0])
print 'Block size: ', struct.unpack('I', blockstream.read(4))[0]

print 'Version: ', struct.unpack('I', blockstream.read(4))[0]
print 'Prev Hash: ', reverse_bytes(blockstream.read(32).encode("hex"))
print 'Merkel Root: ', reverse_bytes(blockstream.read(32).encode("hex"))
print 'time: ', (
    datetime.datetime.fromtimestamp(
        struct.unpack('I', blockstream.read(4))[0]
        ).strftime('%Y-%m-%d %H:%M:%S'))


print 'target: ', hex(struct.unpack('I', blockstream.read(4))[0])
print 'nonce: ', struct.unpack('I', blockstream.read(4))[0]

print 'txcount: ', ord(blockstream.read(1))

#print blockstream.read(32).encode("hex")
