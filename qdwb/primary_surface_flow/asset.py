from check import *
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

def modify_CN(
    curve_number: float,
    antecedent_precipitation: float,
    is_growing_season: bool
) -> float:
    """
    Description
    -----------
    Modify Curve Number using Antecedent Moisture Condition
    **Reference**: Guide Lines for Estimating Runoff for Design of Irrigation and Drainage Networks. No.519 (2010)

    Parameters
    ----------
    antecedent_precipitation : float
        Sum of Precipitation for previous 5 days - Starts from 0 - mm

    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless

    is_growing_season: bool
        Check if its growing season or not

    Returns
    -------
    - modified curve number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless
    """

    check_curve_number(curve_number)
    check_antecedent_precipitation(antecedent_precipitation)
    check_is_growing_season(is_growing_season)
    

    if (is_growing_season and antecedent_precipitation < 12.7) or \
        (not(is_growing_season) and antecedent_precipitation < 35.6):
        return (4.2*curve_number) / (10-0.058*curve_number)
        
    elif (is_growing_season and 12.7 < antecedent_precipitation < 27.9) or \
        (not(is_growing_season) and 35.6 < antecedent_precipitation < 53.3):
        return curve_number

    elif (is_growing_season and antecedent_precipitation > 27.9) or \
        (not(is_growing_season) and antecedent_precipitation > 53.3):
        return (23*curve_number) / (10 + 0.13*curve_number)





def calculate_potential_retention(
    curve_number: float
) -> float:
    """
    Description
    -----------
    Calculate potential retention known as "S"
    **Reference**: National Resources Conservation Service, National Engineering Handbook, Section 4 "Hydrology" (1985)

    Parameters
    ----------
    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless

    Returns
    -------
    - potential_retention : float
        Maximum depth of storm rainfall that could potentially be abstracted by a given site - Starts from 0 - mm
    """

    check_curve_number(curve_number)

    # Constant 25.4, convert inch to mm
    return (1000/curve_number - 10)*25.4