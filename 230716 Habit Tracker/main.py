from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate

habits = [
    break_habit('Coffee', datetime(2023, 7, 10, 10, 20), cost_per_day = 2, minutes_wasted = 15),
    break_habit('Beer', datetime(2023, 6, 30, 0, 0), cost_per_day = 2, minutes_wasted = 5),
    break_habit('Nail Biting', datetime(2023, 7, 15, 10, 00), cost_per_day = 0, minutes_wasted = 1)
  
]

df = pd.DataFrame(habits)

print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
