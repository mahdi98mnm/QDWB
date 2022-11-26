

def check_soil_water(
    soil_water: float
) -> float:
    """
    Check the moisture content of the soil transition layer that is greater than 0

    Input:

        soil_water: Moisture of the transition layer of soil (mm)
    """

    
    if soil_water >= 0:
        soil_water = soil_water
    else:
        raise ValueError("You can not enter a negative value")



def check_feild_capacity(
    feild_capacity: float
) -> float:

    """
    Check the field capacity of the transition layer of soil that is between 0 and 100 percent
    
    Input:

        feild_capacity: Field capacity of the transition layer of soil (% valume)
    """

    if 0 <= feild_capacity <= 100:
        feild_capacity = feild_capacity
    else:
        raise ValueError("The value entered must be between 0 and 100%")    



def check_geology_permeability(
    geology_permeability: float
) -> float:

    """
    Check the Geology Permeability between 0 and 1

    Input

        geology_permeability: Permeability coefficient which is a number between 0 and 1
    """

    if 0 <= geology_permeability <= 1:
        geology_permeability = geology_permeability
    else:
        raise ValueError("The value entered must be between 0 and 1")



def check_depth_soil(
    depth_soil: float
) -> float:

    """
    Check the depth of the third soil layer that is greater than 0

    Input
        depth_soil:  Depth of third layer soil (cm)
    """

    if depth_soil >= 0:
        depth_soil = depth_soil
    else:
        raise ValueError("You can not enter a negative value")