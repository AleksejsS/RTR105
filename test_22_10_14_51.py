'''
n = 5
while n > 0:
    print(n)
    n = n - 1
print('blastoff!')
print(n)
'''
'''
n = 5
while n > 0:
    print('lather')
    print('rinse')
print('dry off!')
'''
'''
n = 0
while n > 0:
    print('lather')
    print('rinse')
print('dry off!')
'''
'''
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('done!')
''' 
'''
while True:
    line = raw_input('hello there')
    if line == 'done':
        break
    print(line)
print('done!')
'''
'''
while True:
    line = raw_input('meow')
    if line == 'done':
        break
    print(line)
    print('done!')
'''
'''
while True:
    line = raw_input('woof')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done!')
'''
'''
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done!')
'''
'''
for i in [5,4,3,2,1]:
    print(i)
print('blastoff!')
'''
'''
friends = ['joseph','glenn','sally']
for friend in friends:
    print('happy new year:', friend)
print('done!')
'''
'''
print('before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('after')
'''

largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far, the_num)

    print('after', largest_so_far)
    
