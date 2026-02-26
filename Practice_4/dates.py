from datetime import datetime, timedelta

# 1. Subtract five days from current date
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("5 days ago:", five_days_ago.strftime("%Y-%m-%d"))


# 2. Print yesterday, today, tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:    ", today.strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))


# 3. Drop microseconds from datetime
now_with_microseconds = datetime.now()
now_without_microseconds = now_with_microseconds.replace(microsecond=0)
print("With microseconds:   ", now_with_microseconds)
print("Without microseconds:", now_without_microseconds)


# 4. Calculate two date difference in seconds
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
difference = date2 - date1
print("Difference in seconds:", difference.total_seconds())