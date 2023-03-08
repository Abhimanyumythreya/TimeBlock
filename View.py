from tkinter import Tk, ttk, messagebox, StringVar, IntVar, Grid



class View(Tk):
    def __init__(root):
        super().__init__()
        root.title('Time Block Planner')
        root.iconbitmap('letter-t.ico')
        root.minsize(1400, 1000)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.Styleing()
        
        root.mainframe = ttk.Frame(root, style='TFrame', padding=10)
        root.mainframe.grid(row=0, column=0, sticky='nwes')

        #Fixing 14 columns and 10 rows
        for i in range(14):
            if i<=9: root.mainframe.rowconfigure(i, weight=1)
            root.mainframe.columnconfigure(i, weight=1)

        root.greetingframe = GreetFrame(root.mainframe, 'Greeting.TFrame')

        root.detailframe = DetailFrame(root.mainframe, 'Detail.TFrame')
        
    def Styleing(root):
        s = ttk.Style()
        s.configure('TFrame', background='#B8E3DA')
        s.configure('Greeting.TFrame', background='black')
        s.configure('Detail.TFrame', background='black')

        s.configure('TLabel', background='#E6D9C8', font=('TkHeadingFont', 15))
        s.configure('Greeting.TLabel', font=('TkHeadingFont', 22))
        s.configure('Detail.TLabel', font=('TkHeadingFont', 30))

        s.configure('TCheckbutton', background='#E6D9C8', indicatorcolor='green', font=('TkHeadingFont', 20))

        s.configure('TSpinbox', padding=8)
        
        s.configure('TButton', font=('TKHeadingFont', 15))

    


    
class GreetFrame(ttk.Frame):    
    def __init__(frame, parent, style, borderwidth=20, relief='solid', padding=10):
        super().__init__(parent)      
        frame.configure({'style':style,
                         'borderwidth':borderwidth,
                         'relief':relief,
                         'padding':padding})
        frame.grid(row=0, column=0, rowspan=1, columnspan=14, sticky='nwes', padx=10, pady=10)
        frame.grid_propagate(0)

        #Fixing 14 columns with custom weights
        for i in range(14):
            if i in [0,7, 8, 13]: frame.columnconfigure(i, weight=2) #fist, last columns will double the size
            elif i in [1, 2, 3, 4, 5, 6, 9, 10, 11, 12]: frame.columnconfigure(i, weight=1)
        
        #Fixing 5 rows with custom weights
        for i in range(5):            
            if i in [1,2,3]: frame.rowconfigure(i, weight=1)
            else: frame.columnconfigure(i, weight=2)

        frame.greeting = StringVar()
        frame.GreetLabel = ttk.Label(frame, textvariable=frame.greeting, width=10,anchor='center', style='Greeting.TLabel')
        frame.GreetLabel.grid(row=1, column=1, rowspan=3, columnspan=6, sticky='nwes')

        frame.ShutDown = IntVar()
        frame.ShutDown.set(1)
        frame.ShutDownButton = ttk.Checkbutton(frame, text='Shutdown', onvalue=0, offvalue=1, variable=frame.ShutDown, command=frame.SHUTDOWN)
        frame.ShutDownButton.grid(row=2, column=9, rowspan=1, columnspan=4, sticky='nes')    
           
    def SHUTDOWN(frame):
        if messagebox.askyesno(
                title= 'SHUTDOWN ?',
                message='This will record as deviation if the blocks are not complete yet.\nAre you sure to ShutDown?'): 
            frame.ShutDown.set(0)
        else:
            frame.ShutDown.set(1)
    
class DetailFrame(ttk.Frame):
    def __init__(frame, parent, style, borderwidth=20, relief='solid', padding=10):
        super().__init__(parent)
        frame.configure({'style': style,
                         'borderwidth': borderwidth,
                         'relief': relief,
                         'padding': padding})
        frame.grid(row=1, column=0, rowspan=9, columnspan=8, sticky='nwes', padx=10, pady=10)
        frame.grid_propagate(0)

        #Fixing 8 columns and 9 rows
        for i in range(9):
            if i <= 7: frame.columnconfigure(i, weight=1)
            frame.rowconfigure(i, weight=1)
            

        frame.detaillabel = ttk.Label(frame, text='Details', anchor='center', style='Detail.TLabel')
        frame.detaillabel.grid(row=0, column=0, rowspan=1, columnspan=8, sticky='nwe')

        frame.Date = IntVar()
        frame.Date.set(3)
        frame.today = ttk.Checkbutton(frame, text='Today', width=8, onvalue=0, offvalue=1, variable=frame.Date, command=frame.Send_Date)
        frame.tom = ttk.Checkbutton(frame, text='Tomorrow', width=8, onvalue=1, offvalue=0, variable=frame.Date, command=frame.Send_Date)

        frame.today.grid(row=1, column=1, rowspan=1, columnspan=2, sticky='nwe')
        frame.tom.grid(row=1, column=5, rowspan=1, columnspan=2, sticky='nwe')

        frame.Startlabel = ttk.Label(frame, text='Start At ', anchor='w')
        frame.Startlabel.grid(row=2, column=1, rowspan=1, columnspan=2, sticky='swe')
        frame.Endlabel = ttk.Label(frame, text='Finish At', anchor='e')
        frame.Endlabel.grid(row=5, column=5, rowspan=1, columnspan=2, sticky='nwe')

        frame.Start_Hour, frame.Start_Minute = IntVar(), IntVar()
        frame.Starthourbox = ttk.Spinbox(frame, width=4, from_=0, to=23,
                                         textvariable=frame.Start_Hour, wrap=True, justify='center', command=frame.Send_STime)
        
        frame.Startminbox = ttk.Spinbox(
            frame, width=4, from_=0, to=59, textvariable=frame.Start_Minute, wrap=True, justify='center', command=frame.Send_STime)
        frame.Starthourbox.grid(row=3,column=1, rowspan=1, columnspan=1, sticky='nwe')
        frame.Startminbox.grid( row=3, column=2, rowspan=1, columnspan=1, sticky='new')

        frame.End_Hour, frame.End_Minute = IntVar(), IntVar()
        frame.Endhourbox = ttk.Spinbox(frame, width=4, from_=0, to=23,textvariable=frame.End_Hour, wrap=True,justify='center', command=frame.Send_ETime)
        frame.Endminbox = ttk.Spinbox(frame, width=4, from_=0, to=59,textvariable=frame.End_Minute, wrap=True,justify='center', command=frame.Send_ETime)
        frame.Endhourbox.grid(row=4, column=5, rowspan=1, columnspan=1, sticky='wes')
        frame.Endminbox.grid(row=4, column=6, rowspan=1, columnspan=1, sticky='wes')


        frame.SaveButton = ttk.Button(frame, text='Save/Schedule', command=frame.SAVE)
        frame.SaveButton.grid(row=6,column=2, columnspan=4)

    def Set_Cntrl(frame, control): frame.control = control
    def Send_Date(frame): 
        if frame.control: frame.control.Set_Date()

    def Send_STime(frame):        
        if frame.control:
            frame.control.Show_StartTime()
            frame.control.Set_StartTime()

    def Send_ETime(frame):
        if frame.control:
            frame.control.Show_EndTime()
            frame.control.Set_EndTime()

    def SAVE(frame):
        if messagebox.askyesno(
                title='DateTime Setting',
                message='Are you sure to save these timings and schedule further?'):
            if frame.control: frame.control.Set_Schedule()
        
            
        



if __name__=='__main__': pass
    
    
