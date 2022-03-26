import re, requests, sys, argparse

class RegEx:
    def __init__(self, pattern, desc):
        self.pattern = pattern
        self.desc = desc

rgxEmail = RegEx(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", "Emails")
rgxPhone = RegEx(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", "Phone Numbers")
rgxIP = RegEx(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP Addresses")
rgxWord = RegEx(r"[a-zA-Z]+", "Words")

def scrapeURL(url, rgx):
    try:
        src = requests.get(url.strip())
        for rg in rgx:
            print("[*] Scraping " + rg.desc + "from " + url.strip())
            res = set(re.findall(rg.pattern, src.text, re.I))
            for dat in res:
                print(dat)
    except Exception as err:
        print(str(err))

def scrapeFile(fle, rgx):
    try:
        with open(fle) as fh:
            for url in fh:
                scrapeURL(url, rgx)
    except Exception as err:
        print(str(err))
def main(rgs):
    rgx = []
    isFile = True
    if args.input.lower().startswith("http"):
        isFile = False
    if args.scrape.lower() == "e":
        rgx = [rgxEmail]
    elif args.scrape.lower() == "p":
        rgx = [rgxPhone]
    elif args.scrape.lower() == "w":
        rgx = [rgxWord]
    elif args.scrape.lower() == "i":
        rgx = [rgxIP]
    elif args.scrape.lower() == "a":
        rgx = [rgxEmail, rgxPhone, rgxWord, rgxIP]

    if isFile:
        scrapeFile(args.input, rgx)
    else:
        scrapeURL(args.input, rgx)

    print(""":::::::::: ::::::::::: ::::    ::: ::::::::::: ::::::::  :::    ::: :::::::::: :::::::::  
:+:            :+:     :+:+:   :+:     :+:    :+:    :+: :+:    :+: :+:        :+:    :+: 
+:+            +:+     :+:+:+  +:+     +:+    +:+        +:+    +:+ +:+        +:+    +:+ 
:#::+::#       +#+     +#+ +:+ +#+     +#+    +#++:++#++ +#++:++#++ +#++:++#   +#+    +:+ 
+#+            +#+     +#+  +#+#+#     +#+           +#+ +#+    +#+ +#+        +#+    +#+ 
#+#            #+#     #+#   #+#+#     #+#    #+#    #+# #+#    #+# #+#        #+#    #+# 
###        ########### ###    #### ########### ########  ###    ### ########## #########  """)
if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("input", action="store", type=str, help="Desired URL or List of URLs contained in a file")
    parse.add_argument("scrape", action="store", type=str, nargs="?", default="a", help="\ne= Email, p = Phone, i = IPs, w = Words, a = All")

if len(sys.argv[2:]) == 0:
    print(""":::    ::: ::::::::::: :::::::::   ::::::::   ::::::::  :::::::::  
:+:    :+:     :+:     :+:    :+: :+:    :+: :+:    :+: :+:    :+: 
+:+    +:+     +:+     +:+    +:+ +:+        +:+        +:+    +:+ 
+#++:++#++     +#+     +#+    +:+ +#++:++#++ +#+        +#++:++#:  
+#+    +#+     +#+     +#+    +#+        +#+ +#+        +#+    +#+ 
#+#    #+#     #+#     #+#    #+# #+#    #+# #+#    #+# #+#    #+# 
###    ###     ###     #########   ########   ########  ###    ### """)
    print("HTML Data Scraper Made By The3ye")
    print("Github: https://github.com/The3yeHTB")
    print("HackTheBox: https://app.hackthebox.com/users/716430")
    parse.print_help()
    parse.exit()

args = parse.parse_args()
main(args)
