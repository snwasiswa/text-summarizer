""" The file analyses text from a given user"""

#Import important libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

class Summary:

    def __init__(self, text):

        self.stop_words = set(stopwords.words("english"))
        self.text = text
        self.all_sentences = sent_tokenize(self.text)
        self.score_sentence = {}


    # Function that removes stop words
    def tokenize_text(self):

        words = word_tokenize(self.text)

        return words

    # Function that keeps track of the frequency of words in a text or sentence
    def score_word(self):
        # Create an empty dictionary
        freq_words = {}
        for word in self.tokenize_text():
            # Get every in word in lower case
            word = word.lower()
            if word in self.stop_words:
                continue
            if word in freq_words:
                freq_words[word] += 1
            else:
                freq_words[word] = 1

        return freq_words

    def get_summary(self):

        for sentence in self.all_sentences:
             for word, score in self.score_word().items():
                 if word in sentence.lower():

                     if sentence in self.score_sentence:
                         self.score_sentence[sentence] += score

                     else:

                         self.score_sentence[sentence] = score



        value = 0
        for sentence in self.score_sentence:
            value += self.score_sentence[sentence]

        average_value = int(value / len(self.score_sentence))

        summary = ""
        for sentence in self.all_sentences:

            if (sentence in self.score_sentence) and (self.score_sentence[sentence] > (1.1 * average_value)):
                summary += " " + sentence

        print(summary)


def main():

    with open('testfile.txt', 'r') as file:
        data = file.read()
        summarize = Summary(data)

    summarize.get_summary()

if __name__ == "__main__":

    main()





