# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    listener_loops.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 15:31:48 by zoozdev777        #+#    #+#              #
#    Updated: 2023/05/25 17:13:33 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def header(s):
    print('\n=========', s.upper(), '============')
    
    
header('LISTENER LOOP 1')
theSum=0
x=-1
while (x != 0):
    x = int(input("enter next number to add; enter 0 to stop"))
    theSum += x
print('sum: ', theSum)

header('LISTENER LOOP 2')
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no')
    return answer

response = get_yes_or_no('Do you like lima beans? Y-es or N-o: ')
if response == 'Y':
    print('Great! they are very healthy.')
else:
    print('Too bad. Quite tasty.')