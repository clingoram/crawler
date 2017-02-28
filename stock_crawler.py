from yahoo_finance import Share                    
import datetime                  
from pprint import pprint 
                  
def getStock(id):                  
   stock=Share(str(id)+'.TW')                    
   info=stock.get_info()                     
   sum=stock.get_volume()                     
   open=stock.get_open()                     
   day_h=stock.get_days_high()                    
   day_l=stock.get_days_low()                    
   year_h=stock.get_year_high()                   
   yaer_l=stock.get_year_low() 
                    
   histor_data=stock.get_historical('2017-02-01', '2017-02-05')             
   return histor_data,day_h,day_l,yaer_l,year_h  
   
 pprint(getStock(2002)) #中鋼 
