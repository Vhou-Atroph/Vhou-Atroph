from tkinter import *

global window
window=Tk()
idBox=Text(window,width=50,height=20,font=('Arial',8,'normal'),wrap=WORD)
theBtn=Button(window,text="Get IDS from URL")

def getID(url):
  if '/dragon/' in url:
    print(str(url.rsplit('/', 1)[-1]))
  else:
    pass
def loopIDGet():
  idBoxOutput=idBox.get(1.0,END)
  for link in idBoxOutput.splitlines():
    getID(link)
theBtn.configure(command=loopIDGet)

idBox.pack()
theBtn.pack()
window.mainloop()