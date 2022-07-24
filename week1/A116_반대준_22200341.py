def dayOfTheWeek(day,month,year) :
    def leapyear(n):
        return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)  
    sum = 0
    a = [31, 29 if leapyear(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    l = {0:"Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",4: "Thursday",5: "Friday",6: "Saturday"}
    
    for i in range(1971,year):
        sum+=366 if i%4==0 else 365
    for i in range(month-1):
        sum+=a[i]
    sum+=day
    return l[(sum + 4) % 7]


print(dayOfTheWeek(day = 31, month = 8, year = 2019))
print(dayOfTheWeek(day = 18, month = 7, year = 1999))
print(dayOfTheWeek(day = 15, month = 8, year = 1993))