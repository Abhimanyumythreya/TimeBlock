from datetime import datetime, time, timedelta

def get_time(): return int(input('Hours: ')), int(input('Minutes: '))

def check_clash(T1, T2):
    while T1 and T1>T2:
        T2 = time(*get_time())
    return T2

class Metrics:
    'Metrics are behaviours with quantifiable values.'
    
    def __init__(self):
        '''
        Creates an empty dictionary.
        Keys and values will be of 'String' datatype and primitive datatypes respectively.
        '''
        self.metrics = {}

    def add_metric(self, **kw):
        '''
        Adds a new metric to the dictionary of metrics.
        Multiple metrics could be added at once.
        '''
        self.metrics.update(**kw)
    
    def update_metric(self, metric, value):
        '''
        Updates the first positional arguement with the second positional
        arguemnt.
        '''
        self.metrics[metric] = value

    def delete_metric(self, metric):
        '''
        Deletes the metric from the dictionary of metrics.
        '''
        del self.metrics[metric]

    def __str__(self):
        '''
        this method is implemented for the reference only. Will be removed in future.
        '''
        return f'{self.metrics}'

class Work:
    'A list of tasks or ideas or obligations for the day.'

    def __init__(self):
        '''
        Creates an empty list.
        '''
        self.works = []

    def add_work(self, *works):
        '''
        Adds work/s to the list of daily tasks or obligations.
        '''
        [self.works.append(work) for work in works]

    def update_work(self, old, new):
        '''
        Amends an old work with the new.
        '''
        index = self.works.index(old)
        self.works[index] = new

    def delete_work(self, work):
        '''
        Deletes a certain work.
        '''
        self.works.remove(work)

    def __str__(self):
        return f'{self.works}'

class Block:
    '''
    A dedicated period for a task.
    Class Variables:
        end -> time object
        all_blocks -> list object
    '''
    end = None
    all_blocks = []
    
    def __init__(self, task=[]):
        '''
        Creates a block object with:
            starting time -> time object
                (Checks if clashing withe previous block)
            ending time -> time object
        Updates the class variables.
        '''
        self.start = check_clash(Block.end, time(*get_time()))
        self.end = time(*get_time())
        self.task = task
        Block.end = self.end
        Block.all_blocks.append([self.start, self.end])

    def __str__(self):
        string = ''
        for i, block in enumerate(Block.all_blocks):
            string += f'Block {i+1}:\n  Starts At: {block[0]}\n  Ends At: {block[1]}\n'
        return string

class Sheet:
    '''
    A Daily sheet traks the work done in time and attention available for the day.
    Class Variable:
        shutdown -> bool value

    '''
    shutdown = False
    def __init__(self, Metrics=Metrics(), Tasks=Work(), Ideas=Work(), Blocks=Block()):
        '''
        Creates a daily-sheet with:
            Date -> datetime object: date of the day. (automatically generated.)
            Metrics -> Metris object: an empty dictionary
            Tasks -> Work object: an empty list
            Ideas -> work object: an empty list.
            Blocks -> Block object: collection of starting and ending times.
        '''
        self.Date = datetime.today()
        self.metrics = Metrics
        self.tasks = Tasks
        self.ideas = Ideas
        self.blocks = Blocks

    def add_block(self):
        Block()

