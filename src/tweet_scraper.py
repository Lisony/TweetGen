import pandas as pd
import snscrape.modules.twitter as sntwitter
from tqdm import tqdm
from os.path import exists
import re


def scrape_tweet_to_csv(author, n = 5000, path = "data/raw/"):
    file_path = path + author
    print(file_path)
    if exists(f"{file_path}_tweets.csv"):
        print("Tweets already scrapped!\n")
    else:
        print(f"Scrapping tweets from {author}...\n")

        scraper = sntwitter.TwitterSearchScraper(f"from:{author}")
        
        tweets = []
        limit = 20000
        for i, tweet in enumerate(scraper.get_items()):
            author = tweet.user.username
            tweet_text = tweet.rawContent
            
        
            if i%1000:
                print(f"Progress:{(i/limit)*100}%")
            if i > 20000:
                break
            
            if tweet_text.startswith("@"):
                continue
            
            if len(tweets) >= n:
                break
            
            # if tweet contains link do not include it 
            if not re.search("https://", tweet_text):
                tweets.append([author, tweet_text])
                
            if not re.search("http://", tweet_text):
                tweets.append([author, tweet_text])
        
        tweets_df = pd.DataFrame(tweets, columns=["author", "content"])
        
        tweets_df.to_csv(path + f"{author}_tweets.csv", index=False)
        
 