import tkinter as tk
import time
import sys

#variables
numSamples=0
maxSamples=4
idx = 0
sEqual=0
aList = []
aList1 = []
tMesureList = []
t0 = time.clock()
keyword = "bryan gonzalez."

def mesureList():
	global tMesureList
	for k in range(0,(len(aList)-1)):
		j = aList[k+1] - aList[k]
		tMesureList.append(j)

def helloCallBack():
	text.insert('end', '\n')	
	list2string()

def compareAnswer():
	global sEqual
	sList = ''.join(aList1)
	if sList == keyword:
		text.insert('end', 'Sucessful\n')
		sEqual = 1
		return sEqual
	else:
		text.insert('end', 'no equals\n')
		sEqual = 0
		return sEqual
	
def onKeyPress(event):
	global idx 
	if str(keyword[idx]) != str(event.char):
		 clearRedo()
	else:
		idx+=1
		text.insert('end', '%s' % (event.char, )) #text.insert('end', 'You pressed %.8f\n' % (time.clock() - t0, ))
		aList.append(time.clock() - t0)
		aList1.append(event.char)
		if '.' == str(event.char):
			idx=0
			text.insert('end', '\nProcessing..\n') #text.insert('end', '\nfound period\n')
			compareAnswer()
			if sEqual:
				mesureList()
				printList()
				if numSamples >= maxSamples:
					quitProgram()
	
def list2string():
	sList = ''.join(aList1)
	text.insert('end', sList)
	if sList == keyword:
		printList()
	else:
		aList[:] = []
		aList1[:] = []
		tMesureList[:] = []
		idx=0

def printList():
	global aList
	global aList1
	global numSamples
	global tMesureList
	filename = 'data'+str(numSamples)+'.txt'
	f = open(filename,'w')
	for item in aList:
		f.write("%f\n" % item)
	for item in aList1:
		f.write("%s\n" % item)	
	for item in tMesureList:
		f.write("%f\n" % item)	
	f.close()
	aList[:] = []
	aList1[:] = []
	tMesureList[:] = []
	idx=0
	numSamples += 1
	
def clearRedo():
	global idx
	aList[:] = []
	aList1[:] = []
	tMesureList[:] = []
	idx=0
	text.insert('end', '\nTypo Failed Attempt\n')

def quitProgram():
		sys.exit()
	
#_______________________start of main_________________________

#tk declare instance
root = tk.Tk()
root.geometry('500x600')

#create 3 objects for tk
w = tk.Label(root, text=keyword, font=('Comic Sans MS', 18))
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 10))
B = tk.Button(root, text ="done", command = helloCallBack)

#pack the object
w.pack()
B.pack()
text.pack()

#run program
root.bind('<KeyPress>', onKeyPress)
root.mainloop()