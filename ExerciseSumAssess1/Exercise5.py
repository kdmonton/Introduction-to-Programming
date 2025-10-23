month_day = {
    'Jan': 31,
    'Feb': 28,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'Jun': 30,
    'Jul': 31,
    'Aug': 30,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31,
    }

month = input('Enter the month(e.g. Jan, Feb, Mar): ').capitalize()
if month in month_day:
    if month == 'Feb':
        leap = input('Is it a leap year? y/n: ').lower()
        if leap == 'y':
            print('Feb has 29 days')
        else:
            print('Feb has 28 days')
    else:        
        print(f'{month} has {month_day[month]} days')
else:
    print('Invalid month, please enter a proper abbreviation(e.g. Jan, Feb, Mar)')