import random
from prettytable import PrettyTable
from termcolor import colored

original_start = 31000
final_end = 41000

min_skip_kms = 0
max_skip_kms = 25
min_entry_kms = 5
max_entry_kms = 20
num_entries = 30

start_odometer = original_start
table = PrettyTable()

table.field_names = [colored("1st odometer reading", "green"), colored("2nd odometer reading", "green")]

while start_odometer < final_end and num_entries > 0:
    skip_kms = random.randint(min_skip_kms, max_skip_kms)
    start_odometer += skip_kms
    
    entry_kms = random.randint(min_entry_kms, max_entry_kms)
    end_odometer = start_odometer + entry_kms
    table.add_row([start_odometer, end_odometer])
    
    start_odometer = end_odometer
    num_entries -= 1

table.border = True
table.header = True
table.hrules = True
table.horizontal_char = '~'
table.junction_char = '|'
table._hrule_chars = 'x'

print(table)