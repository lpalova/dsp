# Hint:  use Google to find python function

####a) 
from datetime import datetime
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_start_object = datetime.strptime(date_start, '%m-%d-%Y')
date_stop_object = datetime.strptime(date_stop, '%m-%d-%Y')
diff = date_stop_object - date_start_object
diff.days

####b)  
from datetime import datetime  
date_start = '12312013'  
date_stop = '05282015' 
date_start_object = datetime.strptime(date_start, '%m%d%Y')    
date_stop_object = datetime.strptime(date_stop, '%m%d%Y')    
diff = date_stop_object - date_start_object    
diff.days 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
