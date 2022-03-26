import requests, sys, time, multiprocessing, argparse
from datetime import datetime

def request(url):
    try:
        agent = {
            "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko)"
        }
        rsp = requests.get(url)
        rsp = requests.get(url)
        if rsp.status_code != 404:
            print("[+] Status " + str(rsp.status_code) + ": " + url)
    except Exception as err:
        print(str(err))

def scan(usrl, word, ext):
    turl = url + word.rstrip()
    request(turl)
    if ext:
        request(turl + ext)
def main(args):
    start = datetime.now()
    print("===================================================")
    print("Started @ " + str(start))
    print("===================================================")
    if args.url.endswith("/") == False: args.url =+ "/"
    with open(args.worldlist) as file:
        for word in file:
            if word.startswith("#") == False:
                p = multiprocessing.Process(target=scan, args=(args.url , word , args.extension))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", action="store", help="starting url")
    parser.add_argument("wordlist", action="store", help="list of paths/files")
    parser.add_argument("-e", "--extension", action="store", help="file extension")

    if len(sys.argv[2:])==0:
        print(""":::       ::: :::::::::: :::::::::  :::::::::  :::::::::: :::::::::: ::::    ::: :::    ::: ::::    ::::  
:+:       :+: :+:        :+:    :+: :+:    :+: :+:        :+:        :+:+:   :+: :+:    :+: +:+:+: :+:+:+ 
+:+       +:+ +:+        +:+    +:+ +:+    +:+ +:+        +:+        :+:+:+  +:+ +:+    +:+ +:+ +:+:+ +:+ 
+#+  +:+  +#+ +#++:++#   +#++:++#+  +#+    +:+ :#::+::#   +#++:++#   +#+ +:+ +#+ +#+    +:+ +#+  +:+  +#+ 
+#+ +#+#+ +#+ +#+        +#+    +#+ +#+    +#+ +#+        +#+        +#+  +#+#+# +#+    +#+ +#+       +#+ 
 #+#+# #+#+#  #+#        #+#    #+# #+#    #+# #+#        #+#        #+#   #+#+# #+#    #+# #+#       #+# 
  ###   ###   ########## #########  #########  ###        ########## ###    ####  ########  ###       ### """)
    print("Web Server Directory and File Enumerator Tool Made By The3ye")
    print("Github: https://github.com/The3yeHTB")
    print("HackTheBox: https://app.hackthebox.com/users/716430")
    parser.print_help()
    parser.exit()

    args = parser.parse_args()
    main(args)
