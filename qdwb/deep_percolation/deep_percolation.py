
from check import *

class DeepPerculatoin :

    
    
    def __init__(self,
        feild_capacity: float,  
        soil_water: float,
        depth_soil: float,
        geology_permeability: float
    ):

        self.soil_water = soil_water
        self.feild_capacity = feild_capacity
        self.geology_permeability = geology_permeability
        self.depth_soil = depth_soil


    def inital_deep_perculation(
        feild_capacity : float,
        soil_water : float,
        depth_soil : float
    ) -> float:

        """
        Description
        -----------
        Claculation Deep Perculation (mm) By comparing the moisture of transitional layer of 
        the soil with its field capacity (%) and if the moisture (mm/day) of transitional layer is greater 
        than its field capacity, the amount of deep penetration will be equal to its difference.
        
        Parameters
        ----------

        feild_capacity : float
            Field capacity of the transitional layer of soil (% valume)

        soil_water : float
            Moisture of the transitional layer of soil in mm
        
        depth_soil : float
            Depth of transitional layer soil in cm
            
        Returns
        -------
        soil_water : float
            Moisture of the transitional layer of soil in mm
        inital_deep_perculation : float
            Deep penetration of the transitional layer of soil in mm
        """

        check_soil_water(soil_water = soil_water)
        check_feild_capacity(feild_capacity = feild_capacity)
        check_depth_soil(depth_soil = depth_soil)
        
        feild_capacity = (feild_capacity / 100) * depth_soil * 10
        
        
        
        if soil_water >= feild_capacity:

            initial_deep_perculation = soil_water - feild_capacity
            soil_water = feild_capacity

        else:

            initial_deep_perculation = 0
            soil_water = soil_water


        return initial_deep_perculation, soil_water


    def correction_deep_perculation(
        feild_capacity : float, 
        soil_water : float,
        depth_soil : float,
        geology_permeability : float      
    ) -> float:

        """
        Description
        -----------
        Deep penetration (mm) correction is calculated using a
        deep penetration coefficient with a value between 0 and 1,
        which is considered to be 0.1 for the mountains and 1 for the plains.
        
        Parameters
        ----------
        feild_capacity : float
            Field capacity of the transitional layer of soil (% valume)

        soil_water : float
            Moisture of the transitional layer of soil in mm
        
        depth_soil : float
            Depth of transitional layer soil in cm
        
        geology_permeability : float
            Permeability coefficient which is a number between 0 and 1
            
        Returns
        -------
        corrected_deep_perculation : float
            corrected_deep_perculation: modified deep penetration (mm)
        """

        check_soil_water(soil_water = soil_water)
        check_feild_capacity(feild_capacity = feild_capacity)
        check_depth_soil(depth_soil = depth_soil)
        check_geology_permeability(geology_permeability = geology_permeability)

        inital_deep_perculation = DeepPerculatoin.inital_deep_perculation(
            feild_capacity = feild_capacity, 
            soil_water = soil_water,
            depth_soil = depth_soil
        )


        corrected_deep_perculation = inital_deep_perculation[0] * (1 - geology_permeability)

        return corrected_deep_perculation



    def late_runoff(
        feild_capacity : float, 
        soil_water : float,
        depth_soil : float,
        geology_permeability : float
    ) -> float:
        """
        Description
        -----------
        Delayed runoff (mm) calculation using depth penetration (mm) calculated
        from the function calculationdeepperculation based on depth permeability coefficient
        
        Parameters
        ----------
        feild_capacity : float
            Field capacity of the transitional layer of soil (% valume)

        soil_water : float
            Moisture of the transitional layer of soil in mm
        
        depth_soil : float
            Depth of transitional layer soil in cm
        
        geology_permeability : float
            Permeability coefficient which is a number between 0 and 1
            
        Returns
        -------
        later_runoff : float
            later_runoff in mm
        """
        check_soil_water(soil_water = soil_water)
        check_feild_capacity(feild_capacity = feild_capacity)
        check_depth_soil(depth_soil = depth_soil)
        check_geology_permeability(geology_permeability = geology_permeability)

        inital_deep_perculation = DeepPerculatoin.inital_deep_perculation(
            feild_capacity = feild_capacity, 
            soil_water = soil_water,
            depth_soil = depth_soil
        )

        later_runoff = inital_deep_perculation[0] * geology_permeability

        return later_runoff