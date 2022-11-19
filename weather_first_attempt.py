# This file is a record of my first attempt
# at solving some questions
# I forgot to commit along the process

import csv
from datetime import datetime
import calendar


DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celsius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # ISO Example: 2021-07-02T07:00:00+08:00
    # expected_result = "Monday 05 July 2021"

    
    # slicing iso_string to get required info
    date = iso_string[8:10]

    month_as_number = iso_string[5:7]
    year = int(iso_string[0:4])


    # remove "0" from month_as_number
    # if string starts with "0"
    if month_as_number[0] == "0":
        month_as_number = month_as_number[1:]
    month_as_number = int(month_as_number)

    weekday_as_number = datetime(year,month_as_number,int(date)).weekday()

    # convert to human readable format
    month = calendar.month_name[month_as_number]
    weekday = calendar.day_name[weekday_as_number]
    return f"{weekday} {date} {month} {year}"

    # try with strptime()


def convert_f_to_c(temp_in_farenheit):
    """Converts a temperature from farenheit to celsius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celsius, rounded to 1dp.
    """
    return round((float(temp_in_farenheit) - 32) * 5 / 9, 1)
    

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(x) for x in weather_data]
    return sum(weather_data)/len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file) as csv_data_list:
        reader = csv.reader(csv_data_list)
        # skip heading line
        next(csv_data_list)
        # remove empty line
        for data in reader:
            if line == []:
                continue
            # example line:
            # ["2021-07-02T07:00:00+08:00", 49, 67]
            # append first item in list_in_list
            list_in_list = [] # new list every loop
            list_in_list.append(line[0])
            # item [1],[2] str into int
            for item in line[1:]:
                item = int(item)
                # append int to list_in_list
                list_in_list.append(item)
            weather_data.append(list(list_in_list))
    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()

    min_temp = ()
    for i, temp in enumerate(weather_data):
        temp = float(temp)
        if (min_temp == ()):
            min_temp = (temp, i)
            continue
        if (temp <= min_temp[0]):
            min_temp = (temp, i)

    return min_temp

    

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    
    if len(weather_data) == 0:
        return ()

    max_temp = ()
    for i, temp in enumerate(weather_data):
        temp = float(temp)
        if (max_temp == ()):
            max_temp = (temp, i)
            continue
        if (temp >= max_temp[0]):
            max_temp = (temp, i)

    return max_temp



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
