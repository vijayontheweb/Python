'''
Trace is essentially going to pause operations mid-script and then allow you to play with variables to understand whats going on

(Pdb) x
[1, 2, 5]
(Pdb) y
2
(Pdb) z
3
(Pdb) q
'''
import pdb

x = [1, 2, 5]
y = 2
z = 3
pdb.set_trace()
# TypeError: can only concatenate list (not "int") to list
result = x+y
print(result)
