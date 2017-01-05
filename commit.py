class Commit(object):

    __sha=None
    __message=None
    __html_url=None

    def __init__(self,sha,message,html_url):
        self.__sha = sha
        self.__message=message
        self.__html_url=html_url
        

    def Commit(self):
        return self
    def getSha(self):
        return self.__sha
    def setSha(self,sha):
        self.__sha=sha
    def getMessage(self):
        return self.__message
    def setMessage(self,message):
        self.__message=message
    def getHtml_url(self):
        return self.__html_url
    def setHtml_url(self,html_url):
        self.__html_url=url
    def __str__(self):
        return "URL: " + self.getHtml_url()  + "\nMessage: " + self.getMessage() + "\n\nSHA: " + self.getSha()