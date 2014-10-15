import os
from ctypes import *

print("path", os.path.abspath(__file__))

#mydll = WinDLL('Add')
mydll = cdll.LoadLibrary('Add.dll')

