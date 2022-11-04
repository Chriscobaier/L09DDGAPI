import requests


def test_ddg0(query):


    url_ddg = "https://api.duckduckgo.com"
    resp = requests.get(url_ddg + f"/?q={query}&format=json&pretty=1&nohtml=1")
    rsp_data = resp.json()
    #print(rsp_data)
    goodData = rsp_data["RelatedTopics"]
    return goodData
    #for i in goodData:
        #print(i["FirstURL"])

