from tkinter import Tk
from tkinter import filedialog
import os
import glob

root = Tk()
root.withdraw()
current_directory = filedialog.askdirectory()
if current_directory:
    file_path = os.path.join(current_directory, "*.*")
    f = glob.glob(file_path)
    # glob的第二参数recursive默认False表示不匹配子目录里的文件
    print(f)
