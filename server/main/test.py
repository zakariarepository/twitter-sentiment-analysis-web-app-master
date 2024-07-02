import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime


query = "(bike) until:2023-01-01 since:2013-01-01"
tweets = []
limit = 50


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    

    if len(tweets) == limit:
        break
    else:
        timestamp = int(tweet.date) / 1000  # Convert milliseconds to seconds
        dt = datetime.datetime.fromtimestamp(timestamp)

        # Format the datetime object as a string
        formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
        tweets.append([tweet.rawContent, tweet.url, tweet.likeCount, formatted_date])
        
df = pd.DataFrame(tweets, columns=['Content','lien','likes','date'])
print(df.Content.str.encode("utf-8"))
df.to_csv('file_name.csv', index=False)
df.to_json('data.json',orient='records')