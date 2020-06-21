""" The file analyses text from a given user"""

#Import important libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


class Summary:

    def __init__(self, text):

        self.stop_words = set(stopwords.words("english"))
        self.text = text
        #self.words = words

    # Function that removes stop words
    def tokenize_text(self):

        self.words = word_tokenize(self.text)

    # Function that keeps track of the frequency of words in a text or sentence
    def frequency(self):
        # Create an empty dictionary
        freq_words = {}
        for word in self.tokenize_text():
            # Get every in word in lower case
            word = word.lower()
            if word in freq_words:
                freq_words[word] = freq_words[word] + 1
            if word in self.stop_words:
                continue
            else:
                freq_words[word] = 1

        return freq_words

    def score(self):

        all_sentences = sent_tokenize(self.text)
        score_sentence = {}

        for sentence in all_sentences:
             for word, freq in freq.items():
                 if word in sentence.lower():

                     if sentence in sentenceValue:
                         sentenceValue[sentence] += freq
                     else:
                         sentenceValue[sentence] = freq

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        average = int(sumValues / len(sentenceValue))

    def get_summary(self):

        print(self.frequency)

def main():

    sum = Summary("People like to talk about people. Even though you don't like me, I will still like you")
    sum.get_summary()


if __name__ == "__main__":

    main()





