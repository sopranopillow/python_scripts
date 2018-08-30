###///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////###
### Note: Please rename the file to so that it doesn't have any special character or spaces so that the script doesn't confuse the script ###
### Note: xlWings needed and python to be able to run this script                                                                         ###
###///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////###

### Script made by: Esteban Munoz
### Contact me for any questions at:
### Email: esteban.230@hotmail.com
### Github username: sopranopillow

import xlwings as xwings
import sys

def getTableValues(letter, firstRange, secondRange, thirdRange, fourthRange):
    output = ""
    letterRange = getRangeOfLetter(letter, firstRange)
    startIndex = letterRange[0]
    halfIndex = int((letterRange[1]-letterRange[0])/2)

    while firstRange[startIndex] < letterRange[1] and halfIndex < letterRange[1]:
        output += (
            "       <tr>\n"+
            "           <td>"+firstRange[startIndex]+" "+secondRange[startIndex]+" "+thirdRange[startIndex]+"</td>\n"+
            "           <td>"+fourthRange[startIndex]+"</td>\n"+
            "           <td>&#160;</td>\n"+
            "           <td>"+firstRange[halfIndex]+" "+secondRange[halfIndex]+" "+thirdRange[startIndex]+"</td>\n"+
            "           <td>"+fourthRange[halfIndex]+"</td>\n"+
            "       <tr>\n"
        )
    return output

def getRangeOfLetter(letter, firstRange):
    startLetterIndex = 0
    while firstRange[startLetterIndex][0] != letter
        startLetterIndex+=1

    endLetterIndex = startLetterIndex
    while firstRange[endLetterIndex][0] == letter
        endLetterIndex+=1

    return [startLetterIndex, endLetterIndex]

# Function that searched for the range of the columns given the name of the column
def getRange(columnStart, sheet):
    startIndex = 1

    while sheet.range('A'+str(startIndex)).value != columnStart :
        startIndex += 1
        if startIndex > 300:
            print("Something went wrong, maybe the name of the column has a typo?")
            sys.exit()

    # Needed since there is no do while
    startIndex+=1

    endIndex = startIndex

    while sheet.range('A'+str(endIndex)).value != None:
        endIndex += 1

    # Needed because of extra index
    endIndex-=1

    return [startIndex, endIndex]

def getValues(letter, columnRange, sheet):
    currentIndex = columnRange[0]
    values = []
    while currentIndex < columnRange[1] :
        values.insert(currentIndex - columnRange[0], sheet.range(letter+str(currentIndex)).value)
        currentIndex+=1
    return values

def createTable(letter, firstRange, secondRange, thirdRange, fourthRange):
    output = (
        "<h2>\n"+
        "   <a id=\""+letter.lower()+"\"><a/>"+letter+
        "<table border=\"0\" style=\"width: 100%\">\n"+
        "   <tbody>\n"+
        "       <tr>\n"+
        "           <td>\n"+
        "               <strong>NAME:</strong>\n"+
        "           </td>\n"+
        "           <td>\n"+
        "               <strong>MAJOR:</strong>\n"+
        "           </td>\n"+
        "           <td>&#160;</td>\n"+
        "           <td>\n"+
        "               <strong>NAME:</strong>\n"+
        "           </td>\n"+
        "           <td>\n"+
        "               <strong>MAJOR:</strong>\n"+
        "           </td>\n"+
        "       </tr>\n"+
        "   </tbody>\n"+
        "   <tbody>\n"+
                getTableValues(letter, firstRange, secondRange, thirdRange, fourthRange, columnRange)+
        "   </tbody>\n"+
        "</table>\n"+
        "<p class=\"textright\">\n"+
        "   <a href=\"#\">Back to top</a>\n"+
        "</p>\n"
    )

# Asking for a file path to the excel file
print("Please enter the path of the file")
file = input()

# Asking for the name of the sheet
print("Please enter the name of the excel sheet")
sheet = input()

try:
    # Reding the excel file
    book = xwings.Book(file)

    # Getting excel sheet
    sheet = xwings.sheets[sheet]

except:
    print("err: Error loading the file")

# Asking for the exact names of the columns to start the process
print("Please enter the exact name of the first column, for example: Last NAME")
firstColumnName = input()

print("\n\nA file will be created in the same directory the script is \n\n")

# Getting ranges for from the columns
columnRange = getRange(firstColumnName, sheet)

# Setting the values
firstRange = getValues('A', columnRange, sheet)
secondRange = getValues('B', columnRange, sheet)
thirdRange = getValues('C', columnRange, sheet)
fourthRange = getValues('D', columnRange, sheet)

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','XY','Z']

createTable('A', firstRange, secondRange, thirdRange, fourthRange)

print(firstRange)
print("\n\n")
print(secondRange)
print("\n\n")
print(thirdRange)
print("\n\n")
print(fourthRange)
print("\n\n")