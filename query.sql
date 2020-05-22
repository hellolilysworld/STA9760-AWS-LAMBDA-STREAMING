SELECT 
  name company,
  hour(cast(ts as timestamp)) hour, 
  max(high) max_high 
from 
  project3.mm_sta9730_project3
group by 
  1,2
order by 
  1,2;