import datetime
current_date = datetime.date.today().strftime("%Y-%m-%d")
current_date = current_date.split("-")
b_date = input("Enter birthday in yyyy-mm-dd format: ")
name = input("Name of birthday legend? ")
b_date = b_date.split("-")
print(current_date, b_date)
if current_date[1] == b_date[1] and current_date[2] == b_date[2]:
    age = int(current_date[0]) - int(b_date[0])
    ordinal_suffix = {1: "st", 2: "nd", 3: "rd", 11: "th", 12: "th", 13: "th"}.get(
        age % 10 if not 10 < age <= 13 else age % 14, "th")
    print(f"It's {name}'s {age}{ordinal_suffix} Birthday")
else:
    print("Sorry, today is not your birthday")
