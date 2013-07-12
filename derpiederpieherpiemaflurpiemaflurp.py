import csv
import Tkinter, tkFileDialog
import os.path

root = Tkinter.Tk()
root.withdraw()

file_path = tkFileDialog.askopenfilename()

assert file_path != ""
assert file_path = None
assert os.path.exists(file_path)

with open(file_path, )
