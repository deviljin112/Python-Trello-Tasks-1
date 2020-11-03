import datetime

name = input("What's your name stranger?\n=> ").capitalize()
age = int(input("How old are you?\n=> "))
day, month = input("When is your birthday?\nFormat: DD MM\n=> ").split(" ")
day, month = int(day), int(month)

today = datetime.datetime.now()
user_year = today.year - age
birthday = datetime.datetime(user_year, month, day)
had_birthday = True

if today.month - month < 0:
    months_left = month - today.month
    had_birthday = False

days_left = today.day - day
if days_left < 0:
    days_left = days_left * -1

difference = today - birthday

hours_in_days = difference.days * 24
hours = (difference.seconds // 3600) + hours_in_days
minutes = (difference.seconds // 60) % 60
seconds = int(difference.seconds % 60)

print(
    f"""
OMG {name}!
You are {age},
So, you were born on {birthday.strftime("%d %b %Y")}.
You've been around for
{hours} hours,
{minutes} minutes,
{seconds} seconds.
"""
)

if not had_birthday:
    print(f"You have {days_left} days and {months_left} months until your birthday!")
else:
    print(f"You already had your birthday :(\nWell... Happy late Birthday!")