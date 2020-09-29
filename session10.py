# Session 10 Assignment - Tuple and Named Tuple
# Author: Sujit Kumar Ojha
# email : sujit.ojha@gmail.com

from collections import namedtuple, Counter
from functools import reduce
from faker import Faker
from datetime import datetime,timedelta
from time import perf_counter
import random


# Loading an Faker object
faker = Faker()

# Fake profile named tupple
profile = namedtuple("Fake_Profile", sorted(faker.profile().keys()))
profile.__doc__ = "Fake Profile Created using Faker library"
profile.address.__doc__ = "Permanent Address"
profile.birthdate.__doc__ = "Birth Date"
profile.blood_group.__doc__ = "Blood Group e.g. A+,AB+, O,O+"
profile.company.__doc__ = "Company"
profile.current_location.__doc__ = "Current Location in Latitude and Longitude"
profile.job.__doc__ = "Job Title"
profile.mail.__doc__ = "email address"
profile.name.__doc__ = "Name"
profile.residence.__doc__ = "Residential Address"
profile.sex.__doc__ = "Sex"
profile.ssn.__doc__ = "Social Security Number"
profile.username.__doc__ = "Username"
profile.website.__doc__ = "Website"

# Created 10000 profile dict using namedtuple - profile
profiles_dict_temp = {f"profile_{i}":profile(**faker.profile()) for i in range(10000)}

# Created 10000 people named tuple using inside namedtupple - profile
fake_profiles = namedtuple("Fake_Profiles", sorted(profiles_dict_temp))
fake_profiles_tupple = fake_profiles(**profiles_dict_temp)

# Created 10000 profile dict using dictionary - profile
profiles_dict = {key:value._asdict()for key,value in profiles_dict_temp.items()}

def largest_blood_type(profiles_tpl,profiles_dict):
    """ Find out the largest blood type in given profiles

    Returns:
        Performance for 200x times
    """


    start = perf_counter()
    for i in range(200):
        blood_group_list = [value['blood_group'] for value in profiles_dict.values()]
        blood_group_summary = Counter(blood_group_list)
        Max_blood_group = max(blood_group_summary, key=blood_group_summary.get) 

    elapsed_dict = (perf_counter() - start)/100
    print(f'Dictionary Results\nLargest blood group is {Max_blood_group} and average of 200 run it took {elapsed_dict*1000:4.2f} ms')


    start = perf_counter()
    for i in range(200):
        blood_group_list = [i.blood_group for i in profiles_tpl]
        blood_group_summary = Counter(blood_group_list)
        Max_blood_group = max(blood_group_summary, key=blood_group_summary.get) 

    elapsed_tpl = (perf_counter() - start)/100
    print(f'Named Tuple Results\nLargest blood group is {Max_blood_group} and average of 200 run it took {elapsed_tpl*1000:4.2f} ms')

    return elapsed_tpl,elapsed_dict


def mean_current_location(profiles_tpl,profiles_dict):
    """ Calculates the mean of current location for all profiles

    Returns:
        Performance for 200x times
    """

    start = perf_counter()
    for i in range(200):
        Latitude,Longitude = reduce(lambda prev,next: (prev[0]+next[0],prev[1]+next[1]),[i['current_location'] for i in profiles_dict.values()],(0,0))
        Latitude,Longitude = Latitude/10000,Longitude/10000

    elapsed_dict = (perf_counter() - start)/200
    print(f'Dictionary Results\nMean location: Latitude = {Latitude}, Longitude = {Longitude} and average of 200 run it took {elapsed_dict*1000:4.2f} ms')

    start = perf_counter()
    for i in range(200):
        Latitude,Longitude = reduce(lambda prev,next: (prev[0]+next[0],prev[1]+next[1]),[i.current_location for i in profiles_tpl],(0,0))
        Latitude,Longitude = Latitude/10000,Longitude/10000

    elapsed_tpl = (perf_counter() - start)/200
    print(f'Named Tuple Results\nMean location: Latitude = {Latitude}, Longitude = {Longitude} and average of 200 run it took {elapsed_tpl*1000:4.2f} ms')

    return elapsed_tpl,elapsed_dict

def oldest_person_age(profiles_tpl,profiles_dict):
    """ Calculates the oldest person age from fake profiles

    Returns:
        Performance for 200x times
    """

    start = perf_counter()
    for i in range(200):
        oldest_person_dob = min([i['birthdate'] for i in profiles_dict.values()])
        oldest_person_age = int((datetime.now().date() - oldest_person_dob).days/365)

    elapsed_dict = (perf_counter() - start)/200
    print(f'Dictionary Results\nOldest Person Age (years): {oldest_person_age} and average of 200 run it took {elapsed_dict*1000:4.2f} ms')

    start = perf_counter()
    for i in range(200):
        oldest_person_dob = min([i.birthdate for i in profiles_tpl])
        oldest_person_age = int((datetime.now().date() - oldest_person_dob).days/365)

    elapsed_tpl = (perf_counter() - start)/200
    print(f'Named Tuple Results\nOldest Person Age (years): {oldest_person_age} and average of 200 run it took {elapsed_tpl*1000:4.2f} ms')

    return elapsed_tpl,elapsed_dict

def average_age(profiles_tpl,profiles_dict):
    """ Calculates the average age from fake profiles

    Returns:
        Performance for 100x times
    """

    start = perf_counter()
    for i in range(200):
        average_age = sum([datetime.now().date()-i['birthdate'] for i in profiles_dict.values()],timedelta(0))/10000
        average_age = int((average_age).days/365)

    elapsed_dict = (perf_counter() - start)/200
    print(f'Dictionary Results\nAverage Age (years): {average_age} and average of 200 run it took {elapsed_dict*1000:4.2f} ms')

    start = perf_counter()
    for i in range(200):
        average_age = sum([datetime.now().date()-i.birthdate for i in profiles_tpl],timedelta(0))/10000
        average_age = int((average_age).days/365)

    elapsed_tpl = (perf_counter() - start)/200
    print(f'Named Tuple Results\nAverage Age (years): {average_age} and average of 200 run it took {elapsed_tpl*1000:4.2f} ms')

    return elapsed_tpl,elapsed_dict

def faker_company_stock_data():
    """Create fake company data with stock open, high and close for a day
    100 companies with random stock prices
    Return:
        Named tuple with company stock exchange
    """
    CompanyStockData = namedtuple('CompanyStockData',"Company_Name Symbol Open High Close")

    # Get company name from Faker
    fake_company_name = faker.company()

    # Set the stock value from Rs. 50 to Rs. 5000 randomly
    min_stock_val=50
    max_stock_val = 5000
    stock_value = (random.randint(0,100)*(max_stock_val-min_stock_val)/100 + min_stock_val)

    # Set the interday change between -10% to +10%
    min_change_val = -10
    max_change_val = 10

    # Random day tranding values created
    day_trading = [stock_value + stock_value/100*random.randint(0,100)*(max_change_val-min_change_val)/100 + min_change_val for i in range(10)]

    fake_company = CompanyStockData(Company_Name=fake_company_name,
                                    Symbol=fake_company_name[0:4].upper(),
                                    Open=day_trading[0], 
                                    High=max(day_trading),
                                    Close=day_trading[-1])
    
    return fake_company

# Created 100 profile dict using namedtuple - faker_company_stock_data
company_dict_temp = {f"company_{i}":faker_company_stock_data() for i in range(100)}

# Created 100 people named tuple using inside namedtupple - faker_company_stock_data
company_stock_market = namedtuple("CompanyStockMarket", sorted(company_dict_temp))
company_stock_market_tupple = company_stock_market(**company_dict_temp)

def stock_market_status(named_tuple):
    """Print the stock market status - Open, High & Close
    """
    stock_market_today = named_tuple
    stock_market_today_start = sum([stock.Open for stock in stock_market_today])
    stock_market_today_high = sum([stock.High for stock in stock_market_today])
    stock_market_today_close = sum([stock.Close for stock in stock_market_today])   

    print(f"Stock Market Start: {stock_market_today_start:7.2f},High: {stock_market_today_high:7.2f}, End: {stock_market_today_close:7.2f}")

    return stock_market_today_start, stock_market_today_high, stock_market_today_close