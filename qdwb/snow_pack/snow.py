from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

from check import *

class SnowPack :

    def __init__(self,
        tmax : float,
        tmin : float,
        tmean : float,
        u10 : float,
        esn : float,
        e2 : float
    ):
        self.tmax = tmax
        self.tmin = tmin
        self.tmean = tmean
        self.u10 = u10
        self.esn = esn
        self.e2 = e2




    def check_snow_fall_or_not(
        tmax : float,
        tmin : float,
        tmean : float
    ):

        """
        Description
        -----------
        Check snowfall.
        **Reference**: Based on Equation 1-2 in SWB Version 2.0 (2018).
        Parameters
        ----------
        tmax : float
            Maximum Daily Temperature [Degrees Celsius]

        tmin : float
            Minimum Daily Temperature [Degrees Celsius]

        tmean : float
            Mean Daily Temperature [Degrees Celsius]
            
        Returns
        -------
        p : A sentence about the precipitation is snow or rain & boolean parameter.
        """
        check_greater_than(
            a=tmin,
            a_name="Tmin",
            b=tmax,
            b_name="Tmax"
        )

        check_greater_than(
            a=tmean,
            a_name="Tmean",
            b=tmax,
            b_name="Tmax"
        )
        
        check_greater_than(
            a=tmin,
            a_name="Tmin",
            b=tmean,
            b_name="Tmean"
        )


        if (tmean - 1/3 * (tmax - tmin)) <= 0:
            
            return True
        else:
            
            return False




    def snow_melt(
        tmax : float,
    ) -> float:

        """
        Description
        -----------
        Calculate snow melting rate.
        **Reference**: Based on Equation 1-3 in SWB Version 2.0 (2018).
        Parameters
        ----------
        tmax : float
            Maximum Daily Temperature [Degrees Celsius]

        Returns
        -------
        M : float
        Snow melting rate [mm / day]
        """
        # Degree Day factor = 1.5 (mm/day.°c)
        DEGREE_DAY_FACTOR = 1.5

        check_maximum_temperature(tmax = tmax)

        return DEGREE_DAY_FACTOR * (tmax)



    def sublimation_snow_and_ice_surface(
        wind_speed_at_10m_above_ground_surface : float,
        saturated_vapor_pressure_at_snow_surface_temperature : float,
        steam_pressure_at_2m_above_snow_surface : float
    ) -> float:
        """
        Description
        -----------
        Calculate evaporation from snow and ice surfaces.
        **Reference**: Based on Equation 55-6 in Instructions for methods of calculating the balance of water resources(1393).
        Parameters
        ----------
        
        wind_speed_at_10m_above_ground_surface : float
            Average daily values of wind speed at a height of 10 meters above the snow surface [m / s]
        
        saturated_vapor_pressure_at_snow_surface_temperature : float
            Saturated vapor pressure corresponding to the temperature of the snow surface [Kpa]
        
        steam_pressure_at_2m_above_snow_surface : float
            steam pressure at a height of 2 meters above the snow surface [Kpa]

        Returns
        -------
        E : float
            Evaporation [mm / day]
        """

        return ((0.18 + 0.98 * wind_speed_at_10m_above_ground_surface) * (saturated_vapor_pressure_at_snow_surface_temperature - steam_pressure_at_2m_above_snow_surface))