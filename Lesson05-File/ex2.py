import  csv
minAqi=88
minPlace='a'
try:
    with open('AQI.csv','r',encoding='utf8') as f:
        next(f)
        reader=csv.reader(f)
        for row in reader:
            try:
                if int(row[2])<minAqi:
                    minAqi=int(row[2])
                    minPlace=row[0]
            except ValueError:
                continue   

except FileExistsError:
    print("File does not exist!")
except FileNotFoundError:
    print("File does not found!")

print("{} 空氣最好，AQI 是 {}".format(minPlace,minAqi))
