# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    A-sorting-basics.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 22:43:51 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 23:03:40 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('--- ',s)
    
#======================    
header('SORT')
l = [1,6,3,8,5,9,44,22]
l.sort()  #simply sort 
debug('sort: '+ ''.join(map(str,l)))

#======================    
header('SORTED')
l = [1,6,3,8,5,9,44,22]
sortedList = sorted(l) #sort and return sorted 
debug('sorted: '+ ''.join(map(str,sortedList)))


#======================    
header('SORTED IN REVERSE ORDER')
l = [1,6,3,8,5,9,44,22]
sortedList = sorted(l, reverse= True) #sort and return sorted 
debug('sorted in reverse: '+ ''.join(map(str,sortedList)))

#======================    
header('SORTED IN REVERSE ORDER WITH KEY PARAMETER')
def absoluteFunc(x):
    if x < 0:
        return -x
    else:
        return x

l = [-2,1,7,3,8,-6,5,9,44,22]
sortedList = sorted(l, reverse= True, key= absoluteFunc) #sort and return sorted 
debug('sorted in reverse w key param: '+ ''.join(map(str,sortedList)))