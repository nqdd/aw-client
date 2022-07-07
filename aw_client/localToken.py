import os

class LocalToken:
    authFile = 'auth.tracker'

    def get(self) -> str:
        try:
            tokenFile = open(self.authFile, "r")
            token = tokenFile.read()
            tokenFile.close()
            return token
        except:
            return None
        
    def set(self, token) -> None:
        try:
            tokenFile = open(self.authFile, "w+")
            tokenFile.write(token)
            tokenFile.close()
        except:
            pass

    def delete(self) -> None:
        if os.path.exists(self.authFile):
            os.remove(self.authFile)
