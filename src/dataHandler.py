import json

class dataHandler:
    def __init__(self):
        f = open("./data.json", "r", encoding='UTF-8')
        self.data = json.load(f)
        f.close()
    
    def addData(self, site, name):
        if name not in self.data[site]:
            self.data[site].append(name)
            f = open("./data.json", "w", encoding='UTF-8')
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            f.close()
            return 0
        else:
            return 1

    def getData(self):
        return self.data

    def removeData(self, site, name):
        if name in self.data[site]:
            self.data[site].remove(name)
            f = open("./data.json", "w", encoding='UTF-8')
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            f.close()
            return 0
        else:
            return 1