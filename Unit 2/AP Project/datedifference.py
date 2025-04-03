
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def dayssince0(date):
    days = date[1]
    for y in range(1, date[2]): 
        if (y%4==0 and y%100!=0) or (y%400==0):
            days += 366 
        else:
            days += 365
    for m in range(1, date[0]):
        days += monthdays[m-1]
        if m == 2:
            days += 1
    return days

d1 = [4, 3, 2025]  
d2 = [12, 25, 2026]

diff = dayssince0(d2) - dayssince0(d1)
print(diff)
