import sys
from calendar import Calendar

RED_COLOR_SYMBOL = '\033[91m'
BOLD_SYMBOL = '\033[1m'
END_COLOR_SYMBOL = '\033[0m'


class Month(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def display(self):
        calendar = Calendar(0)
        dates_iterator = calendar.itermonthdates(self.year, self.month)
        sys.stdout.write('\n')
        for i, day_date in enumerate(dates_iterator):
            if day_date.month != self.month:
                sys.stdout.write('\t')
                continue
            DayList(day_date, i).display()
        sys.stdout.write('\n')

class DayList(object):

    def __init__(self, date, number):
        self.date = date
        self.number = number

    def is_last_day_of_week(self):
        return (self.number + 1) % 7 == 0

    def template(self):
        if self.is_last_day_of_week():
            return '{}\n'
        return '{}\t'

    def display(self):
        template = self.template()
        date_to_print = template.format(self.date.day)
        if self.date.isoweekday() in (6, 7):
            sys.stdout.write('{}{}{}'.format(
                RED_COLOR_SYMBOL, date_to_print, END_COLOR_SYMBOL
            ))
        else:
            sys.stdout.write(date_to_print)

class CalendarList(object):

    def print_calendar(self):
        year = self.year()
        month = self.month_number()
        Month(year, month).display()

    def year(self):
        year = input('Enter year number\n>')
        return int(year)

    def month_number(self):
        month = int(input('Enter month number\n> '))
        if month not in range(1,12):
            print('Incorrect month_number, month must be for 1-12.')
        return month

def main():
    calendar = CalendarList()
    calendar.print_calendar()

if __name__ == '__main__':
    main()