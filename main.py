import os
import tkinter
import DBManager
top = tkinter.Tk(className="PyBackup")

#CREATION FRAME PART
#creating the frame for the menus
menuFrame=tkinter.Frame(top, width=500, height=30)
#creating the left part frame
leftFrame=tkinter.Frame(top, width=200, height=400)
#creating the listing frame of saves
listingFrame=tkinter.Frame(leftFrame, bg="white", width=200, height=300, highlightbackground="black", highlightthickness=2)
#creating the editing details frame
editFrame = tkinter.Frame(top, bg="white", width=800, height=350, highlightbackground="black", highlightthickness=2)


#file button
mnbtFile = tkinter.Menubutton(menuFrame, text="File")
mnbtFile.menu = tkinter.Menu(mnbtFile, tearoff=0)
mnbtFile["menu"] = mnbtFile.menu

NewEntryVar = tkinter.IntVar()
SettingsVar = tkinter.IntVar()
ExitVar = tkinter.IntVar()

mnbtFile.menu.add_checkbutton(label="New Entry", variable=NewEntryVar)
mnbtFile.menu.add_checkbutton(label="Settings", variable=SettingsVar)
mnbtFile.menu.add_checkbutton(label="Exit", variable=ExitVar)

#edit button
mnbtEdit = tkinter.Menubutton(menuFrame, text="Edit")
mnbtEdit.menu = tkinter.Menu(mnbtEdit, tearoff=0)
mnbtEdit["menu"] = mnbtEdit.menu

RemoveAllVar = tkinter.IntVar()
RemoveAllSavesVar = tkinter.IntVar()
RemoveDBVar = tkinter.IntVar()

mnbtEdit.menu.add_checkbutton(label="Remove All", variable=RemoveAllVar)
mnbtEdit.menu.add_checkbutton(label="Remove All Saves", variable=RemoveAllSavesVar)
mnbtEdit.menu.add_checkbutton(label="Remove Database", variable=RemoveDBVar)



saveButton = tkinter.Button(leftFrame, text="Save", highlightcolor="blue", width=27, height=1)

#packing everything
menuFrame.pack(side="top", fill=tkinter.X)
mnbtFile.pack(side="left")
mnbtEdit.pack(side="left")
leftFrame.pack(side="left")
listingFrame.pack(side="top",padx=10, pady=10)
editFrame.pack(side="right", padx=10, pady=10)
saveButton.pack(side="bottom", pady=10)
top.mainloop()
