import snscrape.modules.twitter as sntwitter

def fetch_latest_tweets(query, max_tweets=10):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append(tweet.content)
    return tweets

if __name__ == "__main__":
    query = "memecoin news"
    tweets = fetch_latest_tweets(query)
    for tweet in tweets:
        print(tweet)