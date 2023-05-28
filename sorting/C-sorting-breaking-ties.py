# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    C-sorting-breaking-ties.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 23:18:02 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/27 16:40:21 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('--- ',s)
    
    
    
header('BREAKING TIES')
# A 1 3
# A 2 3
# A 3 5

# A 1 1 1 
# A 2 2 4
# A 3 3 2
# A 3 3 3

tuples = [('A', 3, 2),('C', 3, 2),('B', 3, 2),('A', 3, 2),('C', 3, 2)]

for t in sorted(tuples):
    print(t)

 
 
header('REVERSE SORTING A STRING')
letters = "alwnfiwaksuezlaeiajsdl"
print(letters)  
d=[]
for ch in letters:
    d.append(ch)

sorted_letters = sorted(d , key = lambda d: d[0], reverse = True) 
print(sorted_letters)
