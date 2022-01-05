import os
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")

# I. Create encoded keystring
#     1. URL encode keys
#     2. Concatenate encoded consumer key, colon, and encoded consumer secret.
#     3. Base64 encode string from previous step.
# II. Obtain bearer token
#     1. Make POST request to POST request to oauth2/token
#         a. Authorization: Basic <encoded_keystring>
#         b. Content-Type: application/x-www-form-urlencoded;charset=UTF-8.
#         c. grant_type=client_credentials
#     2. Parse reaponse JSON
# III. Create bearer authorization header
#     1. Use "access_token" to create header
#         a. Authorization: Basic <access_token>
