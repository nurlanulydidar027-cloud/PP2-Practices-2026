from datetime import datetime, date, timedelta

# 1. Get current date and time
now = datetime.now()
print(now)              # 2026-02-19 10:30:00
print(now.year)         # 2026
print(now.month)        # 2
print(now.day)          # 19

# 2. Create a specific date
birthday = date(2000, 5, 15)
print(birthday)         # 2000-05-15

# 3. Difference between two dates
today = date.today()
birthday = date(2000, 5, 15)
diff = today - birthday
print(diff.days)        # number of days since birthday

# 4. Add days to a date
today = date.today()
future = today + timedelta(days=30)
print(future)           # date 30 days from now

# 5. Format date as string
now = datetime.now()
print(now.strftime("%d-%m-%Y"))   # 19-02-2026
print(now.strftime("%H:%M:%S"))   # 10:30:00