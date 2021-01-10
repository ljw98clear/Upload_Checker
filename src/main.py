import dataHandler
import toon

d = dataHandler.getData()
toonInst = []

for site, names in d.items():
    for name in names:
        toonInst.append(toon.toon(site,name))

for a in toonInst:
    print(a.checkUpload())