from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

from .check import *

def snow_fall(
    tmax : float,
    tmin : float,
    tmean : float
):

    """
    Description
    -----------
    Check snowfall.
    **Reference**: Based on Equation 1-2 in SWB Version 2.0 (2018).
    Parameters
    ----------
    tmax : float
        Maximum Daily Temperature [Degrees Celsius]

    tmin : float
        Minimum Daily Temperature [Degrees Celsius]

    tmean : float
        Mean Daily Temperature [Degrees Celsius]
        
    Returns
    -------
    p : A sentence about the precipitation is snow or rain & boolean parameter.
    """

    if (tmean - 1/3 * (tmax - tmin)) <= 0:
        print('Snow')
        return True
    else:
        print('Rain')
        return False




def snow_melt(
    tmax : float,
) -> float:

    """
    Description
    -----------
    Calculate snow melting rate.
    **Reference**: Based on Equation 1-3 in SWB Version 2.0 (2018).
    Parameters
    ----------
    tmax : float
        Maximum Daily Temperature [Degrees Celsius]

    Returns
    -------
    M : float
       Snow melting rate [mm / day]
    """
    # Degree Day factor = 1.5 (mm/day.°c)
    DEGREE_DAY_FACTOR = 1.5

    check_maximum_temperature(tmax)

    return DEGREE_DAY_FACTOR * (tmax)



def evaporation_sublimation_snow_ice_surface(
    u10 : float,
    esn : float,
    e2 : float
) -> float:
    """
    Description
    -----------
    Calculate evaporation from snow and ice surfaces.
    **Reference**: Based on Equation 55-6 in Instructions for methods of calculating the balance of water resources(1393).
    Parameters
    ----------
    
    u10 : float
        Average daily values of wind speed at a height of 10 meters above the snow surface [m / s]
    
    esn : float
        Saturated vapor pressure corresponding to the temperature of the snow surface [Kpa]

    e2 : float
        Steam pressure at a height of 2 meters above the snow surface [Kpa]

    Returns
    -------
    E : float
       Evaporation [mm / day]
    """
    return ((0.18 + 0.98 * u10) * (esn - e2))