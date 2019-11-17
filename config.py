import json, os, sys

def read():

    if(os.path.isfile("config.json")):
        config = open("config.json", "r")
        cfg = json.loads(config.read())
    else:
        from default_config import cfg_d
        _config = open("config.json", "w")
        json.dump(cfg_d, _config) 
        _config.close()
        print("Created default config.json. Configure and then run again.")
        sys.exit()
        
    return cfg

def update(keys, values):
    cfg = read()
    for i in range(keys.lenght):
        cfg[keys[i]] = values[i]
    _config = open("config.json", "w")
    json.dump(cfg, _config) 
    _config.close()