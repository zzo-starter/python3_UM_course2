
#------------ I.1 Query/Filter by parsing CSV data 
file = open("kaggle_etf_sampledata.csv","r")
fLines = file.readlines()
for line in fLines:
    print(line.strip())

print("-------")
header = fLines[0]

field_names = header.strip().split(',')
print(field_names)

for row in fLines[1:]:
    vals = row.strip().split(",")
    if vals[5] != '712':
        print("{}:{}:{}:{}:{}:{}".format(vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))

file.close()