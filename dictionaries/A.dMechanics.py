# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    A.dMechanics.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/20 23:06:19 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/20 23:06:40 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def header(s):
    print('\n=========', s.upper(), '============')

header('A1 create')
person ={}

person['firstName'] = 'Red'
person['email']     = 'red@gmail.com'
person['gender']    = 'male'
person['phone']     = '310-555-1212'

print(person)


header('A2 read')
print('person:', person)
print('a person firstName:', person['firstName'])
print('b person firstName:', person.get('firstName')) #prevents runtime-error when DNE vs using 'a'
print('c person lastName:', person.get('lastName', 'No last name found!')) #when DNE, can return optional value 

header('A3 update')
person['firstName'] = 'Orange'
print(person)


header('A4 delete')
del person['phone']
print(person)

header('A5 quantity')
print('quantity: ' + str(len(person)))


header('A6 iterate thru dictionary item keys')
for key in person: #python defaults to using keys
    print(key)
    
header('A6 iterate thru dictionary item values')
for v in person.values(): #python defaults to using keys
    print(v)
    
    
header('A7 list of keys')
keys = list(person) #defaults to key
print(keys)

header('A7 list of values')
vals = list(person.values()) #explicitly referencing values
print(vals)


header('A8 check existence')
exists = 'firstName' in person
print(' fn exists as key? ', exists)
if exists:
    print( 'firstName: ', person['firstName'])
else:
    print( 'firstName does not exist')


header('A9 aliasing vs copying')
p1 = person #alias
print('person ', person)
print('p1 pointing to person? :', p1 is person)
print('p1 ', p1)
p1['firstName'] = 'Yellow'
print('person ', person)