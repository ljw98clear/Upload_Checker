import manatoki

class toon:
    def __init__(self, site, name):
        if site == "마나토끼":
            self.site = manatoki.manatoki(name)
        elif site =="애니24":
            #self.site = ohli24.ohli24(name)
            self.site = None
            pass

    def checkUpload(self):
        if self.site != None:
            retval = self.site.routine()
            return retval

    def __del__(self):
        if self.site != None:
            self.site.quit()
            print("객체 제거함")