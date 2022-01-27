import math

# Prepping data
dataTable = open('E:\Programs\ChemCalc\data.text', 'a+')
dataTable.seek(0)
data = dataTable.readlines()

for i in range(len(data)):
  data[i] = data[i].strip('\n')

dataTable.seek(2)

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

    elements = input('Enter the elements in the compound seperated by space: ').split()

    #Calculation and data collection
    for i in range(len(elements)):
        noOfAtoms = input(f'How many {elements[i]} atoms are there in your compound? ')
        
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
    print(f'Your total atomic mass is: {round_down(totalAtomicMass, 4)}')

    #Rounding function
    for i in range(len(elements)):

        if int(str((listTotalAtomicMasses[i]/totalAtomicMass) *100)[5]) >= 5:
            print(f'The element {elements[i]} has a total mass of {listTotalAtomicMasses[i]} in your compound and makes up {round_up((listTotalAtomicMasses[i] / totalAtomicMass) * 100)}% of it!')

        elif int(str((listTotalAtomicMasses[i]/totalAtomicMass) *100)[5]) < 5:
            print(f'The element {elements[i]} has a total mass of {listTotalAtomicMasses[i]} in your compound and makes up {round_down((listTotalAtomicMasses[i] / totalAtomicMass) * 100, 2)}% of it!')

        else:
            print(f'The element {elements[i]} has a total mass of {listTotalAtomicMasses[i]} in your compound and makes up {(listTotalAtomicMasses[i] / totalAtomicMass) * 100}% of it!')

    #Close data table file    
    dataTable.close()

#Call function
calculateEPercentInComp()