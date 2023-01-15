import datetime
import tkcalendar


def block_dates(calendar):
    with open('dates.txt', 'r') as file:
        for line in file.readlines():
            date_string = line.strip()
            date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            calendar.calevent_create(date, 'Unavailable', 'red')
            print(date)

if __name__ == '__main__':
    pass



