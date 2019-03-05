import Tkinter
from Tkinter import Canvas
from Tkinter import Radiobutton
from Tkinter import IntVar

import gobject

import os


class BciUI:
  def __init__(self, root):
    self.ui_window = root
    self.ui_window.title("BCI Experimentation System")
    self.Fcanvas = Canvas(bg="black", height=600, width=170)
    self.start_video(root)

  def start_video(self,root):


    def snd1():
      os.system("/Users/priscilla/Documents/Thesis/BCI_Experimentation_System/sample1.mp4")

    var = IntVar()

    rb1 = Radiobutton(root, text="Play Video", variable=var, value=1, command=snd1)
    rb1.pack()
    self.Fcanvas.pack()
    root.mainloop()



def main():
  root = Tkinter.Tk()
  BciUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()


