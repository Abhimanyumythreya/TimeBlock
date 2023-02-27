from tkinter import *
from tkinter import ttk

app = Tk()
s = ttk.Style()
s.configure('TFrame', background='#DFEBEB')
s.configure('dateframe.TFrame', background='#BDB74D')
s.configure('metricframe.TFrame', background='#288499')
s.configure('taskframe.TFrame', background='#465994')
s.configure('ideaframe.TFrame', background='#624694')
s.configure('blockframe.TFrame', background='#F2BC8D')

mainframe_1 = ttk.Frame(app, padding=5)
dateframe = ttk.Frame(mainframe_1, borderwidth=20, style='dateframe.TFrame')
metricframe = ttk.Frame(mainframe_1, borderwidth=20, style='metricframe.TFrame')
taskframe = ttk.Frame(mainframe_1, borderwidth=20, style='taskframe.TFrame')
ideaframe = ttk.Frame(mainframe_1, borderwidth=20, style='ideaframe.TFrame')
blockframe = ttk.Frame(mainframe_1, borderwidth=20, style='blockframe.TFrame')

mainframe_1.grid(row=0, column=0, sticky='nwes')
dateframe.grid(row=0, column=0, columnspan=14, rowspan=1, sticky='nwes')
metricframe.grid(row=1, column=0, columnspan=14, rowspan=3, sticky='nwes')
taskframe.grid(row=4, column=0, columnspan=4, rowspan=6, sticky='nwes')
ideaframe.grid(row=4, column=4,columnspan=3, rowspan=6, sticky='nwes')
blockframe.grid(row=4, column=7, columnspan=7, rowspan=6, sticky='nwes')

app.grid_columnconfigure(0, weight=1, minsize=1400)
app.grid_rowconfigure(0, weight=1, minsize=1000)

for i in range(14):
    mainframe_1.grid_columnconfigure(i, weight=1)
for i in range(10):
    mainframe_1.grid_rowconfigure(i, weight=1)

for widget in mainframe_1.winfo_children():
    widget.grid_configure(padx=5, pady=5)

app.mainloop()