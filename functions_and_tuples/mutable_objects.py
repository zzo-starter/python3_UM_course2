# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mutable_objects.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/24 00:12:17 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/24 00:14:51 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')


#============
header('pass in list and update')
def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    # no return; yet list is updated (side-effect) pass by ref
    # can also delete items
    
mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)

print(mylst) #['Michigan', 'Wolverines', 'are', 'awesome']


# vars passed by val; lists and dicts passed by ref (side-effect)
def changeit(x):
    x= x + 100
    
y = 10
changeit(y)
print('y:', y)

#============
header('pass in list and set')
def myfun(lst):
    lst = [1, 2, 3]
    # list was not replaced

mylist = ['a', 'b']
myfun(mylist)
print(mylist)