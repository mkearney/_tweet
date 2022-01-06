import requests

from .. import constants

def api_path(endpoint: str, params:dict=None)->str:
    args = []
    for arg, val in enumerate(params):
        args.append(f"{arg}={val}")
    args = "&".join(args)
    return f"{_base_url_}{endpoint}{args}"

def api_get(url:str, *)->response:
    return requests.get(
        api_path(url, *),
        headers=bearer_token()
    )

def api_post(url:str, *)->response:
    return requests.post(
        api_path(url, *),
        headers=bearer_token()
    )

def api_token(url:str, **kwargs)->response:
    return requests.post(api_path(url, *kwargs))
