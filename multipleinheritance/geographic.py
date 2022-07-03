#grographic.py
class Geographic:
    def setcordinate(self,lat,long): #lat คือรัติจูด
        self.latitude = lat
        self.longitud = long

    def getcordinate(self): #แสดงค่า latitude longitud
        return f'Latitude : {self.latitude}\nLongitud : {self.longitud}'
    
    def gettimezone(self):
        timezone = round(self.longitud/12 - 1) #เราใส่ round เพื่อให้ค่าที่ออกมาถูกปัดเศษตามจำนวนหลัก
        if timezone > 0:
            return f'TimeZone = +{timezone}' #timezone +7
        else:
            return f'TimeZone = {timezone}' #timezone -7

    def getclimate(self):
        if self.latitude <= -66.5 or self.latitude >= -66.5 :
            return 'Polar Zone' #ให้แสดง Polar Zone
        elif self.latitude <= -23.5 or self.latitude >= -23.5 :
            return 'Temperate Zone'
        else :
            return 'Tropical Zone'

