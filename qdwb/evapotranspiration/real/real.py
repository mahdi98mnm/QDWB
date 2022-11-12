from cmath import exp
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math


def available_evaporable_water(
    e_a : float,
    is_in_fisrt_step : bool,
    infiltration : float,
    initial_available_evaporable_water : float = None,
    available_evaporable_water_in_previous_step : float = None
) -> float:

    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------
    e_a : float
        evaporation_noncovered_areas in mm
    is_in_fisrt_step : bool
        Is_in_fisrt_step in boolean - True if we are on the first day, False if we are not on the first day
    infiltration : float
        infiltration in mm
    initial_available_evaporable_water : float
        initial available evaporable water in mm - If we are on the first day, we must enter a hypothetical value
    available_evaporable_water_in_previous_step : float
        available evaporable water in previous step in mm
    

    Returns
    -------
    available_evaporable_water : float
        available evaporable water in mm
    
    """
    if is_in_fisrt_step is True:
        ae = initial_available_evaporable_water
    else:
        ae = available_evaporable_water_in_previous_step
    
    

    return (0.5 * infiltration) + ae - e_a



def available_water(
    permanent_wilting_point_wet : float,
    field_capacity_wet : float,
    soil_depth : float
) -> float:

    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------
    permanent_wilting_point_wet : float
        permanent wilting point wet in percent(volumetric)
    field_capacity_wet : float
        field capacity wet in percent(volumetric)
    soil_depth : float
        soil depth in mm
   
    Returns
    -------
    available_water : float
        available water in No units
    
    """
    fc = field_capacity_wet * soil_depth
    pwp = permanent_wilting_point_wet * soil_depth

    return (fc - pwp) / 100



def moisture_reduction_function(
    soil_wetness_in_previous_step : float,
    permanent_wilting_point_wet : float,
    field_capacity_wet : float,
    soil_depth : float
) -> float:
    
    """
    Description
    -----------
    calculate moisture reduction function With FC and PWP and SW(t-1) - eq 2 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    soil_wetness_in_previous_step : float
        soil wetness in previous step in percent(volumetric)
    permanent_wilting_point_wet : float
        permanent wilting point wet in percent(volumetric)
    field_capacity_wet : float
        field capacity wet in percent(volumetric)
    soil_depth : float
        soil_depth in mm
    Returns
    -------
    moisture_reduction_function : float
        moisture reduction function in No units
    """
    
    fc = (field_capacity_wet / 100) * soil_depth
    pwp = (permanent_wilting_point_wet / 100) * soil_depth

    
    return (soil_wetness_in_previous_step - pwp) / (fc - pwp)



def et_covered(
    moisture_reduction_function : float,
    crop_coefficient : float,
    crop_cover : float,
    reference_crop_evapotranspiration : float
) -> float:
    
    """
    Description
    -----------
    calculate evapotranspiration covered areas With QDWB approach - eq 3 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    moisture_reduction_function : float
        moisture reduction function in No units
    crop_coefficient : float
        crop coefficient in No units
    crop_cover : float
        crop cover in No units
    reference_crop_evapotranspiration : float
        reference crop evapotranspiration in mm
   
    Returns
    -------
    evapotranspiration_covered_areas : float
        evapotranspiration covered areas in mm
    """
    f = moisture_reduction_function
    
    return f * crop_coefficient * crop_cover * reference_crop_evapotranspiration



def ratio_of_actual_evaporable_water_to_total_evaporable_water(
    is_in_fisrt_step : bool,
    available_water : float,
    available_evaporable_water : float,
    initial_available_evaporable_water : float = None
) -> float:
    
    """
    Description
    -----------
    calculate ratio of actual evaporable water to total evaporable water - eq 5 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    is_in_fisrt_step : bool
        Is_in_fisrt_step in boolean - True if we are on the first day, False if we are not on the first day
    available_water : float
        available water in No units
    available_evaporable_water : float
        available evaporable water in mm
    initial_available_evaporable_water : float
        initial available evaporable water in mm - If we are on the first day, we must enter a hypothetical value
   
    Returns
    -------
    ratio_of_actual_evaporable_water_to_total_evaporable_water : float
        ratio_of_actual_evaporable_water_to_total_evaporable_water in No units
    """
    if Is_in_fisrt_step is True : 
        ae = initial_available_evaporable_water
    else:
        ae = available_evaporable_water
        
    
    aw = available_water

    return ae / aw



def e_noncovered(
    ratio_of_actual_evaporable_water_to_total_evaporable_water : float,
    crop_cover: float,
    reference_crop_evapotranspiration : float
) -> float:

    """
    Description
    -----------
    calculate evaporation_noncovered_areas With Ke and cc and ET0 - eq 4 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx 
    ----------

    ratio_of_actual_evaporable_water_to_total_evaporable_water : float
        ratio_of_actual_evaporable_water_to_total_evaporable_water in No units
    crop_cover : float
        crop cover in no units
    reference_crop_evapotranspiration : float
        reference crop evapotranspiration in mm

   
    Returns
    -------
    evaporation_noncovered_areas : float
        evaporation_noncovered_areas in mm
    
    """
    
    ke = ratio_of_actual_evaporable_water_to_total_evaporable_water

    return (1 - crop_cover) * reference_crop_evapotranspiration * ke



def et_QDWB(
    evaporation_noncovered_areas : float,
    evapotranspiration_covered_areas : float
) -> float:

    # reference_evapotranspiration
    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------

    evaporation_noncovered_areas : float
        evaporation_noncovered_areas in mm
    evapotranspiration_covered_areas : float
        evapotranspiration covered areas in mm
   
    Returns
    -------
    et_QDWB : float
        real evapotranspiration with QDWB in mm
    
    """
    ET_covered = evapotranspiration_covered_areas

    E_noncovered = evaporation_noncovered_areas

    return ET_covered + E_noncovered