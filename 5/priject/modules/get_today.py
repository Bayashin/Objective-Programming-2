import datetime

class Today:
    def get(self):
        return "{0:%d%m%ｙ}".format(datetime.datetime.now())