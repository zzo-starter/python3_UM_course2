"""
- twitter data in project_twitter_data.csv ( text, retweets, replies)
- postitive_words.txt; negative_words.txt

2. You will create a csv file, which contains columns for the 
- Number of Retweets, 
- Number of Replies, 
- Positive Score (which is how many happy words are in the tweet), 
- Negative Score (which is how many angry words are in the tweet), 
- and the Net Score for each tweet.

3. At the end, you upload the csv file to Excel or Google Sheets
    3.1 and produce a graph of the Net Score vs Number of Retweets
    
"""

#removes characters considered punctuation from everywhere in the word
def strip_punctuation(s):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    ns = s
    for pc in punctuation_chars:
        ns = ns.replace(pc, '')
    return ns


#calculates how many words in the string are considered positive words.
def get_pos(s):
    global positive_words
    qty=0
    words_in_string = s.split() 
    for w in words_in_string:  
        if strip_punctuation(w).lower() in positive_words:
                qty +=1
    return qty

#calculates how many words in the string are considered negative words.
def get_neg(s):
    global negative_words
    qty=0
    words_in_string = s.split()
    for w in words_in_string:  
        if strip_punctuation(w).lower() in negative_words:
            qty +=1
    return qty


#=================== define positive  
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
print(positive_words)

#=================== define negative    
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
print(negative_words)

#unit test
sentence= 'what a truly Wonderful addict day it is today! #incredible'
print(sentence)
print ('pos: ', get_pos(sentence))
print ('neg: ', get_neg(sentence))

#==================== read tweet file 
f = open("project_twitter_data.csv","r")
fLines = f.readlines()[1:]  
outlines=[]
outlines.append("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
for l in fLines: 
    r = l.split(',')
    #print(r[0])
    #print(r[1])
    #print(r[2])
    pos = get_pos(r[0]) 
    neg = get_neg(r[0])
    net = pos - neg   
    res = r[1]+ ','+ r[2].replace('\n','')+','+ str(pos) + ',' + str(neg) + ',' + str(net) 
    outlines.append(res) 
     
##---- write to file 
f = open('resulting_data.csv','w')
f.write('')
f.close()
with open('resulting_data.csv', 'a') as f:
    for r in outlines:
        f.write( r + '\n')    
f.close()