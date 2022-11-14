
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math
import datetime
from calendar import monthrange


def convert_celsius2kelvin(
    celsius : float
) -> float:
    
    """
    Description
    -----------
    Convert Temperature in Degrees Celsius to Degrees Kelvin.
    
    Parameters
    ----------
    celsius : float
        Temperature in Degrees Celsius
    
    Returns
    -------
    kelvin : float
        Temperature in Degrees Kelvin
    """
    
    return celsius + 273.15



def convert_kelvin2celsius(
    kelvin : float
) -> float:
    
    """
    Description
    -----------
    Convert Temperature in Degrees Kelvin to Degrees Celsius.
    
    Parameters
    ----------
    kelvin : float
        Temperature in Degrees Kelvin
    
    Returns
    -------
    celsius : float
        Temperature in Degrees Celsius
    """
    
    return kelvin - 273.15



def convert_degrees2radians(
    degrees : float
) -> float:
    
    """
    Description
    -----------
    Convert Angular Degrees to Radians.
    
    Parameters
    ----------
    degrees : float
        Value in Degrees
    
    Returns
    -------
    radians : float
        Value in Radians
    """
    
    return degrees * (math.pi / 180.0)



def convert_radians2degrees(
    radians : float
) -> float:
    
    """
    Description
    -----------
    Convert Angular Radians to Degrees.
    
    Parameters
    ----------
    radians : float
        Value in Radians
    
    Returns
    -------
    degrees : float
        Value in Degrees
    """
    
    return radians * (180.0 / math.pi)



def convert_radiation2evaporation(
    radiation : float
) -> float:
    
    """
    Description
    -----------
    Convert Radiation in MJ/m2/day to Equivalent Evaporation in mm/day.
    **Reference**: Based on Equation 20 in Allen et al (1998).
    
    Parameters
    ----------
    radiation : float
        Radiation in MJ/m2/day
    
    Returns
    -------
    equivalent evaporation : float
        Equivalent Evaporation in mm/day
    """
    
    return radiation * 0.408



def degree_minute_second_to_decimal_degree(
    degree : int,
    minute : int,
    second : int
    ) -> float:
 
    """
    Description
    -----------
    Convert degree_minute_second to decimal degree 
    ----------
    Latitude:
    degree : int
        degree in degree - Positive for the Northern Hemisphere and negative for the Southern Hemisphere
    minute : int
        minute in minute - Positive
    second : int
        second in second - Positive

   
    Returns
    -------
    decimal_degree : float
        decimal degree in degree
    """
    if degree < 0 :
        dd = -(abs(degree) + float(minute) / 60 + float(second) / 3600)
    else:
        dd = degree + float(minute) / 60 + float(second) / 3600

    return dd



def standard_date_to_Julian_day (
    standard_date_in_gregorian : str
    ) -> int:
       
    """
    Description
    -----------
    calculate Julian Day with standard date
    Ref:https://rafatieppo.github.io/post/2018_12_01_juliandate/
    ----------

    standard_date_in_gregorian : str
        Date with the specified standard

    Returns
    -------
    Julian Day : int
        Number of days of the year taking into account the leap year
    """
        
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(standard_date_in_gregorian, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday

    return(jdate)