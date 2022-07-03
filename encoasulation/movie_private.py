class Movie:
    def __init__(self) -> None:
        #ตัวแปร private ขึ้นต้นด้วย underscore 2 ครั้ง
        self.__title = None
        self.__year = None
        self.__genre = None
        self.__rating = 5
    
    #เมธอด protected ขึ้นต้นด้วย underscore 1 ครั้ง
    def _add_movie(self,title:str,year:int,genre:str,rating=5):
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__rating = rating

    #เมธอด private ขึ้นต้นด้วย underscore 2 ครั้ง
    def __getmovie_detail(self):
        print(f'Title: {self.__title}')
        print(f'Year: {self.__year}')
        print(f'Genre: {self.__genre}')
        print(f'Rating: {self.__rating}')

    #สร้าง public method เพื่อให้ class อื่นๆ ได้เรียกใช้ private method
    def print_detail(self):
        self.__getmovie_detail()

class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)
    
    def add_channel(self,ch:str):
        self.channel = ch
    
    def print_detail(self):
        super().print_detail()
        print(f'Channel: {self.channel}')

if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie('My Octopus Teacher',2020,'Documentary')
    m1.add_channel('NetFlix')
    #m1.__getmovie_detail()   #error 
    #เรียก private method ผ่านทาง super class
    #obj._className__privateMethod()
    #m1._Movie__getmovie_detail() 
    m1.print_detail()