import Tkinter
import tkMessageBox
from Tkinter import *

top = Tk()
top.geometry("500x500")

main = Tkinter.Frame(top)
main.grid()

L1 = Label(main, text="preconditions")
L1.grid(row=0, column=1)

E1 = Text(main, height=1, width=30)
E1.grid(row=0, column=2)

L2 = Label(main, text="Rules")
L2.grid(row=2, column=1)
E2 = Text(main, height=20, width=40)
E2.grid(row=2, column=2)
def helloCallBack():
    # tkMessageBox.showinfo( "Hello Python", E1.get("1.0","end").split(" "))
    print(E1.get("1.0", "end-1c"))
    print(E2.get("1.0", "end-1c"))

    pre = E1.get("1.0", "end-1c").split(" ")

    rules = E2.get("1.0", "end-1c").split("\n")
    length = len(rules)

    i = 0

    while i < length and len(rules)>0:
        stack = []
        for rule in rules:
            els = rule.split(" ")
            for el in els:
                if el == "then" :
                    stack.append(rule)
                else:
                    if not el in pre :
                        break
        res = resolve(pre,stack)
        if  isinstance(res, basestring):
            pre = append_to_pre(pre, res)
            print("res "+res)
            rules.remove(res)
        print("rules now:" )
        print(rules)
        i +=1

    str1 = ' '.join(str(e) for e in pre)
    L3 = Label(main, text="output: " + str1)
    L3.grid(row=4, column=2)

    print(list(dict.fromkeys(pre)))


B = Tkinter.Button(main, text="Submit", command=helloCallBack)
B.grid(column=2)

def append_to_pre(pre , rule):
    output=False
    remove=False
    if not isinstance(rule, basestring):
        return pre
    els = rule.split(" ")
    for el in els:
        if remove:
            if el in pre:
                pre.remove(el)
        else:
            if output and not remove:
                if el == "remove":
                    remove = True
                else:
                    pre.append(el)
            else:
                if el == "then":
                    output=True


    return pre
def resolve(pre, stack):
    i = len(pre)-1
    while i >= 0:
        j= len(stack)-1
        while j>=0:
            rule = stack[j]
            p = pre[i]
            els = rule.split(" ")
            kb = []
            for el in els:
                if el == "then":
                    break
                else:
                    kb.append(el)
            if p in kb:
                return rule
            else:
                j-=1
        i -=1

top.mainloop()
print(resolve(["a" ],["b then v"]))
print(append_to_pre(["a", "b"],resolve(["a", "b"],["a then v","b then s"])))