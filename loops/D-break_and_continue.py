# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D-break_and_continue.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 17:27:03 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 19:29:39 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')

x = 0 
while x<= 10:
    x +=1
    if x == 3:
        break #finish
    print('x:',x)
print('finished.')
    

x = 0 
while x<= 10:
    x +=1     
    if x == 3:
        continue #go back to top; skip; continue 
    print('x:',x)
print('finished.')