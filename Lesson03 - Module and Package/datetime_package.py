import datetime

def print_next_day():
    today=datetime.date.today()
    print(today)
    day=datetime.timedelta(days=1)
    tomorrow=today+day
    print(tomorrow)
    
print_next_day()
