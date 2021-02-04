import openpyexcel


class ReadData:
    def getRowCount(filepath, sheetname):
        workbook = openpyexcel.load_workbook(filepath)
        sheet = workbook[sheetname]
        return sheet.max_row

    def getColCount(filepath, sheetname):
        workbook = openpyexcel.load_workbook(filepath)
        sheet = workbook[sheetname]
        return sheet.max_column

    def readData(filepath, sheetname, rowno, colno):
        workbook = openpyexcel.load_workbook(filepath)
        sheet = workbook[sheetname]
        return sheet.cell(row=rowno, column=colno).value

    def writeData(filepath, sheetname, rowno, colno, data):
        print(data)
        workbook = openpyexcel.load_workbook(filepath)
        sheet = workbook[sheetname]
        sheet.cell(row=rowno, column=colno).value = data
        workbook.save(filepath)
