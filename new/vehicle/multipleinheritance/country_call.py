from country import Country

#สร้าง object ของ country ประเทศไทย
c1 = Country ('Thailand' ,513120,66.93 )
c1.setcordinate(15.8700,100.9925)
c1.setcelsius(31)
c1.show_detail()

#สร้าง object ของ country ประเทศ Norway
c2 = Country ('Norway' ,385207,5.379 ) #Area: 385207 Population : 5.379 Million
c2.setcordinate(60.4720,8.4689) #Latitude : 60.472 #Longitud : 8.4689
c2.setcelsius(15)
c2.show_detail()


