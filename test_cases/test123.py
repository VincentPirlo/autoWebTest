# -*- coding: utf-8 -*-
import os
import os.path
from pathlib import Path


curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath, type(curpath))

c = os.path.dirname((curpath))
print(c)
dir = c+"\\output\\report"

print(dir)
