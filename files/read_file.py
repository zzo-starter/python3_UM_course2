
#------------------- A
#A.1
print("opening file")
file = open("kaggle_etf_sampledata.txt", "r")
print("...file open ok...\n")

# A.2 get entire contents into a string var
# only want to do this when wanting to parse; ETL
# but not large files
fContent = file.read()
print(fContent)

# A.3 print first 100 characters
print (fContent[:100])
file.close()
print("closed file.\n")  

#------------------- B

file = open("kaggle_etf_sampledata.txt", "r")
# B.1 read n lines instead of entire file at once
# returns a list of strings
fLines = file.readlines()
  
# B.2 
print(fLines[:3])
file.close() 
print("closed file.")

#print each line; however line ends in \n
for l in fLines[:3]:
    print(l)
print()

# B.3 strip any white space, and new line chars
for l in fLines[:3]:
    print(l.strip())    
print()
#------------------- C

#simplified if wanting to read all lines; will not work with slices
print('simplified')
file = open("kaggle_etf_sampledata.txt","r")
for l in file:
    print(l.strip())
file.close()

#------------------- D
file = open("kaggle_etf_sampledata.txt","r")
fLines = file.readlines()
print ("# of lines in file: ", len(fLines))
file.close()

#---------------------- E
file = open("kaggle_etf_sampledata.txt","r")
fChars = file.read()
print("# of chars in file: ", len(fChars))
file.close()