#Author(s): 1120079

#File: GUI_Task_GCD_LCM_Task.py
""" Simple cal for multiplication"""

import tkinter as tk
import math
root = tk.Tk()
root.title( "Calculator" )



def btn_cal(*args):

    try:
        a = float(txtA.get())
        b = float(txtB.get())
    except:
        result = "error!"
    else:
        txtresult.set(str(a*b))



txtA = tk.StringVar()
txtA.set( "0" )
entryA = tk.Entry( root, textvariable=txtA )
entryA.grid( row=0, column=0,sticky="w" )

txtB = tk.StringVar()
txtB.set( "0" )
entryB = tk.Entry( root, textvariable=txtB )
entryB.grid( row=0, column=2, sticky="w" )


lblsymbol = tk.Label( root, text="*" )  # hint: replace text(fixed) with textvariable
lblsymbol.grid( row=0, column=1, sticky="w" )

txtresult = tk.StringVar()
txtresult.set( "0.0" )
lblresult = tk.Label( root, textvariable = txtresult )  # hint: replace text(fixed) with textvariable
lblresult.grid( row=0, column=4, sticky="w" )

btn = tk.Button( root, text="=", command = btn_cal )
btn.grid( row=0, column=3 )

for child in root.winfo_children(): child.grid_configure( padx=5, pady=5 )
entryA.focus()

root.mainloop()


"""if __name__ == "__main__":

    print( ">>> doctest >>>" )
    import doctest
    doctest.testmod()
    print( "<<< doctest <<<" )"""
