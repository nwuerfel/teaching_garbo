from Tkinter import *
import sys

class displayHub:
    def __init__(self, master,numEntries):
        self.master = master
        master.title("A simple GUI for interfacing with student data")

        self.label = Label(master, text="Some garbo")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

def main(argv):
        root = Tk()
        my_gui = displayHub(root,2)
        root.mainloop()

if __name__ == '__main__':
    main(sys.argv[1:])
