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

        #self.words = words

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

        #score_sentence = {}

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

        return summary


def main():

    sum = Summary("There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar.")

    print(sum.get_summary())

if __name__ == "__main__":

    main()





