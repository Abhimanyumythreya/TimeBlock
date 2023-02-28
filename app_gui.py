from tkinter import *
from tkinter import ttk
#from PIL import Image as I, ImageTk
#Instead convert images into .ico and use iconbitmap method!

def SHUTDOWN():
    ...
def RUNNING():
    ...
def BEGIN_DAILY():
    sheet = Sheet()
    

def UPDATION(): pass
def GET_DEVIATIONS(): pass
def GET_STATISTICS(): pass
def SETTINGS(): pass
def TIPS(): pass

def App():
    root = Tk()
    root.title('TimeBlock')
    root.iconbitmap('letter-t.ico')
    root.minsize(1000, 700)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    s = ttk.Style()
    s.configure('TFrame', background='black')
    s.configure('white.TFrame', background='white')
    s.configure('TLabel', background='green')
    s.configure('TCheckbutton', background='blue')

    mainframe_1 = ttk.Frame(root, padding=5)
    mainframe_1.grid(row=0, column=0, sticky='nwes')

    greetframe = ttk.Frame(mainframe_1)
    greetframe.grid(row=0, column=0, rowspan=2, columnspan=14)

    global Greet
    Greet = StringVar()    
    greet = ttk.Label(greetframe, textvariable=Greet)
    greet.grid(row=1, column=1, rowspan=2, columnspan=4, sticky='nwes')

    global Shutdown
    Shutdown = StringVar()
    shutdown = ttk.Checkbutton(greetframe, text='ShutDown', 
                               variable=Shutdown, onvalue='1',
                               offvalue='', command=SHUTDOWN)
    shutdown.grid(row=1, column=6, columnspan=3, rowspan=2, sticky='nwes')


    detailframe = ttk.Frame(mainframe_1)
    detailframe.grid(row=2, column=0, rowspan=8, columnspan=7)
    if RUNNING:
        details = ttk.Label(detailframe, text='Details')
        details.grid(row=1, column=1)

        global Date
        Date=StringVar()
        today = ttk.Checkbutton(detailframe, text='Today', onvalue='1', variable=Date)
        tomorrow = ttk.Checkbutton(detailframe, text='Tomorrow', onvalue='', variable=Date)
        today.grid(row=2, column=0)
        tomorrow.grid(row=2, column=3)

        startlabel = ttk.Label(detailframe, text='Starting Time: ')
        startlabel.grid(row=3, column=1)
        global START
        START = StringVar()
        startbox = ttk.Spinbox(detailframe, from_=0, to=23, textvariable=START, wrap=True, justify='center')
        startbox.grid(row=3, column=3)

        endlabel = ttk.Label(detailframe, text='Ending Time: ')
        endlabel.grid(row=4, column=1)
        global END
        END = StringVar()
        endbox = ttk.Spinbox(detailframe, from_=0, to=23, textvariable=END, wrap=True, justify='center')
        endbox.grid(row=4, column=3)

        okbutton = ttk.Button(detailframe, text='Schedule', command=BEGIN_DAILY)
        okbutton.grid()
    else:
        update = ttk.Button(detailframe, text='Update', command=UPDATION)
        update.grid()
        

    optionframe = ttk.Frame(mainframe_1)
    optionframe.grid(row=2, column=7, rowspan=8, columnspan=7)

    deviation = ttk.Button(optionframe, text='Deviations', command=GET_DEVIATIONS)
    deviation.grid(row=0, column=0, columnspan=3)

    statistics = ttk.Button(optionframe, text='Statistics', command=GET_STATISTICS)
    statistics.grid(row=1, column=0, columnspan=3)

    settings = ttk.Button(optionframe, text='Settings', command=SETTINGS)
    settings.grid(row=3, column=0)

    tips = ttk.Button(optionframe, text='TIPS', command=TIPS)
    tips.grid(row=3, column=3)

    for i in range(14):
        if i <= 9:
            mainframe_1.columnconfigure(i, weight=1)
            mainframe_1.rowconfigure(i, weight=1)
        else:
            mainframe_1.columnconfigure(i, weight=1)
    for widget in mainframe_1.winfo_children():
        widget.configure(style='white.TFrame')
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
def Sheet():
    app = Toplevel()
    s = ttk.Style()
    s.configure('dateframe.TFrame', background='#BDB74D')
    s.configure('TFrame', background='#DFEBEB')
    s.configure('metricframe.TFrame', background='#288499')
    s.configure('taskframe.TFrame', background='#465994')
    s.configure('ideaframe.TFrame', background='#624694')
    s.configure('blockframe.TFrame', background='#F2BC8D')

    mainframe_1 = ttk.Frame(app, padding=5)
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

    app.grid_columnconfigure(0, weight=1, minsize=1400)
    app.grid_rowconfigure(0, weight=1, minsize=1000)

    for i in range(14):
        mainframe_1.grid_columnconfigure(i, weight=1)

    for i in range(15):
        mainframe_1.grid_rowconfigure(i, weight=1)

    for widget in mainframe_1.winfo_children():
        widget.grid_configure(padx=5, pady=5)
        widget.configure(borderwidth=20, relief=SOLID)

        
if __name__=='__main__':
    app = App()
    global Greet
    Greet.set('Helloooooooo00000000000000000000000000000000oooooo User!')
    global Date
    Date.set('bharath')
    app.mainloop()