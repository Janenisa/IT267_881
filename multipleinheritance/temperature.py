#temperature.py
class Temperature:
    def setcelsius(self,temp):
        self.celsius = temp
    
    def getfahrenheit(self):
        return (self.celsius * 1.8 + 32)

    def getweather(self):
        if self.celsius  <= 0 : #ค่าน้อยกว่าเท่ากับ 0
            return 'Freezing' #ให้แสดง freezing
        elif self.celsius  <= 18 :
            return 'Cold'
        elif self.celsius  <= 28 :
            return 'Warm'    
        else :
            return 'Hot'