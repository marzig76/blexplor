

class block(object):

    magic_number = ''
    block_size = ''
    version = ''
    prev_hash ''
    merkel_root = ''
    time = ''
    target = ''
    nonce = ''
    txcount = ''

    def __init__(self, blockstream):
        self.magic_number = hex(parse_int(blockstream))
        self.block_size = parse_int(blockstream)
        self.version = parse_int(blockstream)
        self.prev_hash = parse_hash(blockstream)
        self.merkel_root = parse_hash(blockstream)
        self.time = (
            datetime.datetime.fromtimestamp(
                parse_int(blockstream)
                ).strftime('%Y-%m-%d %H:%M:%S'))
        self.target = ''
        self.nonce = ''
        self.txcount = ''
