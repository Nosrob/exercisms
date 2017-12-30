import datetime

def meetup_day(year, month, day_of_the_week, which):
    index = {"1st":0, "2nd":1, "3rd":2, "4th":3, "5th": 4, "last": -1}
    calendar = { 'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}

    d = datetime.date(year, month, 1)
    while d.month == month:
        calendar[d.strftime('%A')].append(d.day)
        d += datetime.timedelta(days=1)

    if which == "teenth":
        return datetime.date(year,month,[x for x in calendar[day_of_the_week] if 12 < x < 20][0])

    return datetime.date(year,month,calendar[day_of_the_week][index[which]])
