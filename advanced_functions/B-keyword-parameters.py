# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    B-keyword-parameters.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 21:51:20 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 21:58:17 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('\n--- ',s)
    
header('KEYWORD PARAMETERS')
initial =7    
def f(x,y=3, z= initial):
    print("x, y, z are "+ str(x), str(y), str(z))
    
f(2) # output # 2, 3, 7
f(2,4) # output # 2, 4, 7
#f(2, ,8) runtime error
# ~ can invoke via param
f(2, z=8) #~ 2,3,8
f(x=1, z=3, y=2) #in any order ~ 1,2,3
