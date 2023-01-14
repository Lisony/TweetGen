import pandas as pd
import markovify as mk
from itertools import chain


tweets_df = pd.read_csv("data/raw/jordanbpeterson_tweets.csv")



N = 1000
tweet_subset = tweets_df["content"][0:N]
text = "".join(chain.from_iterable(tweet_subset))
markov_model = mk.Text(text)


for i in range(5):
    print(markov_model.make_sentence())