class Fileops:

    def savefile(self,name,content):
        file = open(name, 'w')
        file.write(content)
        file.close()