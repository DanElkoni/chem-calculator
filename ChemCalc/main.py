from tkinter import *
from tkinter import ttk
import math
import os
# Initial vars
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
rawComp = ''

# Data prep
full_path = os.path.realpath(__file__)

dataTable = open(f'{os.path.dirname(full_path)}\data.text', 'a+')
dataTable.seek(0)
data = dataTable.readlines()

for i in range(len(data)):
	data[i] = data[i].strip('\n')

dataTable.seek(2)

# Rounding Functions
def round_down(n, decimals):
	multiplier = 10 ** decimals
	return int(n * multiplier) / multiplier
def round_up(n, decimals=2):
	multiplier = 10 ** decimals
	return math.ceil(n * multiplier) / multiplier

# WINDOW AND GUI DEFINING ->
# Window defining
root = Tk()
root.geometry('450x300')
root.resizable(False, False)
root.title('Chemistry Calculator')

# Title style
titleStyle = ttk.Style()
titleStyle.configure('big.TLabel', font=('Helvetica', 15))

mainTitle = ttk.Label(text="Welcome to the Chemistry Calculator!", style='big.TLabel')
mainTitle.pack()

labelStyle = ttk.Style()
labelStyle.configure('medium.TLabel', font=('Helvetica', 13), padding=3)

firstLabel = ttk.Label(text='Enter a compound formula!', style='medium.TLabel')
firstLabel.place(x=0,y=40)

# Comp entry box
compEntryBox = ttk.Entry(root)
compEntryBox.place(width=167,x=210,y=44)

def getComp():
	rawComp = split(compEntryBox.get())
	global displayComp
	displayComp = compEntryBox.get()
	compEntryBox.delete(0, END)
	combineElements(rawComp)
	print(rawComp)

# Comp box Button
entryButton = ttk.Button(text='Enter!', command=getComp)
entryButton.place(width=50,x=390,y=41)

# Label and entry for masses
massLabel = ttk.Label(text='Enter element symbol then mass: ', style='medium.TLabel')
massLabel.place(x=0, y=70)

massEntry = ttk.Entry()
massEntry.place(width=128, x=250, y=74)

# Display final info
infoLabel = ttk.Label(text='Info on your compound here!', style='medium.TLabel')
infoLabel.pack(anchor='center',pady=70)

def logElements():
	symbolMass = massEntry.get()
	symbolMass = symbolMass.split()
	if symbolMass[0] not in data:
		dataTable.write(f'{symbolMass[0]}\n{symbolMass[1]}\n')
	massEntry.delete(0, END)

#Button for masses
entryButtonMass = ttk.Button(text='Enter!', command=logElements)
entryButtonMass.place(width=50,x=390,y=72)


# Actual code and functions
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

def combineStrs(compound):
	i = 0
	ix = 0
	while i < len(compound)-1:
		if compound[i] in numbers:
			if compound[i+1] in numbers:
				compound[i] += compound[i+1]
				compound.pop(i+1)
				i += 1
		i += 1

	while ix < len(compound)-1:
		if compound[ix] in numbers and compound[ix+1] in numbers:
			combineStrs(compound)
		else:
			ix += 1
	
	addOnes(compound)

def split(compound):
    return list(compound)

def combineElements(compound):
	i = 0
	while i < len(compound):
		if compound[i].isupper():
			if compound[i+1].islower():
				compound[i] += compound[i+1]
				compound.remove(compound[i+1])
				i+=1
		i+=1
	combineStrs(compound)

def addOnes(compound):
	i = 0

	while i < len(compound)-1:
		if compound[i] not in numbers:
			if compound[i+1] not in numbers:
				compound.insert(i+1, '1')
				i += 1   
		i += 1
	if compound[len(compound)-1] not in numbers:
		compound.append('1')

	calcAllVals(compound)
	
def calcAllVals(compound):
	dataString = ''

	totalCompMass = 0
	elements = []
	elementNum = []
	i = 0
	while i < len(compound):
		elements.append(compound[i])
		elementNum.append(int(compound[i+1]))
		i += 2

	for i in range(len(elements)):
		totalCompMass += elementNum[i] * float(data[data.index(elements[i]) + 1])
	dataString += f'The total atomic mass of {displayComp} is {totalCompMass}\n'
	
	for i in range(len(elements)):
		percentMass = (elementNum[i] * float(data[data.index(elements[i]) + 1]) / totalCompMass) * 100
		if int(str(percentMass)[5]) >= 5:
			percentMass = round_up(percentMass)
		elif int(str(percentMass)[5]) <= 5:
			percentMass = round_down(percentMass, 2)
		dataString += f'The element {elements[i]} makes up %{percentMass} of {displayComp}\n'

	dataString += f'10 grams of {displayComp} is {round_down(10/totalCompMass, 4)} mols!\n'

	infoLabel.configure(text=dataString)

root.mainloop()

dataTable.close()