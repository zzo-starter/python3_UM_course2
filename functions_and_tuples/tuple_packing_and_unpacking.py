# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tuple_packing_and_unpacking.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/24 00:25:05 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/24 00:54:53 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')


#===========
header('Tuple Packing')
#this tuple
julia1 = ('a',123,'b',456, 'c')
#same as this tuple
julia2 = 'a',123,'b',456,'c'

print(julia1,'==', julia2)

a,b,c,d = 1,2,3,4
print(a,b,c,d)

#==========
header('Return multiple values via a Tuple')
def getUser(id):
    #return id and name
    return ( id,'Julia','Roberts')

print( getUser(123) )


#==========
header('Tuple Unpacking')

julia = 'Julia',123,'Roberts',22,'actress'
fname, id, lname,age,profession = julia

print('id:', id)
print('first name:', fname)
print('last name', lname)


#==========
header('Tuple as Arguments')

def add(x,y):
    return x+y

z = (5,4)
print ( 'z=', add(*z) ) #sending a simplified tuple

#==========
header('Iterating Thru Tuples in a Dictionary')

# k1:3, k2:7 ... 
d = {"k1":3,"k2":7,"k3":8,"k4":9}

#one way
for t in d.items():
    print('A@tuple ', t, ' k=', t[0], ' v=', t[1])
    
#simplified way if just want to access K/V
for k,v in d.items():
    print('B k=', k, ' v=', v)
