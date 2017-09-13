from tkinter import Tk, Label, W, N, Entry, Button, filedialog
class request_window:
    def __init__(self,text):
        self.root_req = Tk()
        self.root_req.title('Words per minute')
        # get screen width and height
        ws = self.root_req.winfo_screenwidth() # width of the screen
        hs = self.root_req.winfo_screenheight() # height of the screen
        w,h = 250,120
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
        self.root_req.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.result = None
        instruction = Label(self.root_req,text = text)
        instruction.grid(columnspan = 2,sticky = W,padx = 10)

        self.req_field = Entry(self.root_req)
        self.req_field.grid(columnspan = 2,row = 1, sticky = N,padx = 10)

        log_button = Button(self.root_req,text = "Enter",command = self.enter)
        log_button.grid(row = 3,column = 0,pady = 10)
        self.root_req.bind("<Return>",self.enter)

        cancel_button = Button(self.root_req,text = "Cancel", command = self.cancel)
        cancel_button.grid(row = 3,column = 1,pady = 10)
        self.root_req.bind("<Escape>",self.cancel)
        self.root_req.mainloop()

        if self.result == None or self.result == False:
            raise ValueError("\n\n\tRequest cancelled by user.\n\n")


    def enter(self,event = None):
        self.result = self.req_field.get()
        self.root_req.destroy()

    def cancel(self,event = None):
        self.result = False
        self.root_req.destroy()

def select_file(title):
    ftypes = [
        ('txt files', '*.txt'),
        ('All files', '*'),
    ]

    root_sel = Tk()
    root_sel.withdraw()
    root_sel.title(title)
    filename = filedialog.askopenfile(filetypes=ftypes,initialdir = "./datafiles/")
    root_sel.destroy()
    try:
        return(filename.name)
    except:
        raise KeyError('\n\n\tFile selection cancelled by user.\n\n')
