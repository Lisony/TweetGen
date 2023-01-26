import pandas as pd
import markovify as mk
from itertools import chain
import spacy


class model:
    def __init__(self, author, sentence_len = 300, n_tweets = 50):
        N = 4000
        self.author = author
        self.n_tweets = n_tweets

        text = self.data_parser(author, N)
        self.tweets = self.generate_tweets(text , n_tweets, sentence_len)

    def save_to_csv(self):
        gen_tweets_df = pd.DataFrame([self.author]*self.n_tweets, columns=['author'])
        gen_tweets_df["gen_content"] = self.tweets
        gen_tweets_df.to_csv("results/" + f"{self.author}_tweets_gen.csv", index=False)
    @staticmethod
    def data_parser(author, N):
        tweets_df = pd.read_csv(f"data/raw/{author}_tweets.csv")

        tweet_subset = tweets_df["content"][0 : N]
        text = "".join(chain.from_iterable(tweet_subset))


        return text

    @staticmethod
    def generate_tweets(text, num_tweets, sentence_len):
        markov_model = mk.Text(text, state_size=3)

        return [markov_model.make_short_sentence(sentence_len) for _ in range(num_tweets)]

 
    

    
            
# class POSifiedText(mk.Text):
#     def word_split(self, sentence):
#         return ["::".join((word.orth_, word.pos_)) for word in text(sentence)]

#     def word_join(self, words):
#         sentence = " ".join(word.split("::")[0] for word in words)
#         return sentence



# TO DO VALIDATE GENERETED TWEETS
# MAYBE JACCARD SIMILARITY?






# make a model, generate tweets and save to csv




