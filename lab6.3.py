from datetime import date

date1 = (14, 1, 2025)
date2 = (16, 2, 2025)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

days_difference = abs((d2 - d1).days)

print(f"Number of days between {date1} and {date2}: {days_difference} days")
