#import os
from ctypes import *

#print("path", os.path.abspath(__file__))

#mydll = WinDLL('Add')

# Load DLL file 'Explore'
mydll = cdll.LoadLibrary('Explore.dll')

# Demo simple call to C function with arguments and printing returned result
print('mydll.sum(4,7) is' , mydll.sum(4, 7))

# Demo simple printing in C of a message from Python
mydll.print_hi(b"karlos")

# Demo pointer to primitive type
age = c_int(0)
mydll.get_age(byref(age))
print("your age is:", age.value)

# Demo string buffer
name = create_string_buffer(80)
mydll.get_name(name)
print("your name is:", name.value)

# Demo C data structure
class Point(Structure):
  _fields_ = [("x", c_int),
              ("y", c_int)]

point = Point(0, 0)
print('point: x={0}, y={1}'.format(point.x, point.y))
mydll.set_point(byref(point), c_int(5), c_int(18))
print('point: x={0}, y={1}'.format(point.x, point.y))