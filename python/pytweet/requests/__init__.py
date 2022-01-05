import requests

def api_path(endpoint: str, params:dict=None)->str:
    args = []
    for arg, val in enumerate(params):
        args.append(f"{arg}={val}")
    args = "&".join(args)
    return f"{_base_url_}{endpoint}{args}"

def api_get(url:str, *):
    return requests.get(
        api_path(url, *),
        headers=bearer_token()
    )

def api_post(url:str, *):
    return requests.post(
        api_path(url, *),
        headers=bearer_token()
    )
