class Movie:
    def __init__(self) -> None:
        #ตัวแปร Protected ขึ้นต้นด้วย _ 1 ครั้ง
        self._title = None #เตรียมตัวแปรไว้เพื่อใช้
        self._year = None
        self._genre = None

    #เมธอด Protected ขึ้นต้นด้วย _ 1 ครั้ง
    def _add_movie(self,title:str,year:int,genre:str):
        self._title = title
        self._year = year
        self._genre = genre

    def _getmovie_detail(self):
        print(f'Title : {self._title}')
        print(f'Year : {self._year}')
        print(f'Genre : {self._genre}')
#คลาส Movie,Documentary อยู่ไฟล์เดียวกันไม่ต้อง Import
class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self) #super().__init__() ถ้าเป็นชื่อคลาส Movie.__init__(self) ต้องใช้ (self)ถ้าใช้ super ไม่ต้อง
    
    def add_channel(self,ch:str): #ดูก่อนว่าอาจารย์ไกด์ไทป์มาให้ไหมถ้าไกด์ต้องไกด์เหมือนอาจารย์
        self.channel = ch
    
    def _getmovie_detail(self):
        #super()._getmovie_detail()
        Movie._getmovie_detail(self) 
        print(f'Channel: {self.channel}')

    #สร้าง public method เพื่อให้คลาสอื่นเรียกใช้ method
    def print_detail(self):
        self._getmovie_detail()       
#สร้าง object
if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie('My Octopus Teacher',2020,'Documentary')  
    m1.add_channel('Netflix')
    m1._getmovie_detail() #เรียกใช้ของ Documentary (Overriding me)
