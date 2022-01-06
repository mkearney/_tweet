import os
import base64

from constants import __base_url__, __oauth2_token__

# I. Create encoded keystring
#     1. URL encode keys
#     2. Concatenate encoded consumer key, colon, and encoded consumer secret.
#     3. Base64 encode string from previous step.
# II. Obtain bearer token
#     1. Make POST request to POST request to oauth2/token
#         a. Authorization: Basic <encoded_keystring>
#         b. Content-Type: application/x-www-form-urlencoded;charset=UTF-8
#         c. grant_type=client_credentials
#     2. Parse reaponse JSON
# III. Create bearer authorization header
#     1. Use "access_token" to create header
#         a. Authorization: Basic <access_token>


def bearer_auth()->dict:
    bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
    if not bearer_token:
        consumer_key = base64.b64encode(
            os.environ.get("TWITTER_CONSUMER_KEY")
        )
        consumer_secret = base64.b64encode(
             os.environ.get("TWITTER_CONSUMER_SECRET")
        )
        headers = {
             "Authorization": f"Basic {consumer_key}:{consumer_secret}",
             "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        body = {"grant_type": "client_credentials"}
        r = requests.post(
            f"{__base_url__}{__oauth2_token__}",
            headers=headers,
            json=body
        )
        bearer_token = r.json["access_token"]
        os.environ["TWITTER_BEARER_TOKEN"] = bearer_token

    # return as dict to be used in headers
    return {"Authorization": f"Bearer {bearer_token}"}
