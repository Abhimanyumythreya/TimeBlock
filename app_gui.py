from tkinter import *
from tkinter import ttk, messagebox
#from PIL import Image as I, ImageTk
#Instead convert images into .ico and use iconbitmap method!
global RUNNING
RUNNING = False

def SHUTDOWN():pass
def UPDATION(): pass
def GET_DEVIATIONS(): pass
def GET_STATISTICS(): pass
def SETTINGS(): pass
def TIPS(): pass

def STYLE():
    s = ttk.Style()
    s.configure('TFrame', background='#DFEBEB')
    s.configure('white.TFrame', background='white')
    s.configure('dateframe.TFrame', background='#BDB74D')
    s.configure('metricframe.TFrame', background='#288499')
    s.configure('taskframe.TFrame', background='#465994')
    s.configure('ideaframe.TFrame', background='#624694')
    s.configure('blockframe.TFrame', background='#F2BC8D')
    s.configure('TLabel', background='green')
    s.configure('TCheckbutton', background='blue')


def BEGIN_DAILY(root):
    if messagebox.askyesno(title='Datetime Confirmation', message='Sure to save the date, time and schedule?'):
        root.title('Daily Sheet')
        mainframe_1 = ttk.Frame(root, padding=5)
        dateframe = ttk.Frame(mainframe_1, style='dateframe.TFrame')
        metricframe = ttk.Frame(mainframe_1, style='metricframe.TFrame')
        taskframe = ttk.Frame(mainframe_1, style='taskframe.TFrame')
        ideaframe = ttk.Frame(mainframe_1, style='ideaframe.TFrame')
        blockframe = ttk.Frame(mainframe_1, style='blockframe.TFrame')

        mainframe_1.grid(row=0, column=0, sticky='nwes')
        dateframe.grid(row=0, column=0, columnspan=14,
                       rowspan=1, sticky='nwes')
        metricframe.grid(row=1, column=0, columnspan=14,
                         rowspan=4, sticky='nwes')
        taskframe.grid(row=5, column=0, columnspan=4,
                       rowspan=10, sticky='nwes')
        ideaframe.grid(row=5, column=4, columnspan=3,
                       rowspan=10, sticky='nwes')
        blockframe.grid(row=5, column=7, columnspan=7,
                        rowspan=10, sticky='nwes')
        for i in range(14):
            mainframe_1.grid_columnconfigure(i, weight=1)

        for i in range(15):
            mainframe_1.grid_rowconfigure(i, weight=1)

        for widget in mainframe_1.winfo_children():
            widget.grid_configure(padx=5, pady=5)
            widget.configure(borderwidth=20, relief=SOLID)
            widget.grid_propagate(0)
    else:
        ...

def App():
    root = Tk()
    root.title('TimeBlock')
    root.iconbitmap('letter-t.ico')
    root.grid_columnconfigure(0, weight=1, minsize=1400)
    root.grid_rowconfigure(0, weight=1, minsize=1000)

    global Greet
    Greet = StringVar()

    global Shutdown
    Shutdown = StringVar()

    global Date
    Date = StringVar()

    global START_HOUR
    START_HOUR = StringVar()

    global START_MINUTE
    START_MINUTE = StringVar()

    global END_HOUR
    END_HOUR = StringVar()

    global END_MINUTE
    END_MINUTE = StringVar()

    STYLE()
    
    mainframe_1 = ttk.Frame(root, padding=5)
    mainframe_1.grid(row=0, column=0, sticky='nwes')
    

    greetframe = ttk.Frame(mainframe_1, style='dateFrame.TFrame')
    greetframe.grid(row=0, column=0, rowspan=2, columnspan=14)

        
    greet = ttk.Label(greetframe, textvariable=Greet)
    greet.grid(row=1, column=1, rowspan=2, columnspan=4, sticky='nwes')

    
    shutdown = ttk.Checkbutton(greetframe, text='ShutDown', 
                                variable=Shutdown, onvalue='1',
                                offvalue='', command=SHUTDOWN)
    shutdown.grid(row=1, column=6, columnspan=3, rowspan=2, sticky='nwes')

    detailframe = ttk.Frame(mainframe_1, style='white.TFrame')
    detailframe.grid(row=2, column=0, rowspan=8, columnspan=9)
    detailframe.grid_propagate(0)
    for i in range(12):
        if i<=6: 
            detailframe.columnconfigure(i, weight=1)
            detailframe.rowconfigure(i, weight=1)
        else: 
            detailframe.rowconfigure(i, weight=1)
        
    if not RUNNING:
        details = ttk.Label(detailframe, text='Details')
        details.grid(row=0, column=0, columnspan=7, rowspan=1, sticky='nwes')
        
        today = ttk.Checkbutton(detailframe, text='Today', onvalue='1', variable=Date)
        tomorrow = ttk.Checkbutton(detailframe, text='Tomorrow', onvalue='', variable=Date)
        today.grid(row=2, column=1, columnspan=2, rowspan=1, sticky='nwes')
        tomorrow.grid(row=2, column=4, columnspan=2, rowspan=1, sticky='nwes')

        hourlabel = ttk.Label(detailframe, text='Hour', justify='center')
        hourlabel.grid(row=3, column=1, sticky='wes')
        minutelabel = ttk.Label(detailframe, text='Minute', justify='center')
        minutelabel.grid(row=3, column=5, sticky='wes')

        startlabel = ttk.Label(detailframe, text='Starting Time-> ')
        startlabel.grid(row=4, column=0, columnspan=1, sticky='we')

        
        starthourbox = ttk.Spinbox(detailframe, from_=0, to=23, textvariable=START_HOUR,
                                    wrap=True)
        starthourbox.grid(row=4, column=1)

        
        startminutebox = ttk.Spinbox(detailframe, from_=0, to=59, textvariable=START_MINUTE,
                                    wrap=True)
        startminutebox.grid(row=4, column=5)

        endlabel = ttk.Label(detailframe, text=' <-Ending Time')
        endlabel.grid(row=5, column=6, sticky='we')

        
        endhourbox = ttk.Spinbox(detailframe, from_=0, to=23, textvariable=END_HOUR,
                                    wrap=True)
        endhourbox.grid(row=5, column=1)

        
        endminutebox = ttk.Spinbox(detailframe, from_=0, to=59, textvariable=END_MINUTE,
                                    wrap=True)
        endminutebox.grid(row=5, column=5)
            
        schedule = ttk.Button(detailframe, text='Schedule', command=lambda: BEGIN_DAILY(root))
        schedule.grid(row=8, column=2,columnspan=3, sticky='nwes')

    else:
        update = ttk.Button(detailframe, text='Update', command=UPDATION)
        update.grid()
            
    optionframe = ttk.Frame(mainframe_1, style='white.TFrame')
    optionframe.grid(row=2, column=9, rowspan=8, columnspan=5)
    optionframe.grid_propagate(0)
    for i in range(12):
            if i<=6:
                optionframe.columnconfigure(i, weight=1)
                optionframe.rowconfigure(i, weight=1)
            else:
                optionframe.rowconfigure(i, weight=1)

            options = ttk.Label(optionframe, text='Options', justify='center')
            options.grid(row=0, column=0, columnspan=7, rowspan=1, sticky='nwes')

    deviation = ttk.Button(optionframe, text='Deviations', command=GET_DEVIATIONS)
    deviation.grid(row=1, column=2, columnspan=3, sticky='nwes')

    statistics = ttk.Button(optionframe, text='Statistics', command=GET_STATISTICS)
    statistics.grid(row=2, column=2, columnspan=3, sticky='nwes')

    settings = ttk.Button(optionframe, text='Settings', command=SETTINGS)
    settings.grid(row=4, column=0, sticky='nwes')

    tips = ttk.Button(optionframe, text='TIPS', command=TIPS)
    tips.grid(row=4, column=6, sticky='nwes')

    for i in range(14):
        if i <= 9:
            mainframe_1.columnconfigure(i, weight=1)
            mainframe_1.rowconfigure(i, weight=1)
        else:
            mainframe_1.columnconfigure(i, weight=1)
    for widget in mainframe_1.winfo_children():
        widget.grid_configure(padx=5, pady=5, sticky='nwes')

    for i in range(10):
            if (1 <= i <= 5) or (6 <= i <= 8):
                greetframe.columnconfigure(i, weight=2)
            else:
                greetframe.columnconfigure(i, weight=1)
    for i in range(4):
            if i == 1 or i == 2: greetframe.rowconfigure(i, weight=2)
            else: greetframe.rowconfigure(i, weight=1)


    return root

        
if __name__=='__main__':
    app = App()
    global Greet
    Greet.set('Helloooooooo00000000000000000000000000000000oooooo User!')
    global Date
    Date.set('bharath')
    
    app.mainloop()
    
    