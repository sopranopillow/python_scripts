import pandas as panda
import sys, os
import xlwings as xwings

from pandas import ExcelWriter
from pandas import ExcelFile

###///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////###
### Note: Please rename the file to so that it doesn't have any special character or spaces so that the script doesn't confuse the script ###
### Note: Pandas, xlWings needed, and python to be able to run this script                                                                ###
###///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////###

# Asking for a file path to the excel file
print("Please enter the path of the file")
file = input()

# Asking for the name of the sheet
print("Please enter the name of the excel sheet")
sheet = input()

# Xlwings needed for password protected files
wb = xwings.Book(file)
sheet = wb.sheets[sheet]

df = panda.read_excel(file, sheet)

print("Column headings: ")
print(df.columns)