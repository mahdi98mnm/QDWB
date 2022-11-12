
from .error_crop import *


def correction_crop_coefficient_for_step_mid_and_end(
    crop_coefficient_mid : float,
    crop_coefficient_end : float,
    RH_min : float,
    maximum_crop_height : float,
    wind_speed_at_2m : float
) -> float:
    
    """
    Description
    -----------
    calculate correction_crop_coefficient_for_step_mid_and_end - eq 70 FAO56
    ----------
    crop_coefficient_mid : float
        crop_coefficient_mid - crop_coefficient in middle of step - Table 12 Page 110 FAO56
    crop_coefficient_end : float
        crop_coefficient_end - crop_coefficient in end of step - Table 12 Page 110 FAO56
    RH_min : float
        Minimum relative humidity in percent
    maximum_crop_height : float - Table 12 Page 110 FAO56
        Maximum crop height in meter
    wind_speed_at_2m : float
        Wind speed at 2m in meter / second

    Returns
    -------
    Modified crop coefficient : float
        Modified crop coefficient in No unit

    """
    

    if crop_coefficient_mid >= 0.45 :
        cor_crop_coefficient_mid = crop_coefficient_mid + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (maximum_crop_height / 3) ** 0.3
    elif wind_speed_at_2m != 2 or RH_min != 45 :
        cor_crop_coefficient_mid = crop_coefficient_mid + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (maximum_crop_height / 3) ** 0.3
    else :
        cor_crop_coefficient_mid = crop_coefficient_mid
    

    if crop_coefficient_end >= 0.45 :
        cor_crop_coefficient_end = crop_coefficient_end + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (maximum_crop_height / 3) ** 0.3
        
    elif wind_speed_at_2m != 2 or RH_min != 45 :
        cor_crop_coefficient_end = crop_coefficient_end + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (maximum_crop_height / 3) ** 0.3
    else :
        cor_crop_coefficient_end = crop_coefficient_end
    


    return cor_crop_coefficient_mid, cor_crop_coefficient_end
   



def calculate_crop_coefficient_for_linear_changes_steps(
    crop_coefficient_ini : float,
    crop_coefficient_mid : float,
    crop_coefficient_end : float,
    length_ini_crop : int,
    length_dev_crop : int,
    length_mid_crop : int,
    length_late_crop : int,
    plant_date : str,
    modeling_date : str
) -> float:
    
    """
    Description
    -----------
    calculate crop_coefficient_for_linear_changes_steps in special day - eq 66 FAO56
    ----------

    crop_coefficient_ini : float
        crop_coefficient_ini - crop_coefficient in start of step - Table 12 Page 110 FAO56
    crop_coefficient_mid : float
        crop_coefficient_mid - crop_coefficient in middle of step - Table 12 Page 110 FAO56
    crop_coefficient_end : float
        crop_coefficient_end - crop_coefficient in end of step - Table 12 Page 110 FAO56
    length_ini_crop : int
        length_ini_crop - length of initial crop in day - Table 11 Page 104 FAO56
    length_dev_crop : int
        length_dev_crop - length of development crop in day - Table 11 Page 104 FAO56
    length_mid_crop : int
        length_mid_crop - length of middle crop in day - Table 11 Page 104 FAO56
    length_late_crop : int
        length_late_crop - length of late crop in day - Table 11 Page 104 FAO56
    plant_date : str
        plant_date - Date of planting in format YYYY-MM-DD - Table 11 Page 104 FAO56 according to Region
    modeling_date : str
        modeling_date - Date of modeling in format YYYY-MM-DD


    Returns
    -------
    crop_coefficient : float
        crop_coefficient in special day in No unit

    """
    plant_date = date(int(plant_date[:4]), int(plant_date[5:7]), int(plant_date[8:]))
    modeling_date = date(int(modeling_date[:4]), int(modeling_date[5:7]), int(modeling_date[8:]))
    n = modeling_date - plant_date
    n_day = n.days
    # n_day : Number of days since the beginning of crop cultivation
    
    check_date_for_crop_coefficient(
        plant_date = plant_date,
        modeling_date = modeling_date,
        n = n_day,
        length_ini_crop = length_ini_crop,
        length_dev_crop = length_dev_crop,
        length_mid_crop = length_mid_crop,
        length_late_crop = length_late_crop)
        
    if n_day <= length_ini_crop :
        crop_coefficient = crop_coefficient_ini

    elif length_ini_crop < n_day <= length_ini_crop + length_dev_crop :
        crop_coefficient = crop_coefficient_ini + ((n_day - length_ini_crop) / length_dev_crop) * (
            crop_coefficient_mid - crop_coefficient_ini)

    elif length_ini_crop + length_dev_crop < n_day <= length_ini_crop + length_dev_crop + length_mid_crop :
        crop_coefficient = crop_coefficient_mid

    elif length_ini_crop + length_dev_crop + length_mid_crop < n_day <= length_ini_crop + length_dev_crop + length_mid_crop + length_late_crop :
        crop_coefficient = crop_coefficient_mid + ((n_day - length_ini_crop - length_dev_crop - length_mid_crop) / length_late_crop) * (
            crop_coefficient_end - crop_coefficient_mid)
    
    return crop_coefficient