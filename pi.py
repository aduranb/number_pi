import sys

sys.path.insert(0, 'v2')
from computepi import compute_pi

args = sys.argv

try:
    nodecimals = int(args[1])
    print(compute_pi(nodecimals=nodecimals))
except Exception:
    print('argument must be an integer')
