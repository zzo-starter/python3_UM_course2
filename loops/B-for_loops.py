# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    B-for_loops.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/24 01:14:52 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 17:25:55 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')

 
#====================
header('FOR LOOP')
def sumTo(aBound):
    theSum = 0
    for i in range(aBound+1): #0123 +1 step 1
        theSum += i
    return theSum 
print(sumTo(4))

#====================
header('FOR LOOP')
def sumTo(aBound):
    theSum = 0
    for i in range(1, aBound+1): #123 +1 step 1
        theSum += i
    return theSum 
print(sumTo(4))

#====================
header('FOR LOOP')
def sumTo(aBound):
    theSum = 0
    for i in range(1, aBound+1, 2): #123 +1; step 2
        theSum += i
    return theSum 
print(sumTo(4))

#====================
header('FOR LOOP')
list1 = [8,3,4,5,6,7,9]
tot =0
for n in list1:
    tot += n
print('t1:', tot)

# as while loop
tot2 =0
i = 0
while i <= len(list1)-1:
    tot2+= list1[i]
    i +=1
print('t2:',tot2) 
