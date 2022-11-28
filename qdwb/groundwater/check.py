
def check_positive(
    a: float,
    a_name: str
) -> float:
    """
    Description
    -----------
    Checking the input of the value, which should be greater than 0.

    Parameters
    ----------

    a : float
        value to be checked
    a_name: str
        such as 
        deep_perculation in m^3,
        entrance_groundwater in m^3,
        outlet_groundwater in m^3,
        evaporation_from_groundwater in m^3,
        penetration_from_free_surface_water in m^3,
        penetration_from_alluvial_fan in m^3,
        infiltration_by_artificial_feeding_projects in m^3,
        rate_of_water_leakage_from_underground_water_to_surface_water in m^3,
        withdrawal_from_springs in m^3,
        withdrawal_from_aqueducts in m^3,
        withdrawal_from_wells in m^3,
        R_fg in m^3,
        depth_of_undergroundwater in m
        discharge_from_the_spring_at_time_i in m^3
        discharge_from_the_spring_at_time_i1 in m^3
        
        
    
    """

    if a >= 0:
        a = a
    else:
        raise ValueError(f"{a_name} is greater than zero or equal zero!")



def check_is_evaporation_from_groundwater_or_not(
    depth_of_undergroundwater : float,
    evaporation_from_groundwater: float
) -> float:
    """
    Description
    -----------
    If the depth of the underground water is less than 5 meters, the volume
    of evaporation from the underground water is calculated, otherwise,
    the evaporation from the underground water is 0.

    Parameters
    ----------

    depth_of_undergroundwater : float
        groundwater depth in m

    evaporation_from_groundwater : float
        evaporation from groundwater in m^3
    
    Returns
    -------
    evaporation_from_groundwater : float
        evaporation from groundwater in m^3

    """

    if depth_of_undergroundwater > 5:
        return evaporation_from_groundwater

    else:
        return 0


