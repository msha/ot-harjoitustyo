class Fileops:

    def savefile(self,name,content):
        with open(name, "w",encoding="utf-8") as file:
            file.write(content)
