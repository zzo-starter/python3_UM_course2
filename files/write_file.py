
#--------------- G
file = open("sample_output.txt","w")

for number in range(13):
    square = number * number
    #print('@', number, '=', square)
    #G.1
    file.write( str(square)+ '\n') #G.2

file.close()


#--------------- 
filename = "sample_output2.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n") #G.2
outfile.close()

infile = open(filename, "r")
# read 10 first characters from the file
print(infile.read()[:10])
infile.close()

