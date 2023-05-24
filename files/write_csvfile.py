


#------- J.1
olympians = [
    ("JJ Abrams", 31, "Cross Country Skiing"),
    ("Minnesota Alto", 30, "Sailing"),
    ("Waco Abe", 31, "Cross Country Skiing")    
]

outfile = open("sample_output3.csv","w")
header_row = 'Name,Age,Sport'
outfile.write(header_row + '\n')
#print(header_row)

for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2] )
    outfile.write(row_string)
    outfile.write('\n')
    #print(row_string)
outfile.close()
