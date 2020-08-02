#A Genereic Function to read the Specific Values from a CSV, Print all the Rows of a Specific Column
def readColumn(fileName:str=None, columnNo:int=1, sep:str='	', skipRows:int=-1):
    columnValues = []
    
    if fileName == None: 
        print("< Min - Usage : varName = readColumn(fileName) >")
    
    try:
        columnValues = []

        inpFile = open(fileName)

        for l in range(skipRows+1):
            inpFile.readline()

        while True:
            line = inpFile.readline().strip().split(sep)
            if line == ['']:
                break
            else:
                columnValues.append(line[columnNo-1])

        inpFile.close()
    except Exception as e:
        print("Error Occured. Please check your Arguments again.")
    
    return columnValues

# def WriteColumn(fileName:str=None, columnNo:int=1, sep:str=',', skipRows:int=-1):
