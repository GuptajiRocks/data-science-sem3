import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt_tab')

data = 'Jack was a lively boy who loved to stay active. During the day, he focused on his schoolwork, determined to excel in his studies. He enjoyed his time at school, where he could learn new things and challenge himself. However, all work and no play made Jack feel a bit dull. So, after school, he would rush outside to play with his friends.'

def sent_token():
    print(nltk.sent_tokenize(data))

def word_token():
    print(nltk.word_tokenize(data))


def freq7():
    word = nltk.word_tokenize(data)
    freq = FreqDist(word)
    print(freq.most_common(7))

freq7()


