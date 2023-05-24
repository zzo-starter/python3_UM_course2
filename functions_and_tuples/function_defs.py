
#========= basic func
def hello(x):
    """hello this is an optional docstring comment
    2nd line of comment """
    global y # avoid global var refs
    
    print("hello!")
    y +=1
    return x


y=5    
x = hello(10)
print(x,' ', y)


#======== funcs calling other funcs "composition"
def square(x):
    return x*x 

def sum_of_squares(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
    
    return a+b+c

a = -5
b = 2 
c = 10

result = sum_of_squares(a,b,c)
print (result)
    

#=========== decompose = creating func placeholders (stubs) for funcs that dont yet exist 

# most_common_letter
# count_frequencies
# best_key 
    
def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d={}
    for c in st:
        if c in d:
            d[c] +=1
        else:
            d[c] = 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0] #convert ks into a real list
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far 

print(most_common_letter("aaabbbbbccssssssssssccdd"))        
    
    
#============= sample funcs

def pow(b,p):
    return b ** p

def square(x):
    a = pow( x, 2 )
    return a

n = 5
result = square( n )
print ('square of n @',5, ' is ', result)