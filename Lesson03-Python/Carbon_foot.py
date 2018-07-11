bus=0.03
car=0.24
scooter=0.06

def carbon_foot(rate):
    return lambda km:rate*km

way=carbon_foot(car)
print(way(100))
