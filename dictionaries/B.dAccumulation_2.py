# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    B.dAccumulation_2.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/20 23:07:15 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/23 20:38:16 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')

 

header('B4 Dynamic Accumulator v3')
# count qty of every word in file dynamically
f = open('B.scarlet.txt','r')
txt = f.read()

d = {}
for word in txt.split():
    s = word.replace(',','')
    if s in d:
        d[s] += 1
    else:
        d[s] = 1


#sort
keys = list(d.keys())
keys.sort()
sorted = {i:d[i] for i in keys}

#display
print(sorted)


#find highest value
hv = 0
max_value = ''
for v in d:
    if d[v] > hv:
        max_value = v
        hv = d[v]

print('hv: @', max_value, ' hv:', hv ) 
