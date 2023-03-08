'''
Controller is a mediator between Model and View.
Any data from Model to View (or Vice-Versa) goes through Controller.
'''
from datetime import datetime, date, time, timedelta

class Control:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.Show_Greet_Message()
        self.Show_StartTime()
        
    def Show_Greet_Message(self):
        message = self.model.today
        message = message.strftime('%A, %d %b. %Y   %I:%M %p')
        self.view.greetingframe.greeting.set(message)

    def Set_Date(self):
        if self.view.detailframe.Date.get()==0:
            self.model.Date = self.model.set_Date(Date_View=True)            
        else: 
            self.model.Date = self.model.set_Date(Date_View=False)
            
        

    def Show_StartTime(self):
        Minimum = self.model.min_StartTime()
        hour, minute = Minimum.hour, Minimum.minute
        self.view.detailframe.Starthourbox['from_'] = hour
        if self.view.detailframe.Start_Hour.get() == hour:
            self.view.detailframe.Startminbox['from_'] = minute
            if self.view.detailframe.Start_Minute.get() < minute:
                self.view.detailframe.Start_Minute.set(minute)
        else:
            self.view.detailframe.Startminbox['from_'] = 0
        

        
    def Set_StartTime(self):
        hour = self.view.detailframe.Start_Hour.get()
        minute = self.view.detailframe.Start_Minute.get()
        if hour and minute:
            self.model.StartTime = self.model.set_Time(hour, minute)
            print(self.model.StartTime)
            

    def Show_EndTime(self):
        Minimum = self.model.StartTime
        hour, minute = Minimum.hour, Minimum.minute 
        self.view.detailframe.Endhourbox['from_'] = hour
        if self.view.detailframe.End_Hour.get() == hour:
            self.view.detailframe.Endminbox['from_'] = minute
            if self.view.detailframe.End_Minute.get() < minute:
                self.view.detailframe.End_Minute.set(minute)
        else:
            self.view.detailframe.Endminbox['from_'] = 0

    def Set_EndTime(self):
        hour = self.view.detailframe.End_Hour.get()
        minute = self.view.detailframe.End_Minute.get()
        if hour and minute:
            self.model.EndTime = self.model.set_Time(hour, minute)
            print(self.model.EndTime)

    def Set_Schedule(self):
        self.model.SAVE()