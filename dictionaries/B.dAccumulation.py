# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    B.dAccumulation.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/20 23:07:15 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/23 20:38:24 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')


header('B1 Static Accumulator')
# count number of times character is in file
f = open('B.scarlet.txt','r')
txt = f.read()
t_count = 0 
s_count = 0
for c in txt:
    if c == 's':
        s_count += 1
    if c == 't':
        t_count += 1
        
print('s was found '+ str(s_count) + ' instances.')
print('t was found '+ str(t_count) + ' instances.')
# ... 

header('B2 Dynamic Accumulator v1')
# count every character in file from predefined set 
f = open('B.scarlet.txt','r')
txt = f.read()
d ={}
d['s']= 0 
d['t']= 0 
for c in txt:
    if c == 's':
        d['s'] += 1
    elif c == 't':
        d['t'] += 1
        
print('s was found '+ str(d['s']) + ' instances.')
print('t was found '+ str(d['t']) + ' instances.')


header('B3 Dynamic Accumulator v2')
# count every character in file from predefined set v2
f = open('B.scarlet.txt','r')
txt = f.read()
d ={'s':0, 't':0}
s = {'s','t'}
for c in txt:
    if c in s:
        d[c] += 1
        
print('s was found '+ str(d['s']) + ' instances.')
print('t was found '+ str(d['t']) + ' instances.')

header('B4 Dynamic Accumulator v3')
# count qty of every character in file dynamically
f = open('B.scarlet.txt','r')
txt = f.read()

d = {}
for c in txt:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
        
print('a was found '+ str(d['a']) + ' instances.')
print('s was found '+ str(d['s']) + ' instances.')
print('t was found '+ str(d['t']) + ' instances.')
# ... 