import json
import urllib.request


#url = "http://www.tuling123.com/openapi/api"
#info = input('\n我: ')
def chat_module(info):
    req = {
            "key":"18127c8722a64ce18101182b1696163b",
            "info":info 
            }
    #req = {
    #        "key":"46bebf7e173d48b5a943e0d5dc57c440",
    #        "info":info 
    #        }

    req = json.dumps(req).encode('utf8')
    #print (req)
    http_post = urllib.request.Request( "http://www.tuling123.com/openapi/api", data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    #print(response_str)
    response_dic = json.loads(response_str)
    #print(response_dic)
    if 'url' in response_dic.keys():
        ans = response_dic['text'] + '\n链接: ' +  response_dic['url']
    else:
        ans = response_dic['text']
    return(ans)


if __name__ == '__main__':
    ans = chat_module('大连的酒店')
    print (ans)
