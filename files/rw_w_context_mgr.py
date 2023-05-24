
#H.1
with open("kaggle_etf_sampledata.txt","r") as md:
    #H.2 can exec any op; however 1x; not sequentially
    # md.read()
    #print('chars qty:', len(md.read()))
    # md.readlines()
    #print('lines qty: ', len(md.readlines()))
    # for line in x
    for line in md:
        print(line.strip())
#H.3 md.close() not necessary         
print ("finished.")