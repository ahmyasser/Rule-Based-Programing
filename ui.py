
import Tkinter
import tkMessageBox
from Tkinter import *

top = Tk()
top.geometry("500x500")

main = Tkinter.Frame(top)
main.grid()

L1 = Label(main, text="preconditions")
L1.grid(row=0, column=1)

E1 =Text(main, height=1, width=30)
E1.grid(row=0, column=2)
 
L2 = Label(main, text="Rules")
L2.grid(row=2, column=1)
E2 = Text(main, height=20, width=40)
E2.grid(row=2, column=2) 

def helloCallBack():
   #tkMessageBox.showinfo( "Hello Python", E1.get("1.0","end").split(" "))

   pre = E1.get("1.0","end-1c").split(" ")

   rules = E2.get("1.0","end-1c").split("\n")
   rules.reverse()

   for rule in rules:
      els = rule.split(" ")

      output= False
      remove = False
      for el in els:

	 if el == "then":
            output = True
   	 else:
         	if(not el in pre and not output):
		   break
  		else:
         	   if(output and el == "remove"):
	     	      remove = True
                   else:
   		      if(output and not el == "remove"):
			 if remove:
		            remove = False
			    pre.remove(el)
		         else:
	     	            pre.append(el)
   str1 = ' '.join(str(e) for e in pre)
   L3 = Label(main, text="output: "+ str1)
   L3.grid(row=4, column=2)

   print(list(dict.fromkeys(pre))) 

B = Tkinter.Button(main, text ="Submit", command = helloCallBack)
B.grid(column=2)


top.mainloop()
