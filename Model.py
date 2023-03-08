from datetime import datetime, date, time, timedelta
from csv import DictWriter, DictReader, writer, reader
import os


class Model:
    Users = []
    Running = False
    Shutdown = False
    today = datetime.now()
    Headers = ['Date Created', 'Date', 'Starting Time', 'Ending Time', 'Tasks', 'Ideas', 'Metrics', 'Deviations']

    def __init__(self, user):
        self.user = user
        self.Date = self.set_Date()
        self.StartTime = None
        self.EndTime = None    

    def set_Date(self, Date_View=True):
        if Date_View: return Model.today.date()
        return Model.today.date() + timedelta(1)
    
    def min_StartTime(self):
        if self.Date == Model.today.date():
            plus_1 = (Model.today + timedelta(minutes=60)).time()
            min_start_time = time(plus_1.hour, plus_1.minute)
            return min_start_time
        return time(0, 0)

    

    def set_Time(self, hour, minute):        
        t = time(hour, minute)
        return t       

    def SAVE(self): 
        Model.Running = True
        if not os.path.exists(f'{self.user}\'s Statistics.csv'):
            with open(f'{self.user}\'s Statistics.csv', 'a') as Stat:
                writer = DictWriter(Stat, fieldnames=Model.Headers, restval=None)
                writer.writeheader()
            
        with open(f'{self.user}\'s Statistics.csv', 'a') as Stat:
            writer = DictWriter(Stat, fieldnames=Model.Headers, restval=None)
            writer.writerow({
                'Date Created':date.today(),
                'Date': self.Date,
                'Starting Time': self.StartTime,
                'Ending Time': self.EndTime
            })
            
                    
    def UPDATE(self): pass
    def DESTROY(self): pass


    


if __name__=='__main__': 
    bharath = Model('Bharath')
    bharath.SAVE()
    print(bharath.today.date())