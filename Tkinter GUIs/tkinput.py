from tkinter import *


class Tkinput():
    def __init__(self, prompt):
        self.response = ""
        self.root = Tk()
        self.label = Label(self.root, text=prompt)
        self.label.pack()

        self.entrytext = StringVar()
        self.e = Entry(self.root, textvariable=self.entrytext)
        self.e.pack()
        self.e.focus_force()
        self.e.bind("<Return>", lambda _: self.clicked1())

        self.buttontext = StringVar()
        self.buttontext.set("return")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = Label(self.root, text="")
        self.label.pack()

        self.root.mainloop()

    def clicked1(self):
        self.response = self.entrytext.get()
        self.root.destroy()

    def getResponse(self):
        return self.response


def tkinput(prompt):
    imp = Tkinput(prompt)
    resp = imp.getResponse()
    return resp.strip()
