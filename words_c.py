
most_words_searched = 10


def checking_the_word(word):
    """
    Clean word using defined rules
    :param word:
    :return:
    """
    # find regex for word1
    return word.lower().strip(',').strip('.').strip('\'').strip('"').strip('*').strip('?').strip('!').strip(';').\
        strip(':')


class words_counter(object):
    """Word counting object, counts total words and top 10 occurring words"""

    def __init__(self, file_path):
        self.top_words = list()
        self.total_words = 0
        self.file_path = file_path
        self.word_freq = dict()
        self.counting_words()

    def counting_words(self):
        with open(self.file_path, 'r') as f:
            for word in f.read().split():
                word = checking_the_word(word)
                self.word_freq.setdefault(word, 0)
                self.word_freq[word] += 1
                self.total_words += 1
                self.insert_to_top(word)

    def insert_to_top(self, word):
        if self.top_words:
            for index, item in enumerate(self.top_words):
                if self.word_freq[item] <= self.word_freq[word]:
                    if word in self.top_words:
                        del self.top_words[self.top_words.index(word)]
                    self.top_words.insert(index, word)
                    del self.top_words[most_words_searched:]
                    break
                elif len(self.top_words) < most_words_searched and word not in self.top_words:
                    # Case where top 10 not full and word not in top 10 already
                    self.top_words.append(word)
        else:
            self.top_words.append(word)

    def disp_top_words(self):
        for word in self.top_words:
            print(word, self.word_freq[word])

# possible main function here
