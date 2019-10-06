import json, os, sys

def ini():

    #Load Config
    os.system("cls" if os.name == "nt" else "clear")
    if(os.path.isfile("config.json")):
        config = open("config.json", "r")
        cfg = json.loads(config.read())
    else:
        from config import cfg_d
        _config = open("config.json", "w")
        _config.write(cfg_d)
        _config.close()
        print("Created default config.json. Configure and then run again.")
        sys.exit()

    #Config Variables
    global debug; debug = True
    global name; name = cfg['username']
    global userid; userid = cfg['userid']
    #etc...