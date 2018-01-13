from p2pool.bitcoin import networks
 
PARENT = networks.nets['dallar']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 30 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'c22120aab187c089'.decode('hex')
PREFIX = '567ca4a26746b15f'.decode('hex')
P2P_PORT = 2832
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 3032
BOOTSTRAP_ADDRS = 'pool.dallar.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-dal'
VERSION_CHECK = lambda v: None if 1030000 <= v else 'Dallar version too old. Upgrade to 1.3.0 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17