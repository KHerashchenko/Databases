select year, max(engball100) highest_grade
from zno_results
where engteststatus = 'Зараховано'
group by year