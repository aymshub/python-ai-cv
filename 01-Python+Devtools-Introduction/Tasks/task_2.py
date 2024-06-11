import tempfile
import os
from os import walk

for (dirpath, dirnames, filenames) in walk('.'):
   for file in filenames:
       if file.endswith('.py'):
           print(file)
