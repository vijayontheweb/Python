'''
basic mathematical functions such as trignometric, logarithmic, floor, ceiling
'''
import math
from math import pi

value = 4.35
print(f'FLOOR -> {math.floor(value)}')  # 4
print(f'CEIL -> {math.ceil(value)}')    # 5
print(f'ROUND -> {round(value)}')		# 4	Built into Python itself
print(f'PI -> {math.pi}')				# 3.141592653589793

print(f'PI -> {pi}')				    # 3.141592653589793
print(f'E -> {math.e}')				    # 2.718281828459045
print(f'INFINITY -> {math.inf}')  # inf
print(f'NOT A NUMBER -> {math.nan}')  # nan

print(f'math.log(math.e) -> {math.log(math.e)}')  # 1.0
# Returns the logarithm of X to the given base
# 2.0 i.e. 10 to the power of 2 gives 100
print(f'math.log(x,base) -> {math.log(100,10)}')

# Trignometric Functions
print(f'SIN -> {math.sin(10)}')  # -0.5440211108893698
print(f'DEGREES -> {math.degrees(pi/2)}')  # 90.0
print(f'RADIANS -> {math.radians(180)}')  # 3.141592653589793
