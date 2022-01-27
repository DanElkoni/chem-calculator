import math
import os

full_path = os.path.realpath(__file__)

# Prepping data
dataTable = open(f'{os.path.dirname(full_path)}\data.text', 'a+')
dataTable.seek(0)
data = dataTable.readlines()

compoundTable = open(f'{os.path.dirname(full_path)}\compounds.text', 'a+')
compoundTable.seek(0)
compounds = compoundTable.readlines()

for i in range(len(data)):
  data[i] = data[i].strip('\n')
for i in range(len(compounds)):
  compounds[i] = compounds[i].strip('\n')

dataTable.seek(2)
compoundTable.seek(2)

#Rounding functions
def round_down(n, decimals):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
def round_up(n, decimals=2):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

#Percentage comp function
def calculateEPercentInComp():
    totalAtomicMass = 0.0
    listTotalAtomicMasses = []
    elements = []
    noOfAtoms = 0
    atomicMassOfAtom = 0
    global compound
    compound = ''

    elements = input('Enter the elements in the compound seperated by space: ').split()

    #Calculation and data collection
    for i in range(len(elements)):
        noOfAtoms = input(f'How many {elements[i]} atoms are there in your compound? ')
        
        compound += (elements[i])
        compound += (noOfAtoms)

        #Determining whether data has been inputted before
        if elements[i] in data:
          atomicMassOfAtom = data[data.index(elements[i]) + 1]
          print(f'{elements[i]} has a mass of {atomicMassOfAtom}')
        
        else:
          atomicMassOfAtom = input(f'What is the atomic mass of a(n) {elements[i]} atom, rounded to the nearest hundreds place? ')

          #Writing new data
          dataTable.write(f'{elements[i]}\n{atomicMassOfAtom}\n')

        listTotalAtomicMasses.append(float(noOfAtoms) * float(atomicMassOfAtom))
        totalAtomicMass += float(listTotalAtomicMasses[i])

    #Convert to a more readable and understandable display
    global displayCompound
    displayCompound = ''

    for i in range(len(compound)):
      if compound[i] == '1' and compound[i+1] not in [0,1,2,3,4,5,6,7,8,9]:
        pass
      else:
        displayCompound += compound[i]

    #Looks for and logs compound in compounds.text
    if compound in compounds:
        pass
    else:
        compoundTable.write(f'{compound}\n')
        compoundTable.write(f'{totalAtomicMass}\n')

    print(f'The total atomic mass of {displayCompound} is: {round_down(totalAtomicMass, 4)}')

    #Rounding function
    for i in range(len(elements)):

        if int(str((listTotalAtomicMasses[i]/totalAtomicMass) *100)[5]) >= 5:
            print(f'The element {elements[i]} has a total mass of {listTotalAtomicMasses[i]} in {displayCompound} and makes up {round_up((listTotalAtomicMasses[i] / totalAtomicMass) * 100)}% of it!')

        elif int(str((listTotalAtomicMasses[i]/totalAtomicMass) *100)[5]) < 5:
            print(f'The element {elements[i]} has a total mass of {listTotalAtomicMasses[i]} in {displayCompound} and makes up {round_down((listTotalAtomicMasses[i] / totalAtomicMass) * 100, 2)}% of it!')

        else:
            print(f'The element {elements[i]} has a total mass of {listTotalAtomicMasses[i]} in {displayCompound} and makes up {(listTotalAtomicMasses[i] / totalAtomicMass) * 100}% of it!')

    #Close files    
    dataTable.close()
    compoundTable.close()

    #Choose whether to go on
    quickAns = input('Would you like to convert from m-g(mols to grams) or g-m(grams to mols)? ').lower()
    if quickAns == 'g-m':
        calcGramToMol(totalAtomicMass)
    elif quickAns == 'm-g':
        calcMolToGram(totalAtomicMass)

#Conversion
def calcGramToMol(massOfComp):
    grams = input(f'How many grams of {displayCompound} would you like to convert to mol? ')
    mols = float(grams)/massOfComp
    molecules = round_down(mols * 6.32, 4) * 10**23
    print(f'{grams}g of this compound is {round_down(mols, 4)}mol! Which has {molecules} molecules of {displayCompound}')

def calcMolToGram(massOfComp):
    mols = input(f'How many mols of {displayCompound} would you like to convert to grams? ')
    gs = float(mols)*massOfComp
    molecules = round_down(mols * 6.32, 4) * 10**23
    print(f'{mols}mol(s) of this compound is {round_down(gs, 4)}g! Which has {molecules} molecules of {displayCompound}')

#Call function
calculateEPercentInComp()
