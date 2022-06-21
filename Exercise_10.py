# Import pandas as pd
import pandas as pd

# Fix import by including index_col
# index_col = 0 meants the first column is used as a row labels
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)