import logging
import os
import ConfigParser
# Path to the templates directory
RES = os.path.join(os.path.dirname(__file__), 'res')
TEMPLATES = os.path.join(RES, 'templates')
# Path to the directory containing the Quagga-Fibbing installation
BIN = '/opt/fibbing'

CFG = ConfigParser.ConfigParser()
with open(os.path.join(RES, 'default.cfg'), 'r') as f:
    CFG.readfp(f)

# Warnings are orange
logging.addLevelName(logging.WARNING,
                     "\033[1;43m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
# Errors are red
logging.addLevelName(logging.ERROR,
                     "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
# Debug is green
logging.addLevelName(logging.DEBUG,
                     "\033[1;42m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
# Information messages are blue
logging.addLevelName(logging.INFO,
                     "\033[1;44m%s\033[1;0m" % logging.getLevelName(logging.INFO))

# Critical messages are violet
logging.addLevelName(logging.CRITICAL,
                     "\033[1;45m%s\033[1;0m" % logging.getLevelName(logging.CRITICAL))

log = logging.getLogger(__name__)
fmt = logging.Formatter('%(relativeCreated)d %(filename)s [%(levelname)s]  %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(fmt)
log.addHandler(handler)
