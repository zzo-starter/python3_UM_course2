# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    A-while_loops.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/24 01:14:52 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 17:25:45 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')


#====================
header('WHILE LOOP')
def sumTo(aBound):
    theSum = 0
    aNumber = 1
    while aNumber <= aBound: #1234
        theSum += aNumber
        aNumber +=1
    return theSum 
print(sumTo(4))


#====================
header('WHILE LOOP')
count=0
even_nums = [] 
while count <= 15:
    if count % 2 == 0:
        even_nums.append(count)
    count +=1
print(even_nums)


 
#====================
header('FOR LOOP AS WHILE LOOP')
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
