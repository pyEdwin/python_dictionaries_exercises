# Pre-defined lists
from pytz import country_names


country_names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drives_right =  [True, False, False, False, True, True, True]
cars_per_cap = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country_names':['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'], 'drives_right':[True, False, False, False, True, True, True],'cars_per_cap':[809, 731, 588, 18, 200, 70, 45]}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
