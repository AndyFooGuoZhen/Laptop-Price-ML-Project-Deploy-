import joblib
import numpy as np

model = joblib.load('XGB_model')



class backEnd:
    
    def __init__(self, inches, res, cpu, ram, weight, touchScreen, hdd, ssd, sshd, fstorage, laptopType, os):
        self.inches = inches
        self.res = res
        self.cpu = cpu
        self.ram = ram
        self.weight = weight
        self.touchScreen = touchScreen
        self.hdd = hdd
        self.ssd = ssd
        self.sshd = sshd
        self.fstorage = fstorage
        self.laptopType = laptopType
        self.os = os
        self.arrange()

    def arrange(self):
        finalList = [0] * 10
        
        finalList[0] = self.inches
        finalList[1] = self.res
        finalList[2] = self.cpu
        finalList[3] = self.ram
        finalList[4] = self.weight
        finalList[5] = self.touchScreen
        finalList[6] = self.hdd
        finalList[7] = self.ssd
        finalList[8] = self.sshd
        finalList[9] = self.fstorage

        typeList = [0] * 6
        typeList[self.laptopType] = 1

        oSList = [0] * 9
        oSList[self.os] = 1

        finalList.extend(typeList)
        finalList.extend(oSList)

        self.predict(finalList)

    def predict(self, list): #predict price of laptop given the above dataset

        arrToPredict = np.array([list])
        self.totalPredicted = model.predict(arrToPredict)
        
        

        
    


        


    
