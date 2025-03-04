# This program outputs whether or not today is a weekday
#
# Author: Elaine Cazetta
# Source: W3Schools , ChatGPT
#
# Import the datetime module to work with dates
from datetime import datetime

# Get the current day of the week
today = datetime.today().weekday()

# Check if it's a weekday or weekend
if today < 5:  # 0-4 are Monday to Friday
    print("Yes, unfortunately today is a weekday.")
else:          # 5 and 6 are Saturday and Sunday
    print("It is the weekend, yay!")