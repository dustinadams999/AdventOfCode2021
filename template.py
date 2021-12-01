import numpy as np
import os
import pandas
import sys

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]