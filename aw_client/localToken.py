import os
import logging
import aw_core

# FIXME: This line is probably badly placed
logging.getLogger("requests").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

class LocalToken:
    authFile = os.path.join(aw_core.dirs.get_cache_dir("auth"), 'auth.tracker')

    def get(self) -> str:
        try:
            tokenFile = open(self.authFile, "r")
            token = tokenFile.read()
            tokenFile.close()
            return token
        except:
            logger.error('cannot open auth.tracker')
            return None
        
    def set(self, token) -> None:
        try:
            tokenFile = open(self.authFile, "w+")
            tokenFile.write(token)
            tokenFile.close()
        except Exception as e:
            logger.error(f'cannot write to auth.tracker: {e}')
            pass

    def delete(self) -> None:
        if os.path.exists(self.authFile):
            os.remove(self.authFile)
