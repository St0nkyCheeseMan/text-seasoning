import tkinter
import string
class TextSeasoner:
    @staticmethod
    def strangeCaser(txt):
        i = 0
        p = 0
        while(i<len(txt)):
            if txt[i] in string.ascii_letters:
                if p % 2 == 0:
                    txt = txt[:i] + txt[i].lower() + txt[i+1:]
                else:
                    txt = txt[:i] + txt[i].upper() + txt[i+1:]
                i += 1
                p += 1
            else:
                i += 1
        return txt
top = tkinter.Tk()
top.title("Text Seasoner - F1av0r Y0ur T3xT!")
f1 = tkinter.Frame(top)
f1.pack()
f2 = tkinter.Frame(top)
f2.pack()
txt = tkinter.Text(f1, height = 10, width = 120, font=("Arial", 10, "normal"))
txt.pack(side=tkinter.LEFT)
S = tkinter.Scrollbar(f1,command=txt.yview)
txt.configure(yscrollcommand=S.set)
S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
def converter():
    to_convert = txt.get("1.0", "end-1c")
    txt.delete(1.0,"end")
    txt.insert(1.0, TextSeasoner.strangeCaser(to_convert))
w = tkinter.Button(f2, text="Convert", command = converter)
w.pack(side=tkinter.BOTTOM)
top.mainloop()