import ExcelMods as Ex

excel1 = Ex.ExcelInit("example.xlsx", "Sheet1")
excel2 = Ex.ExcelInit("example.xlsx", "Sheet2")

excel1.open_sheet()
excel2.open_sheet()

if excel1.get_dimensions() == excel2.get_dimensions():
    print("Dimensions Match")
    for cell in excel1.get_coordinates():
        excel1.compare_values(excel1, excel2, cell)
else:
    print("Dimensions don't match, no further action will be performed. ")



    #
    # if ws1[cell].value != ws2[cell].value:
    #     print(f"Values in both sheet do not match at coordinate - {cell}")
    #     print(f"value in {ws1} at {cell} - {ws1[cell].value}")
    #     print(f"value in {ws2} at {cell} - {ws2[cell].value}")
    #


#
#
#
#
#
# wb = openpyxl.load_workbook("example.xlsx")
# ws1 = wb["Sheet1"]
# ws2 = wb["Sheet2"]
#
# if (ws1.max_row == ws2.max_row) and (ws1.max_column == ws2.max_column):
#     print("Dimensions match")
#
# print(ws1['A1'].value)
#
#
# def get_coordinates():
#     for row in ws1.iter_rows():
#         for cel in row:
#             yield cel.coordinate
#
#
# for cell in get_coordinates():
#     if ws1[cell].value != ws2[cell].value:
#         print(f"Values in both sheet do not match at coordinate - {cell}")
#         print(f"value in {ws1} at {cell} - {ws1[cell].value}")
#         print(f"value in {ws2} at {cell} - {ws2[cell].value}")


# for row in ws1.iter_rows():
#     for cell in row:






