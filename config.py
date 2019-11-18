import json, os, sys

def read():

    if(os.path.isfile("config.json")):
        config = open("config.json", "r")
        cfg = json.loads(config.read())
    else:
        from default_config import cfg_d
        _config = open("config.json", "w")
        _config.write(cfg_d) 
        _config.close()
        print("Created default config.json. Configure and then run again.")
        sys.exit()
        
    return cfg

def update(d):
    cfg = read()
    for key in d:
        cfg[key] = d[key]
    _config = open("config.json", "w")
    json.dump(cfg, _config) 
    _config.close()

if __name__ == "__main__":
    print(read())