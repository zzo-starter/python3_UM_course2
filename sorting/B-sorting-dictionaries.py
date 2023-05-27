# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    B-sorting-dics-breaking-ties.py                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 23:18:02 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/27 15:18:08 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('--- ',s)
    
    
    
header('SORT A DICT by KEYS')

d={'E':1,'F':3,'B':5,'A':7,'C':4,'I':2,'D':3,'E':5}
debug('original: '+''.join(d))
debug('sort yet keep original order; then iterate:')
for x in sorted(d.keys()):
    print("{} appears {} times".format(x,d[x]))
    
header('SORT A DICT BY VALS')    
debug('sort yet keep original order; then iterate:')
for x in sorted(d.keys(), key = lambda x:d[x] ):
    print("{} appears {} times".format(x,d[x]))
    

header('SORT A DICT BY VALS')    
debug('sort yet keep original order; then iterate:')
for x in sorted(d, key = lambda x:d[x], reverse= True): # simplified keys default accessor and reversed 
    print("{} appears {} times".format(x,d[x]))
    