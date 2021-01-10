import json

f = open("./data.json", "r", encoding='UTF-8')
data = json.load(f)
f.close()
    
def addData(site, name):
    if name not in data[site]:
        data[site].append(name)
        f = open("./data.json", "w", encoding='UTF-8')
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()
        return 0
    else:
        return 1

def getData():
    return data

def removeData(site, name):
    if name in data[site]:
        data[site].remove(name)
        f = open("./data.json", "w", encoding='UTF-8')
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()
        return 0
    else:
        return 1