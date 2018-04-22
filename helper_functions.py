# Last updated 04/11/18 @ 12:23
import pandas as pd
import sys

def age_at_election(dob, election_date):
    '''Given an election date and a date of birth, return the person's age 
    in years on election day. Return years as floor of years - ie, if someone is 70 years old
    and 360 days, return 70. '''
    try:
        return relativedelta(pd.to_datetime(election_date), pd.to_datetime(dob, format="%Y%m%d")).years
    except:
        return float('nan')

def young_at_election(series, election_date):
    '''Given an election date and a date of birth pandas Series, return 
    a Series whether or not someone was 24 or under on election day.
    Return years as floor of years - ie, if someone is 70 years old
    and 360 days, return 70. '''
    return pd.to_datetime(series, format = "%Y%m%d", errors = "coerce") + pd.DateOffset(years=24) >= election_date


def find_election(array, year, e_type):
    if array is None:
        return None
    
    if e_type.lower() == "general":
        e_type = "GE"
    elif e_type.lower() == "primary":
        e_type = "PR"
    else:
        return None
    
    year = str(year)
    
    for election in array:
        if year in election and e_type in election:
            return True
    return False

# Loading bar from: https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)
