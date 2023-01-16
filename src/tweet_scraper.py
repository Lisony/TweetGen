import pandas as pd
import snscrape.modules.twitter as sntwitter
from tqdm import tqdm
from os.path import exists


def scrape_tweet_to_csv(author, n = 5000, path = "data/raw/"):
    file_path = path + author
    if exists(f"{file_path}_tweet.csv"):
        print(f"Scrapping tweets from {author}\n")

        scraper = sntwitter.TwitterSearchScraper(f"from:{author}")
        
        tweets = []
        for i, tweet in enumerate(scraper.get_items()):
            if i > 20000:
                break
            
            if tweet.rawContent.startswith("@"):
                continue
            
            if len(tweets) >= n:
                break
            
            tweets.append([tweet.user.username, tweet.rawContent])
        
        tweets_df = pd.DataFrame(tweets, columns=["author", "content"])
        
        tweets_df.to_csv(path + f"{author}_tweets.csv", index=False)
    else:
        print("Tweets already scrapped!\n")
    
    

if __name__ == "__main__":
    # Authors
    authors = ["jordanbpeterson", "elonmusk", "AndrzejDuda", "Cobratate", "TateTheTalisman"]
    file_path = "data/raw/"
    
    for author in tqdm(authors):
        scrape_tweet_to_csv(author, 5000, file_path)
    
    
    
    
