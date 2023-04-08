#  Challenge-11
def count_dots(string):
    from collections import Counter
    return Counter(string)['.']

print(count_dots('d..o...ts')) # 5 

# Extra
def age_in_minutes():
    while True:
        yob = int(input("Enter year of birth (YearOfBirth > 1900): "))
        if yob>1900:
            break
    now = 2022 
    age = now - yob
    age_in_min = ((age)*365*24*60)+((age/4)*1)*1440  #(age*daysInYear*hoursInDay*minsInHour)+leap day count 
    return f"Your age in min: {age_in_min:,}"

print(age_in_minutes())# Your age in min: 48,388,320.0
