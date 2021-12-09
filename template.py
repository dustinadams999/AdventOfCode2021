import numpy as np
import sys
from IPython import embed as shell

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]