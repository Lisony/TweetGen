import configparser
import argparse
import time

from src.tweet_scraper import scrape_tweet_to_csv



if __name__ == "__main__":
    timerStart = time.time()

    parser = argparse.ArgumentParser(description="Markov chains tweet generator",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--config", default = "test", help = "Config set from ini.txt")
    args = vars(parser.parse_args())

    params = args["config"]

    config = configparser.ConfigParser()
    config.read("ini.txt")


    author = str(config[params]["twitter_nickname"])
    scrape_tweet_to_csv(author)


    print(f"---Script execution time: {time.time() - timerStart} seconds.---")