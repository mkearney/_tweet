# base URL
__scheme__ = "https"
__domain__ = "api.twitter.com"
__version__ = "/2"
__base_url__ = f"{__scheme__}://{__domain__}{__version__}/"

__oauth2_token__ = "oauth2/token"
__tweets_search_recent__ = "tweets/search/recent"
__tweets_lookup__ = "tweets/lookup"
__tweets_fields__ = (
    "attachments,author_id,context_annotations,conversation_id,"
    "created_at,entities,geo,id,in_reply_to_user_id,lang,"
    "organic_metrics,possibly_sensitive,"
    "promoted_metrics,public_metrics,referenced_tweets,"
    "reply_settings,source,text,withheld"
)
