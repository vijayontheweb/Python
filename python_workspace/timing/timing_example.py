import time
import timeit


def get_default_array(num):
    num_array = []
    for index in range(num):
        num_array.append(str(index))
    return num_array


def get_list_comprehension_array(num):
    return [str(index) for index in range(num)]


def get_mapped_array(num):
    return list(map(str, range(num)))


start_time = time.time()
get_default_array(10000000)
# print(get_default_array(1000000))
end_time = time.time()
print(end_time-start_time)
start_time = time.time()
get_list_comprehension_array(10000000)
# print(get_list_comprehension_array(1000000))
end_time = time.time()
print(end_time-start_time)
start_time = time.time()
get_mapped_array(10000000)
# print(get_mapped_array(1000000))
end_time = time.time()
print(end_time-start_time)
'''
timeit module
'''
print('using timeit module')
stmt1 = '''
get_default_array(100)
'''

setup1 = '''
def get_default_array(num):
    num_array = []
    for index in range(num):
        num_array.append(str(index))
    return num_array
'''
print(timeit.timeit(stmt1, setup1, number=100000))

stmt2 = '''
get_list_comprehension_array(100)
'''

setup2 = '''
def get_list_comprehension_array(num):
    return [str(index) for index in range(num)]
'''

print(timeit.timeit(stmt2, setup2, number=100000))

stmt3 = '''
get_mapped_array(100)
'''

setup3 = '''
def get_mapped_array(num):
    return list(map(str, range(num)))
'''

print(timeit.timeit(stmt3, setup3, number=100000))
