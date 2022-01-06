from auth import bearer_auth
from constants import __base_url__, __tweets_search_recent__

import requests
import pandas as pd

def process_tweets(data):
    df = pd.DataFrame(data["data"])
    df = df.drop(columns=["public_metrics"]).set_index("id")
    public_metrics = pd.DataFrame(
        [row["public_metrics"] for row in data["data"]],
        index = df.index
    )
    users_renames = {
        "id": "author_id",
        "created_at": "author_created_at",
    }
    users = pd.DataFrame(data["includes"]["users"])
    users = users.rename(columns=users_renames).set_index("author_id")
    df = df.join(public_metrics).reset_index()
    df = df.set_index("author_id").join(users).reset_index()
    tweets_ordered_cols = [
        "created_at",
        "username",
        "text",
        "verified",
        "name",
        "location",
        "author_created_at",
        "author_id",
        "source",
        "retweet_count",
        "reply_count",
        "like_count",
        "quote_count",
    ]
    return df.set_index("id").loc[:,tweets_ordered_cols]

def search_tweets(query, max_results:int=100, parse=True)->pd.DataFrame:
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "id,created_at,author_id,text,public_metrics,source",
        "expansions": "author_id",
        "user.fields": "created_at,id,location,name,username,verified"
    }
    r = requests.get(
        url = f"{__base_url__}{__tweets_search_recent__}",
        params = params,
        headers = bearer_auth()
    )
    if parse:
        r = process_tweets(r.json())
    return r

#r = search_tweets("twitter #rstats -is:retweet")
#r
