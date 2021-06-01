month_len = [29, 31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30 ,31]

dow = ['M', 'T', 'W', 'Th', 'F', 'Sat', 'Sun']
sundays = 0

for year in range(1900, 2001):

    if year % 4 == 0 and year != 1900:
        month_len[0], month_len[2] = month_len[2], month_len[0]
    
    for month in range(1, 13):
        for day in range(1, month_len[month]+1):
            dow.append(dow.pop(0))
            if dow[0] == 'Sun' and day == 1 and year > 1900:
                sundays += 1

    month_len[0] = 29
    month_len[2] = 28

print(sundays)