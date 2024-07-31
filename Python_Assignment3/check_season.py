def check_season(month):
    """Return the season for a given month."""
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'
month = input("Enter the month: ")
season = check_season(month)
print(f"The season for {month.capitalize()} is {season}.")
