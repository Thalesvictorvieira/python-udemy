from datetime import datetime

fmt ='%d/%m/%y'
data = datetime.strptime('2024-07-27','%Y-%m-%d')
print(data.strftime(fmt))
print(data.year)