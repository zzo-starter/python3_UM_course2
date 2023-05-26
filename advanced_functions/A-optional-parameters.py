# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    A-optional-parameters.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 20:53:49 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 21:49:35 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('\n--- ',s)

def f(a, L=[]): #L is optional param
    debug("a:"+ str(a) +" L:"+''.join( map(str,L)))
    L.append(a)
    return L

# side-effect since no list was passed, yet appended and returned
debug("@A: "+ ''.join( map(str,f(1)))) #result = 1 in list
debug("@B: "+ ''.join( map(str,f(2)))) #result = 12 in list
debug("@C: "+ ''.join( map(str,f(3)))) #result = 123 in list ~ mutable "side-effect" 

# correctly adding to list
debug("@D: "+ ''.join( map(str,f(4,['hello'])))) 
debug("@E: "+ ''.join( map(str,f(5,['how are ya'])))) 
debug("@F: "+ ''.join( map(str,f(6,['wont you tell me your name?']))))  