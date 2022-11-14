from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

def check_greater_than(
    a: float,
    a_name: str,
    b: float,
    b_name: str,
) -> NoReturn:
    if a > b:
        raise ValueError(f"{a_name} is greater than {b_name}!")


def check_between(
    a: float,
    min: float,
    max: float,
    name: str,
) -> NoReturn:
    if a < min or a > max:
        raise ValueError(f"{name} must be between {min} and {max}!")


def check_date_for_crop_coefficient(
    plant_date : str,
    modeling_date : str,
    n : int,
    length_ini_crop : int,
    length_dev_crop : int,
    length_mid_crop : int,
    length_late_crop : int
):
    """
    Description
    -----------
    check range date for crop coefficient
    ----------

    plant_date : str
        plant_date - Date of planting in format YYYY-MM-DD - Table 11 Page 104 FAO56 according to Region
    modeling_date : str
        modeling_date - Date of modeling in format YYYY-MM-DD
    n : int
        Number of days since the beginning of crop cultivation in number of days
    length_ini_crop : int
        length_ini_crop - length of initial crop in day - Table 11 Page 104 FAO56
    length_dev_crop : int
        length_dev_crop - length of development crop in day - Table 11 Page 104 FAO56
    length_mid_crop : int
        length_mid_crop - length of middle crop in day - Table 11 Page 104 FAO56
    length_late_crop : int
        length_late_crop - length of late crop in day - Table 11 Page 104 FAO56

    Returns
    -------
    raise error or not
    """
    
    if plant_date > modeling_date :
        raise ValueError('The modeling day should be more than the plant day')
    
    if n > length_ini_crop + length_dev_crop + length_mid_crop + length_late_crop :
        raise ValueError('You are out of growth period')