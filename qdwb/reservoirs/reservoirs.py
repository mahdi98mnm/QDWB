import math
from check import *



class RemainedVolumeReservoirs :

    def __init__(self,
        height: float,
        height_min: float,
        height_max: float,
        standard_height : float,
        max_area : float,
        a : float,
        p : float,
        precipitation : float,
        reservoirs_area : float
    ):
        self.height = height
        self.height_min = height_min
        self.height_max = height_max
        self.standard_height = standard_height
        self.max_area = max_area
        self.a = a
        self.p = p
        self.precipitation = precipitation
        self.reservoirs_area = reservoirs_area


    def standard_height(
    height: float,
    height_min: float,
    height_max: float  
    ) -> float:
        """
        Description
        -----------
        calculate the standard height of water in reservoir in m.
        ----------
        height : float
            height in m
        height_max : float
            maximum height in m
        height_min : float
            minimum height in m
        

        Returns
        -------
        standard_height : float
            standard height in m
        """
        check_not_negative(height = height)
        check_not_negative(height = height_min)
        check_not_negative(height = height_max)
        check_greater_than(
            a=height_min,
            a_name="height_min",
            b=height_max,
            b_name="height_max"
        )  

        return (height - height_min) / (height_max - height_min)



    def water_area(
        standard_height : float,
        max_area : float,
        a : float,
        p : float
    ) -> float:

        """
        Description
        -----------
        Convert height of water in reservoir in m to Area of water in m^2.
        **Reference**: Based on Equation Vecchia, A.V., 2002
        Parameters
        ----------
        standard_height : float
            standard height in m
        max_area : float
            Area in m^2 is maximum af Area of water in reservoir = Height_max * Area
        
        a : float
        p: float
            a and p are adjustable parameters
            a>0 and p>1
        

        Returns
        -------
        water_area : float
            Area of surface water in m^2
        """
        check_Value_a(a = a)
        check_Value_p(p = p)
        check_not_negative(height = standard_height)
        

        temp_1 = (a * standard_height) + (0.5 * (1 - a) * (1 - math.cos(math.pi * standard_height))) 
        temp_2 = ((1 - a) * math.pi * math.sin(math.pi * standard_height)) / (2 * a)
        
        return max_area * (temp_1 ** (p - 1)) * (1 + temp_2)



    def water_volume(
        standard_height : float,
        height_min : float,
        height_max : float,
        max_area : float,
        a : float,
        p : float
    ) -> float:
        
        """
        Description
        -----------
        Convert height of water in reservoir in m to Area of water in m^2.
        **Reference**: Based on Equation Vecchia, A.V., 2002 .
        Parameters
        ----------
        standard_height : float
            standard height in m
        height_min : float
            minimum height in m
        height_max : float
            maximum height in m
        max_area : float
            Area in m^2 is maximum af Area of water in reservoir = Height_max * Area
        a : float
        p: float
            a and p are adjustable parameters
            a>0 and p>1
        

        Returns
        -------
        water_volume : float
            Area of surface water in m^2
        """
        check_Value_p(p)
        check_Value_a(a)
        check_not_negative(height = standard_height)
        check_not_negative(height = height_min)
        check_not_negative(height = height_max)
        check_greater_than(
            a=height_min,
            a_name="height_min",
            b=height_max,
            b_name="height_max"
        )  
        

        water_volume = (max_area *(height_max - height_min) / (p * a)) * (a * standard_height + 0.5 * (1 - a) * (1 - math.cos(math.pi * standard_height))) ** p

        return   water_volume



    def precipitation_volume(
        precipitation : float,
        reservoirs_area : float
    ) -> float:
        """
        Description
        -----------
        Estimate rainfall volume that rain on the reservoir in m^3.
        **Reference**: Based on Equation Nouvelot, J.F. (1993) 
        Parameters
        ----------

        precipitation : float
            rainfall on reservoir in m
        reservoirs_area : float
            Area water of Reservoirs in m**2

        Returns
        -------
        precipitation_volume : float
            volume of rainfall in m^3
        """


        return precipitation * reservoirs_area



    def remained_water_volume_at_the_end_of_current_step(
        water_volume : float,
        precipitation_volume : float,
        volume_runoff : float, 
        volume_groundwater : float,
        volume_evaporation : float, 
        volume_wier : float,
        volume_infiltration : float, 
        volume_use : float
    ) -> float:
        
        """
        Description
        -----------
        Estimate Volume of left over water in reservoir(Volume_water2) Using the Balance equation for reservoirs
        **Reference**: Based on Equation Nouvelot, J.F. (1993) 
        Parameters
        ----------

        water_volume : float
            Volume of water at the start time in m^3
            it's diffrences from type of reservoirs
            reservoir considered as a unadjustable reservoir 
        Volume_Percipitation : float
            volume of percipitation that falls on the reservoir in m^3 Can Be Calculated Using ``func.Volume_Percipitation()``
        Volume_Runoff : float
            Volume of runoff that enter reservoir from watershed in m**3
        Volume_groundwater : float
            volume that enters from groundwater in m**3
        Volume_evaporation : float
            volume of water that vape from reservoir through time in m**3
        Volume_Wier : float
            The volume of water discharged from the tank. When overflow is measured, this can be determined with good accuracy.
            For most tanks, it is enough to use the appropriate overflow formula with its geometry in m**3
        Volume_infiltration : float
            volume of water that penetrate and seepage in m^3 Can Be Calculated Using ``func.Volume_infiltration()``
        Volume_Use : float
            volume of water that release and use in downstream with diffrent purposes in m^3
        
        Returns
        -------
        remained_water_volume_at_the_end_of_current_step : float
            volume of water that remain in the reservoir at the end of the time
        """

        
        return water_volume + (volume_runoff + volume_groundwater + precipitation_volume) - (
            volume_evaporation + volume_wier + volume_infiltration + volume_use)