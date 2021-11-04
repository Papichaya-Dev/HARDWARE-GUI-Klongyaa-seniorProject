# Data
from data.mock.pill_channel_datas import pill_channel_datas

def initData(self) :
    self.pill_channel_datas = pill_channel_datas

class Store:
    def __init__(self) -> None:
        self.storeData = "init"
    
    def changeStoreData(self, text):
        self.storeData = text
    
    def printStoreData(self) :
        print(self.storeData)