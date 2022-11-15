from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn


def check_precipitation(
    precipitation : float 
):
    if precipitation < 0 :
        raise ValueError(f'value of  precipitation must be  postive : { precipitation}')



def check_evaporation_to_rainfall_ratio(
    evaporation_to_rainfall_ratio : float 
):
    """
    Discribtion
    in equation of saturated precipitation ;
    the value of (1-Evaporation_to_Rainfall_Ratio)
    shoud not be nagetive beacause of ln

    """
    
    if not evaporation_to_rainfall_ratio < 1:
        raise ValueError(f'evaporation_to_rainfall_ratio Must be less than one : {evaporation_to_rainfall_ratio}')

