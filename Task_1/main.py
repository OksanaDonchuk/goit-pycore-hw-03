# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days between the given date and today's date.
    
    Args:
        date (str): The date in 'YYYY-MM-DD' format.
        
    Returns:
        int: The number of days from the given date to today. If the given date 
             is in the future, the result will be negative.
    """
    # handle the error of incorrect date format
    try:
        transformed_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        # calculate the difference between today and the entered date
        difference = (today - transformed_date).days
        return difference
    except ValueError:
        # convert the date string into a date object
        print(f"Date {date} has invalid format. Try fotmat: YYYY-MM-DD")
            
result = get_days_from_today("2024-05-07")
if result is not None:
    print(result)

    