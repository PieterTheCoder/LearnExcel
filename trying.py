from openxyl import Workbook

#Make new workbook
workbook = Workbook()

#Choose activate sheet
sheet = workbook.activate

#Import data to cell
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["A2"] = "EP"
sheet["B2"] = "21"

#Save Excel file
workbook.save("data.xlsx")
