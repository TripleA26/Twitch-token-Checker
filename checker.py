import requests, threading, random
from colorama import Fore, init
init(convert=True)
def check(token):
    try:
        proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
        token = token.replace("\n", "")
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES',
            'Authorization': f'OAuth {token}',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.twitch.tv',
            'Referer': 'https://www.twitch.tv/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        data = '[{"operationName":"PersonalSections","variables":{"input":{"sectionInputs":["RECS_FOLLOWED_SECTION","RECOMMENDED_SECTION"],"recommendationContext":{"platform":"web","clientApp":"twilight","location":"settings","referrerDomain":"www.twitch.tv","viewportHeight":937,"viewportWidth":1008,"channelName":null,"categoryName":null,"lastChannelName":"531c","lastCategoryName":"fifa 22","pageviewContent":null,"pageviewContentType":null,"pageviewLocation":"settings","pageviewMedium":null,"previousPageviewContent":"twitch_logo","previousPageviewContentType":null,"previousPageviewLocation":"home","previousPageviewMedium":"twitch_topnav"}},"creatorAnniversariesExperimentEnabled":false},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f8cc9b91bb629f2d09dd8299d9f07c4daefe019236a19fc12fa2b14eb95c359e"}}},{"operationName":"ProfileImageSetting","variables":{},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3d814a91606062a51f71e90c9b5a2d6e86792f52dacd912967d458067b5db44d"}}},{"operationName":"UserEmoticonPrefix_Query","variables":{},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"6eb368f3a785c358509cc0da9ff56ac76d535e255196d496dd7312487d3abbe1"}}},{"operationName":"UsernameRenameStatus","variables":{},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"caed6a3d336fc50251da7b944462ea321d7f276ee6fcccdf7e2e3de4d6ab5204"}}}]'

        response = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'})
        try:
            data = response.json()[0]['data']
            print(f"{Fore.LIGHTGREEN_EX}VALID: {token}")
            with open('valid.txt', "a+") as f:
                f.write(f"{token}\n")
        except:
            print(f"{Fore.LIGHTRED_EX} INVALID: {token}{Fore.RESET}")
    except:
        pass
with open("tokens.txt") as file:
    for token in file.readlines():
        threading.Thread(target=check, args=(token,)).start()