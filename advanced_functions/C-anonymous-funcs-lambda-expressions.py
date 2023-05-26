# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    C-anonymous-funcs-lambda-expressions.py            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 22:00:56 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 22:07:55 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('\n--- ',s)
    
    
header('ANONYM FUNCS W LAMBDA EXPRESSIONS')
def add(x,y):
    return x+y

# FUNCTION AS A LAMBDA EXPRESSION
lamAdd = lambda x,y : x+y;


debug('@1 regular function res: 1+2 = ' + str(add(1,2)))

debug('@2 lambda w named function res: 1+2 = ' + str(lamAdd(1,2)))

debug('@3 lambda as anonymous function res: 1+2 = ' + str( (lambda x,y:x+y)(1,2)  ))
