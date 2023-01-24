import pandas as pd
import markovify as mk
from itertools import chain
import spacy


def generate_tweets(N):
    return [markov_model.make_short_sentence(300) for _ in range(N)]
    
            
class POSifiedText(mk.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in text(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence



# TO DO VALIDATE GENERETED TWEETS
# MAYBE JACCARD SIMILARITY?




tweets_df = pd.read_csv("data/raw/krzysztofbosak_tweets.csv")
file_path= "results/"
N = 4000
tweet_subset = tweets_df["content"][0:N]
tweet_author = tweets_df.iloc[0].author
text = "".join(chain.from_iterable(tweet_subset))


# make a model, generate tweets and save to csv
num_tweets = 50
markov_model = mk.Text(text, state_size=3)
gen_tweets_df = pd.DataFrame([tweet_author]*num_tweets, columns=["author"])
gen_tweets = generate_tweets(num_tweets)
gen_tweets_df["gen_content"] = gen_tweets
gen_tweets_df.to_csv(file_path + f"{tweet_author}_tweets_gen.csv", index=False)



