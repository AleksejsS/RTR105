'''
>>> fruit = 'banana'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index +1
'''
'''
fruit =  'banana'
for letter in fruit:
    print(letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
'''
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
        print(count)
'''

	

if word < 'banana':
	print('your word,' + word + ', comes before banana.')
elif word > 'banana':
	print('your word,' + word + ', comes after banana.')
else:
    print('all right, bananas.')
