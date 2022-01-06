import requests

from constants import __base_url__

def api_path(endpoint: str, params:dict=None)->str:
    args = []
    for arg, val in enumerate(params):
        args.append(f"{arg}={val}")
    args = "&".join(args)
    return f"{__base_url__}{endpoint}{args}"

def api_get(url:str, *)->response:
    return requests.get(
        api_path(url, *),
        headers=bearer_auth()
    )

def api_post(url:str, **kwargs)->response:
    return requests.post(
        api_path(url, *kwargs),
        headers=bearer_auth()
    )
