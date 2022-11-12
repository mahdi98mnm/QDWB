


class E_free_water : 

     # init method or constructor 
    def __init__(self,
        solar_or_shortwave_radiation : float,
        method_free_water: str,
        tmean : float,
        delta : float,
        gamma : float,
        latent_heat_of_vaporization : float,
        water_area_of_a_lake_or_reservoir : float,
        wind_speed_at_2m : float,
        e_s : float,
        e_a : float
    ):
        self.solar_or_shortwave_radiation = solar_or_shortwave_radiation
        self.method_free_water = method_free_water
        self.tmean = tmean
        self.delta = delta
        self.gamma = gamma
        self.latent_heat_of_vaporization = latent_heat_of_vaporization
        self.water_area_of_a_lake_or_reservoir = water_area_of_a_lake_or_reservoir
        self.wind_speed_at_2m = wind_speed_at_2m
        self.e_s = e_s
        self.e_a = e_a
        
        
    # Sample Method 
    def based_on_radiation(
        solar_or_shortwave_radiation : float,
        method_free_water: str,
        tmean : float
    )-> float:
    
        """
        Description
        -----------
        calculate Evaporation from the free surface of water - eq 8 & 9
        ----------
        solar_or_shortwave_radiation : float
            Solar or shortwave radiation in MJ/m**2/day
        method_free_water : str 
            method for calculate evaporation from the free surface of water:
                Jensen or Stuart (for based_on_radiation)
                Harbeck or Shuttleworth (for based_on_wind_speed_and_vapor_pressure)
        tmean : float
            Mean Daily Temperature [°C]

        Returns
        -------
        E_free_water : float
            Evaporation from the free surface of water in milimeter/day
        """
        R_S = solar_or_shortwave_radiation

        if method_free_water == 'Jensen':
            E = 0.03523 * R_S * ((0.014 * tmean) - 0.37) 
        elif method_free_water == 'Stuart':
            E = 0.03495 * R_S * ((0.0082 * tmean) - 0.19)

        return E


    def making(
        delta : float,
        gamma : float,
        solar_or_shortwave_radiation : float,
        latent_heat_of_vaporization : float
    )-> float:
    
        """
        Description
        -----------
        calculate Evaporation from the free surface of water - eq 7
        ----------
        delta : float
            Slope Vapour Pressure Curve [kPa °C-1].
        gamma : float
            Psychrometric Constant [kPa °C-1].
        solar_or_shortwave_radiation : float
            Solar or shortwave radiation in MJ/m**2/day
        latent_heat_of_vaporization : float
            latent heat of vaporization in J/kg

        Returns
        -------
        E_free_water : float
            Evaporation from the free surface of water in milimeter/day
        """
        R_S = solar_or_shortwave_radiation
        
        return 52.6 * (delta / (delta + gamma)) * (R_S / latent_heat_of_vaporization) - 0.12 


    def based_on_wind_speed_and_vapor_pressure(
        method_free_water: str,
        water_area_of_a_lake_or_reservoir : float,
        wind_speed_at_2m : float,
        e_s : float,
        e_a : float
    )-> float:
    
        """
        Description
        -----------
        calculate Evaporation from the free surface of water - eq 4 & 5
        ----------

        method_free_water : str 
            method for calculate evaporation from the free surface of water:
                Jensen or Stuart (for based_on_radiation)
                Harbeck or Shuttleworth (for based_on_wind_speed_and_vapor_pressure)
        water_area_of_a_lake_or_reservoir : float
            water area of a lake or reservoir in meter**2
        wind_speed_at_2m : float
            Wind speed at 2m above ground surface in meter / second
        es : float
            Saturation Vapour Pressure [kPa].
        ea : float
            Actual Vapour Pressure [kPa]

        Returns
        -------
        E_free_water : float
            Evaporation from the free surface of water in milimeter/day
        """
        
        e_s_minus_e_a = e_s - e_a

        
        if method_free_water == 'Harbeck' :
            E = 2.909 * (water_area_of_a_lake_or_reservoir**(-0.05)) * wind_speed_at_2m * e_s_minus_e_a
        elif method_free_water == 'Shuttleworth' :
            E = 3.623 * (water_area_of_a_lake_or_reservoir**(-0.066)) * wind_speed_at_2m * e_s_minus_e_a
        

        return E