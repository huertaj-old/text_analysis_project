
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use based on external source
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
#function to strip punctuation from source material
def strip_punctuation(string):
    for chars in string:
        if chars in punctuation_chars:
            string=string.replace(chars, '')
    return string
#count number of positive words based on list
def get_pos(string):
    counter=0
    string=string.split()
    for words in string:
        words=words.lower()
        words=strip_punctuation(words)
        if words in positive_words:
            counter+=1
    return counter
#count number of negative words based on list
def get_neg(string):
    counter=0
    string=string.split()
    for words in string:
        words=words.lower()
        words=strip_punctuation(words)
        if words in negative_words:
            counter+=1
    return counter
#opening and processing provided twitter data
file=open('project_twitter_data.csv', '')
linecounter=0
resulting_header='Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n'
f = open("resulting_data.csv", "w")
f.write(str(resulting_header))
for lines in file:
    linecounter+=1
    tuples=lines.split(',')
    #print(tuples)
    striptweet=strip_punctuation(tuples[0])
    retweets=tuples[1]
    #print(retweets)
    replies=tuples[2].rstrip()
    #print(replies)
    #print(striptweet)
    pos_score=get_pos(striptweet)
    #print('pos=',pos_score)
    neg_score=get_neg(striptweet)
    #print('neg=',neg_score)
    net=pos_score-neg_score
    currentline=[]
    if linecounter >1:
        f.write(retweets)
        f.write(', ')
        f.write(replies)
        f.write(', ')
        f.write(pos_score)
        f.write(', ')
        f.write(neg_score)
        f.write(', ')
        f.write(net)
        f.write('\n')
f.close()