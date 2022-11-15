
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
from check import *
import math

def saturated_precipitation (
    canopy_storage_capacity : float,
    canopy_cover : float,
    evaporation_to_rainfall_ratio: float
)-> float:
    """
    Description
    -------------------------
    calculate interception by Gash mathod , saturated_precipitation
    **reference**based on researches of Gash(1995):
    SWB Version 2.0—A ,page :27 & 28 ,
    A Modified Gash Model for Estimating Rainfall Interception
    Loss of Forest Using Remote Sensing Observations at
    Regional Scale_ Yaokui Cui  and Li Jia _2014
    -------------------------
    Parameters
    ----------

    canopy_storage_capacity : float
        canopy_storage_capacity in inch & constant

    canopy_cover : float 
        canopy_cover in dimentionless

    evaporation_to_rainfall_ratio : float
        Evaporation_to_Rainfall_Ratio in dimentionless
    
    Returns
    -------
    saturated_precipitation : float
        saturated_precipitation in inch  

    """    
    check_evaporation_to_rainfall_ratio(evaporation_to_rainfall_ratio)

    saturated_precipitation = -(canopy_storage_capacity/(canopy_cover * evaporation_to_rainfall_ratio))* math.log(1-evaporation_to_rainfall_ratio)
    
    return saturated_precipitation



def ratio_of_trunk_storage_capacity_to_stem_flow (
    trunk_storage_capacity : float,
    stem_flow :float
) -> float :
    """
    Description
    -------------------------
    calculate interception by Gash mathod , ratio_of_trunk_Storage_Capacity_to_stem_flow
    **reference**based on researches of Gash(1995):
    SWB Version 2.0—A ,page :27 & 28 ,
    A Modified Gash Model for Estimating Rainfall Interception
    Loss of Forest Using Remote Sensing Observations at
    Regional Scale_ Yaokui Cui  and Li Jia _2014
    parameters
    -------------------------
    Parameters
    ----------

    trunk_storage_capacity : float
        trunk_storage_capacity in inch

    stem_flow : float
        stem_flow in dimentionless
    
    Returns
    -------
    ratio_of_trunk_storage_capacity_to_stem_flow: float
        ratio_of_trunk_storage_capacity_to_stem_flow in inch

    """
    ratio_of_trunk_storage_capacity_to_stem_flow = trunk_storage_capacity / stem_flow

    return ratio_of_trunk_storage_capacity_to_stem_flow
