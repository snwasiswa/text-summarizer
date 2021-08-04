""" The file analyses text from a given user"""
#######################################################################################
# Author : Steve Wasiswa
# The program returns a summary given an input as a string
# Basically, the program use extractive summarization approach by only conserving the
# important words within a text and returning them as summary
#######################################################################################

# Import important libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


class Summary:

    def __init__(self, text):
        """ Initialize necessary attributes of the class"""

        self.stop_words = set(stopwords.words("english"))
        self.text = text
        self.all_sentences = sent_tokenize(self.text)
        self.score_sentence = {}

    def tokenize_text(self):
        """ Splitting text into words"""

        words = word_tokenize(self.text)

        return words

    def score_word(self):
        """ Keeps track of the frequency of words in a text or sentence"""
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
        """ Computes a score of  every sentence, and then retuns the summary given an input as string"""

        # Computes the score of every sentence
        for sentence in self.all_sentences:
            for word, score in self.score_word().items():
                if word in sentence.lower():

                    if sentence in self.score_sentence:
                        self.score_sentence[sentence] += score

                    else:

                        self.score_sentence[sentence] = score

        value = 0

        # Compute a average score for every sentence
        for sentence in self.score_sentence:
            value += self.score_sentence[sentence]

        average_value = int(value / len(self.score_sentence))

        summary = ""
        # Add every necessary sentence to the long string after comparison
        for sentence in self.all_sentences:

            if (sentence in self.score_sentence) and (self.score_sentence[sentence] > (1.1 * average_value)):
                summary += sentence + " "

        return summary
