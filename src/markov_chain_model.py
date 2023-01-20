import pandas as pd
import markovify as mk
from itertools import chain
import spacy 


tweets_df = pd.read_csv("data/raw/AndrzejDuda_tweets.csv")


N = 4000
tweet_subset = tweets_df["content"][0:N]
print(len(tweet_subset))
text = "".join(chain.from_iterable(tweet_subset))


class POSifiedText(mk.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in text(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence



markov_model = mk.Text(text)



for i in range(5):
    print(markov_model.make_sentence())