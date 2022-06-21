import openpyxl 
import time
from datetime import datetime
from openpyxl import Workbook

book = Workbook()
# wb = load_workbook(filename = 'option_chain.xlsx')
sheet = book.active

 
# Print value of cell object
# using the value attribute
# print(cell_obj.value)

sheet['A1'] = "time"
sheet['B1'] = "buy_price"
sheet['C1'] = "sell_price"
sheet['D1'] = "strike_price"

book.save('data_recorder_nifty50.xlsx')
# book.save('data_recorder_ntpc.xlsx')