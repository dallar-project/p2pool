import os
import platform
 
from twisted.internet import defer
 
from .. import data, helper
from p2pool.util import pack
 
 
P2P_PREFIX = 'd9d7c2d4'.decode('hex')
P2P_PORT = 20032
ADDRESS_VERSION = 30
RPC_PORT = 20033
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '000005942766af8f99efd3b13fdf5be9ef43981273430f593c669cd1bfe4f586')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: __import__('dallar_subsidy').getBlockBaseValue(height+1)
POW_FUNC = data.hash_throestl
BLOCK_PERIOD = 60 # s
SYMBOL = 'DAL'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Dallar2') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dallar/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dallar'), 'dallar.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.dallar.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.dallar.org/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.dallar.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8