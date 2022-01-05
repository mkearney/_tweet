
def api_request(endpoint: str, params:List=None)->str:
    args = []
    for arg, val in enumerate(params):
        args.append(f"{arg}={val}")
    args = "&".join(args)
    return f"{_base_url_}{endpoint}{args}"
