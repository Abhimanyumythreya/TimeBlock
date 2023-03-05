from datetime import datetime, date, time, timedelta
from csv import DictWriter, DictReader
import os


class Model():
    Users = []
    FieldNames = ['Date_Created', 'Date', 'Starting Time', 'Ending Time', 'Tasks', 'Metrics', 'Ideas', 'Deviations']

    def __init__(self, Running=False, Date_view=0, user='Bharath'):
        self.Running = Running
        self.Date = self.GET_DATE(Date_view)
        self.StartingTime = self.GET_START(self.Date)
        self.EndingTime = GET_END(self.StartingTime)
        self.user = user
        if self.user not in Model.Users:
            Model.Users.append(self.user)
            self.file_name = f'{self.user}\'s Statistics.csv'

    def GET_DATE(self, Date_View):
        if Date_View == 0:return datetime.now().date() + timedelta(1)
        return datetime.now().date()

    def get_time(moment): return int(input(f'{moment} Hour: ')), int(input(f'{moment} Minute: '))

    def GET_START(self):
        t_now = datetime.now()
        today = date.today()
        if self.Date == today:
            print(f'You can choose from {(t_now + timedelta(minutes=60)).time()}')
            t_start = time(*Model.get_time('Starting'))
            if datetime.combine(today, t_start) - t_now >= timedelta(minutes=60):
                pass
            else:
                return self.GET_START(self)
        else:
            print('You can choose to schedule from midnight')
            t_start = time(*Model.get_time('Starting'))
        return t_start

    def SaveData(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'x') as Stats:
                #print('Creating a database for {}'.format(self.user))
                writer = DictWriter(Stats, fieldnames=Model.FieldNames, restval=None, )
                writer.writeheader()
        with open(self.file_name, 'a') as Stats:
            writer = DictWriter(Stats, fieldnames=Model.FieldNames)
            writer.writerow({
                'Date_Created': datetime.today().date(),
                'Date': self.Date,
                'Starting Time': self.StartingTime,
                'Ending Time': self.EndingTime
            })
        self.Running = True


    def UpadteData(self):
        pass


    def DeleteData(self): pass



if __name__=='__main__': pass