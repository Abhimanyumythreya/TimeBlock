'''
Writes to, and reads from database (initially, a csv file).
More of a commandline application, which will be interacted by a Controller.
'''
from datetime import datetime, date, time, timedelta
ShutDown = False
Start = None
End = None
DTobj = datetime.now()

def get_date():
    if input('Is it for today or tomorrow? '):
        global DTobj
        DTobj += timedelta(1)
    return DTobj.date()

def get_time(moment):
    return int(input(f'{moment} Hour: ')), int(input(f'{moment} minute: '))

def get_start():
    global Start
    Start = time(*get_time('Starting'))
    '''
    code to get the logical starting time goes here!
    '''
    return Start

def get_end():
    global End
    End = time(*get_time('Ending'))
    '''
    code to get the logical ending time goes here!
    '''
    return End


class Metrics:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, **kw):
        self.metrics.update(**kw)

    def update_metric(self, metric, value):
        self.metrics[metric] = value

    def del_metric(self, metric):
        del self.metrics[metric]

    def __str__(self):
        return f'{self.metrics}'

class Work:
    def __init__(self):
        self.works = []

    def add_work(self, *works):
        [self.works.append(work) for work in works]

    def update_work(self, old, new):
        i = self.works.index(old) 
        self.works[i] = new

    def del_work(self, work):
        self.works.remove(work)

    def __str__(self):
        return f'{self.works}'

class Block:
    all_blocks = []
    def __init__(self, task=[]):
        self.start = time(*get_time('Starting'))
        self.end = time(*get_time('Ending'))
        self.task = task
        Block.all_blocks.append(
            {'start': self.start,
             'end': self.end,
             'task': self.task   
            }
        )



