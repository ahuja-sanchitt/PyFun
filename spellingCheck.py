''''
This is a spelling correcter using the textblob library, however the accuracy is 70%
'''

from textblob import TextBlob

def correct(sentence):
    incorrect_words=sentence.split(' ')
    correct_words=[]

    for x in incorrect_words:
        correct_words.append(str(TextBlob(x).correct()))

    correct_sentence=' '.join(correct_words)
    print("Corrected sentence %s" %(correct_sentence))


if __name__ == "__main__":
    x = input("Enter your sentence: ")
    correct(x)       

