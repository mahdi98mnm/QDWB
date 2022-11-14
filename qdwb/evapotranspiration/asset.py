from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math
import datetime
from calendar import monthrange
from check import *
from global_variable import *

def mean_temperature_max_min(
    tmax : float,
    tmin : float
) -> float:
    
    """
    Description
    -----------
    calculate Mean Temperature With Tmax and Tmin - eq 9 FAO56
    ----------
    tmax : float
        Maximum Temperature in celsius
    tmin : float
        Minimum Temperature in celsius
    
    Returns
    -------
    Mean Temperature : float
        Mean Temperature in celsius
    """
    check_greater_than(
            a=tmin,
            a_name="Tmin",
            b=tmax,
            b_name="Tmax"
    )
    
    return (tmax + tmin)/2



def slope_vapour_pressure_curve_with_maen_temperature(
    tmean : float
    )-> float:


    """
    Description
    -----------
    calculate Slope Vapour Pressure Curve With Maen Temperature - eq 13 FAO56
    ----------
    tmean : float
        Mean Daily Temperature [°C]

    Returns
    -------
    Slope Vapour Pressure Curve : float
        Slope Vapour Pressure Curve in Kilo pascal per celsius
    """
    
    
    return 4098 * (0.6108 * math.exp((17.27 * tmean) / (tmean + 237.3))) / ((tmean + 237.3)**2)



def pressure_with_altitudes(
    altitude : float
) -> float:
    
    """
    Description
    -----------
    calculate pressure with Altitudes - eq 7 FAO56
    ----------
    altitude : float
        Height in meter
    
    Returns
    -------
    Pressure : float
        pressure in Kilo pascal
    """
    
    return 101.3 * ((293 - (0.0065 * altitude))/293)**5.26



def psychrometric_constant_with_altitudes(
    pressure : float
) -> float:
    
    """
    Description
    -----------
    calculate Psychrometric constant with Altitudes - eq 8 FAO56
    ----------
    Pressure : float
        pressure in Kilo pascal
    
    Returns
    -------
    Psychrometric constant : float
        Psychrometric constant in Kilo pascal per celsius
    """

    return 0.665 * (10**-3) * pressure



def inverse_relative_distance_earth_sun(
    julian_date: int
) -> float:
    
    """
    Description
    -----------
    calculate Inverse Relative Distance Earth Sun With Julian Date - eq 23 FAO56
    ----------

    
    Julian Day : int
        Number of days of the year taking into account the leap year
   
    Returns
    -------
    inverse_relative_distance_earth_sun : float
        inverse relative distance earth sun in Radian
    """
        
    return 1 + (0.033 * math.cos((2 * math.pi * julian_date)/365))



def solar_declination(
    julian_date: int
) -> float:
    
    """
    Description
    -----------
    calculate Solar Declination With Julian Date - eq 24 FAO56
    ----------

    julian_date : int
        Number of days of the year taking into account the leap year
   
    Returns
    -------
    solar_declination : float
        solar_declination in Radian
    """
        
    return 0.409 * math.sin(((2 * math.pi * julian_date) / 365) - 1.39)



def sunset_hour_angle(
    latitude : float,
    solar_declination : float
) -> float:
    
    """
    Description
    -----------
    calculate Sunset Hour Angle With Latitude and Solar Declination - eq 25 FAO56
    ----------

    latitude: float
        latitude in Radian
    solar_declination : float
        solar_declination in Radian
   
    Returns
    -------
    sunset_hour_angle : float
        sunset hour angle in Radian
    """
        
    return math.acos(-math.tan(latitude) * math.tan(solar_declination))



def saturation_vapour_pressure_with_temperature(
    temperature : float
) -> float:
    
    """
    Description
    -----------
    calculate Saturation Vapour Pressure With Temperature - eq 11 FAO56
    ----------
    Temperature : float
        Temperature in celsius - tmean or tmax or tmin or any other temperature
   
    Returns
    -------
    Saturation Vapour Pressure : float
        Saturation Vapour Pressure in Kilo pascal
    """
    
    return 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))



def total_saturation_vapour_pressure(
    Saturated_vapor_pressure_at_maximum_temperature : float,
    Saturated_vapor_pressure_at_minimum_temperature : float
) -> float:
    
    """
    Description
    -----------
    calculate Total Saturation Vapour Pressure With max and min Temperature - eq 12 FAO56
    ----------

    Saturated_vapor_pressure_at_maximum_temperature : float
        Saturated_vapor_pressure_at_maximum_temperature in kilo pascal
    Saturated_vapor_pressure_at_minimum_temperature : float
        Saturated_vapor_pressure_at_minimum_temperature  in kilo pascal

    Returns
    -------
    Total Saturation Vapour Pressure : float
        Total Saturation Vapour Pressure in Kilo pascal
    """
    

    return (Saturated_vapor_pressure_at_maximum_temperature + Saturated_vapor_pressure_at_minimum_temperature) / 2



def maximum_possible_sunshine_duration_in_a_day(
    sunset_hour_angle : float
) -> float:
    
    """
    Description
    -----------
    calculate maximum possible sunshine duration in a day - eq 34 FAO56
    ----------
    
    sunset_hour_angle : float
        sunset hour angle in Radian
   
    Returns
    -------
    maximum_possible_sunshine_duration_in_a_day : float
        maximum possible sunshine duration in a day in hours
    """
        
    return (24 / math.pi) * sunset_hour_angle



def number_of_days_in_month(
    standard_date_in_gregorian: str
) -> int:
    
    """
    Description
    -----------
    Calculate the number of days in a month - https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/
    ----------
    standard_date_in_gregorian : str
        Date with the specified standard
   
    Returns
    -------
    Number of days in month : int
        Number of days in month in Number
    """
        
    return monthrange(int(standard_date_in_gregorian[:4]), int(standard_date_in_gregorian[5:7]))[1]



def extraterrestrial_radiation(
    inverse_relative_distance_earth_sun : float,
    sunset_hour_angle : float,
    latitude : float,
    solar_declination : float
) -> float:
    
    """
    Description
    -----------
    calculate Extraterrestrial Radiation - eq 28 FAO56
    ----------

    inverse_relative_distance_earth_sun : float
        inverse relative distance earth sun in Radian
    sunset_hour_angle : float
        sunset hour angle in Radian
    latitude: float
        latitude in Radian
    solar_declination : float
        solar_declination in Radian

    Returns
    -------
    extraterrestrial_radiation : float
            extraterrestrial radiation in MJ/m**2/day
    """
    
    temp_1 = ((24 * 60 )/ math.pi) * SOLAR_CONSTANT * inverse_relative_distance_earth_sun

    temp_2 = sunset_hour_angle * math.sin(latitude) * math.sin(solar_declination)

    temp_3 = math.cos(latitude)* math.cos(solar_declination) * math.sin(sunset_hour_angle)

    return temp_1 * (temp_2 + temp_3)



class SolarOrShortwaveRadiation  :
   
    # init method or constructor 
    def __init__(self,
        extraterrestrial_radiation : float,
        maximum_possible_sunshine_duration_in_a_day : float = None,
        Actual_duration_of_sunshine_in_a_day : float = None,
        Monthly_average_sunshine_duration : float = None,
        mode_data : str = None,
        Adjustment_coefficient_or_K_RS : float = None,
        tmax : float = None,
        tmin : float = None,
    ):
        self.extraterrestrial_radiation = extraterrestrial_radiation
        self.maximum_possible_sunshine_duration_in_a_day = maximum_possible_sunshine_duration_in_a_day
        self.Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day
        self.Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
        self.mode_data = mode_data
        self.Adjustment_coefficient_or_K_RS= Adjustment_coefficient_or_K_RS
        
        
    # Sample Method 
    def Angstrom (
        extraterrestrial_radiation : float,
        mode_data : str,
        maximum_possible_sunshine_duration_in_a_day : float,
        standard_date_in_gregorian : str,
        Actual_duration_of_sunshine_in_a_day : float = None, 
        Monthly_average_sunshine_duration : float = None
    )-> float:
    
        """
        Description
        -----------
        calculate Solar or shortwave radiation with Relative sunshine duration - eq 35 FAO56
        ----------

        extraterrestrial_radiation : float
            extraterrestrial radiation in MJ/m**2/day
        mode_data : str 
            monthly or daily
        maximum_possible_sunshine_duration_in_a_day : float
            maximum possible sunshine duration in a day in hours
        standard_date_in_gregorian : str
            Date with the specified standard
        Actual_duration_of_sunshine_in_a_day : float
            Actual duration of sunshine in a day in hour
        Monthly_average_sunshine_duration : float
            Monthly average sunshine duration in hour per day
        

        Returns
        -------
        Solar or shortwave radiation : float
            Solar or shortwave radiation in MJ/m**2/day
        """
        if mode_data == 'monthly':
            if Monthly_average_sunshine_duration != None:
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration

            elif Monthly_average_sunshine_duration == None:
                Monthly_average_sunshine_duration = Actual_duration_of_sunshine_in_a_day / number_of_days_in_month(standard_date_in_gregorian = standard_date_in_gregorian)
            
        elif mode_data == 'daily':
            Monthly_average_sunshine_duration = Actual_duration_of_sunshine_in_a_day
        
        N = maximum_possible_sunshine_duration_in_a_day
        temp_1 = extraterrestrial_radiation

        return (0.25 + (0.5 * (Monthly_average_sunshine_duration / N ))) * temp_1
        
    
    def Hargreaves(
        extraterrestrial_radiation : float,
        tmax : float,
        tmin : float,
        Adjustment_coefficient_or_K_RS : float
    )-> float:
        
        """
        Description
        -----------
        calculate Solar or shortwave radiation with max and min Tempreture - eq 50 FAO56
        ----------

        extraterrestrial_radiation : float
            extraterrestrial radiation in MJ/m**2/day
        tmax : float
            Maximum Temperature in celsius
        tmin : float
            Minimum Temperature in celsius
        Adjustment_coefficient_or_K_RS : float
            Adjustment coefficient in C**-0.5 -- between 0.16 to 0.19
                for interior locations, where land mass dominates and air masses are not strongly
                influenced by a large water body, kRs ≅ 0.16;
                for coastal locations, situated on or adjacent to the coast of a large land mass and where
                air masses are influenced by a nearby water body, kRs ≅ 0.19

        Returns
        -------
        Solar or shortwave radiation : float
            Solar or shortwave radiation in MJ/m**2/day
        """
        temp_1 = extraterrestrial_radiation


        return Adjustment_coefficient_or_K_RS * math.sqrt(tmax - tmin) * temp_1



def net_solar_or_shortwave_radiation(
    solar_or_shortwave_radiation : float
) -> float:
    
    """
    Description
    -----------
    calculate Net solar or shortwave radiation with Solar or shortwave radiation - eq 38 FAO56
    ----------

    solar_or_shortwave_radiation : float
        Solar or shortwave radiation in MJ/m**2/day

    
    Returns
    -------
    net_solar_or_shortwave_radiation : float
        Net solar or shortwave radiation in MJ / m**2 /day
    """
    R_ns = 0.77 * solar_or_shortwave_radiation
        
    return R_ns



class ActualVapourPressure:
   
    # init method or constructor 
    def __init__(self,
    tdew : float  = None,
    tmax : float = None,
    tmin : float = None,
    tmean : float = None,
    RH_max : float =None,
    RH_min : float = None,
    RH_mean : float = None,
    twet : float = None,
    tdry : float = None,
    a_psy : float = None
    ):
        self.tdew = tdew
        self.tmax = tmax
        self.tmin = tmin
        self.tmean= tmean
        self.RH_max= RH_max
        self.RH_min= RH_min
        self.RH_mean=RH_mean
        self.twet = twet
        self.tdry = tdry
        self.a_psy = a_psy


   
    # Sample Method 
    def dew(
        tdew:float
    )-> float:
    
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Dewpoint temperature - eq 14 FAO56
        ----------
        tdew : float
            Dewpoint temperature in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        
        
        return saturation_vapour_pressure_with_temperature(temperature = tdew)
    
    def RH_and_T_max_min(
        tmax:float,
        tmin:float,
        RH_max:float,
        RH_min:float
        )-> float:
        
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Maximum relative humidity and Minimum relative humidity and 
        Maximum Tempreture and Minimum Tempreture - eq 17 FAO56
        ----------
        tmax : float
            Maximum Temperature in celsius
        tmin : float
            Minimum Temperature in celsius
        RH_max : float
            Maximum relative humidity and Minimum relative humidity in percent
        RH_min : float
            Maximum Tempreture and Minimum Tempreture in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        
        return ((saturation_vapour_pressure_with_temperature(temperature = tmin) * (
            RH_max/100)) + (saturation_vapour_pressure_with_temperature(temperature = tmax) * (RH_min/100))) / 2
    
    def RH_max_and_T_min(
        tmin : float,
        RH_max : float
        )-> float:
        
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Maximum relative humidity and Minimum Tempreture - eq 18 FAO56
        ----------

        tmin : float
            Minimum Temperature in celsius
        RH_max : float
            Maximum relative humidity and Minimum relative humidity in percent

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """

        return saturation_vapour_pressure_with_temperature(temperature = tmin) * (RH_max/100)
    

    def RH_mean_T_max_min(
        tmax,
        tmin,
        RH_max = None,
        RH_min = None,
        RH_mean = None
        )-> float:
        
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Mean relative humidity and Maximum Tempreture and Minimum Tempreture - eq 19 FAO56
        ----------

        tmax : float
            Maximum Temperature in celsius
        tmin : float
            Minimum Temperature in celsius
        RH_max : float
            Maximum relative humidity and Minimum relative humidity in percent
        RH_min : float
            Maximum Tempreture and Minimum Tempreture in celsius
        RH_mean : float
            Mean relative humidity in percent
        

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """

        if RH_mean == None :
            RH_mean = (RH_max + RH_min) / 2


        return ((saturation_vapour_pressure_with_temperature(temperature = tmax) + saturation_vapour_pressure_with_temperature(temperature = tmin))/2) * (RH_mean/100)
    

    def T_wet_T_dry(
        twet : float,
        tdry : float,
        a_psy : float,
        altitude : float
        )-> float:

        """
        Description
        -----------
        calculate Actual Vapour Pressure With Wet Tempreture and Dry Tempreture and Coefficient of psychrometer - eq 15 and 16 FAO56
        ----------

        twet : float
            Wet Tempreture in celsius
        tdry : float
            Dry Tempreture in celsius
        a_psy : float
            Coefficient of psychrometer in celsius**-1
            Coefficient of psychrometer for ventilated (Asmann type) psychrometers movement of some 5 m/s = 0.000662
            Coefficient of psychrometer for natural ventilated psychrometers (about 1 m/s)= 0.0008
            Coefficient of psychrometer for non-ventilated psychrometers installed indoors = 0.0012
        altitude : float
            Height in meter

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        gama_psy = a_psy * pressure_with_altitudes(altitude = altitude)

        return saturation_vapour_pressure_with_temperature(temperature = twet) - (gama_psy * (tdry - twet))



def clear_sky_solar_or_clear_sky_shortwave_radiation(
    extraterrestrial_radiation : float,
    altitude : float = None
) -> float:
    
    """
    Description
    -----------
    calculate Clear-sky solar or clear-sky shortwave radiation with Extraterrestrial radiation and Altitude - eq 37 FAO56
    ----------

    extraterrestrial_radiation : float
        extraterrestrial radiation in MJ/m**2/day
    altitude : float
        Altitude in meter - station elevation above sea level 
   
    Returns
    -------
    Clear-sky solar or clear-sky shortwave radiation : float
        Clear-sky solar or clear-sky shortwave radiation in MJ / m**2 /day
    """
    if altitude == None :
        R_SO = 0.75 * extraterrestrial_radiation

    else:
        R_SO = (0.75 + (2 * (10**-5) * altitude)) * extraterrestrial_radiation

    return R_SO

def net_longwave_radiation(
    tmax_kelvin : float,
    tmin_kelvin : float,
    actual_vapour_pressure : float,
    solar_or_shortwave_radiation : float,
    clear_sky_solar_or_clear_sky_shortwave_radiation : float
) -> float:

    """
    Description
    -----------
    calculate Net longwave radiation with Tempreture and Actual Vapour Pressure - eq 39 FAO56
    ----------
    
    tmax_kelvin : float
        Maximum Temperature in kelvin
    tmin_kelvin : float
        Minimum Temperature in kelvin 
    actual_vapour_pressure : float
        actual vapour pressure in Kilo pascal
    solar_or_shortwave_radiation : float
        solar or shortwave radiation in MJ/m**2/day
    clear_sky_solar_or_clear_sky_shortwave_radiation : float
        Clear-sky solar or clear-sky shortwave radiation in MJ / m**2 /day

   
    Returns
    -------
    net_longwave_radiation : float
        net longwave radiation in MJ / m**2 /day
    """

    temp_1 = STEFAN_BOLTZMANN_CONSTANT * (((tmax_kelvin**4) + (tmin_kelvin**4)) / 2 )
    temp_2 = 0.34 - (0.14 * math.sqrt(actual_vapour_pressure))
    temp_3 = (1.35 * (solar_or_shortwave_radiation / clear_sky_solar_or_clear_sky_shortwave_radiation)) - 0.35

    R_nl = temp_1 * temp_2 * temp_3


    return R_nl



def net_radiation_at_the_crop_surface(
    net_solar_or_shortwave_radiation : float,
    net_longwave_radiation : float
) -> float:

        """
        Description
        -----------
        calculate Net radiation at the crop surface with Net solar or shortwave radiation and Net longwave radiation - eq 40 FAO56
        ----------

        net_solar_or_shortwave_radiation : float
            net solar or shortwave radiation in MJ / m**2 /day
        net_longwave_radiation : float
            Net longwave radiation in MJ / m**2 /day

        Returns
        -------
        net_radiation_at_the_crop_surface : float
            net radiation at the crop surface in MJ / m**2 /day
        """
        R_ns = net_solar_or_shortwave_radiation
        R_nl = net_longwave_radiation


        return R_ns - R_nl



class SoilHeatFluxDensity :
   
    # init method or constructor 
    def __init__(
        self,
        soil_heat_capacity = None,
        air_temperature_at_previous_step = None,
        air_temperature_at_current_step = None,
        delta_time = None,
        effective_soil_depth = None,
        mean_air_temperature_of_previous_month = None,
        mean_air_temperature_of_next_month = None,
        mean_air_temperature_of_current_month = None,
        mode = None
    ):
        
        self.soil_heat_capacity = soil_heat_capacity
        self.air_temperature_at_previous_step = air_temperature_at_previous_step
        self.air_temperature_at_current_step = air_temperature_at_current_step
        self.delta_time = delta_time
        self.effective_soil_depth = effective_soil_depth
        self.mean_air_temperature_of_previous_month = mean_air_temperature_of_previous_month
        self.mean_air_temperature_of_next_month = mean_air_temperature_of_next_month
        self.mean_air_temperature_of_current_month = mean_air_temperature_of_current_month
        self.mode=mode

        
        # Sample Method 
    def With_Effective_soil_depth (
        soil_heat_capacity : float,
        air_temperature_at_previous_step : float,
        air_temperature_at_current_step : float,
        delta_time : float,
        effective_soil_depth : float 
    )-> float:


        """
    Description
    -----------
    calculate Soil_heat_flux_density with Effective soil depth - eq 41 FAO56
    ----------

    soil_heat_capacity : float
        soil heat capacity in MJ / m**3 / celsius
    air_temperature_at_previous_step : float 
        air temperature at previous step in celsius
    air_temperature_at_current_step : float
        air temperature at current step in celsius
    delta_time : float
        Length of time interval in day
    effective_soil_depth : float
        effective soil depth in meter
        
    Returns
    -------
    soil_heat_flux_density : float
        soil heat flux density in MJ / m**2 /day
    """
    
        return soil_heat_capacity * ((air_temperature_at_previous_step + air_temperature_at_current_step) / delta_time ) * effective_soil_depth


    def For_day_and_ten_day_periods (
    )-> float:
        """
    Description
    -----------
    calculate Soil_heat_flux_density for For day and ten-day periods - eq 43 & 44 FAO56
    ----------

    Returns
    -------
    soil_heat_flux_density : float
        soil heat flux density in MJ / m**2 /day
    """

        return 0


    def For_monthly_periods (
        mean_air_temperature_of_previous_month : float,
        mean_air_temperature_of_next_month = None,
        mean_air_temperature_of_current_month = None
    )-> float:

        """
    Description
    -----------
    calculate Soil_heat_flux_density with Effective soil depth - eq 41 FAO56
    ----------
    mean_air_temperature_of_previous_month : float 
        mean air temperature of previous month in celsius
    mean_air_temperature_of_next_month : float
        mean air temperature of next month in celsius
    mean_air_temperature_of_current_month : float
        mean air temperature of current month in celsius
        
    Returns
    -------
    soil_heat_flux_density : float
        soil heat flux density in MJ / m**2 /day
    """

        if mean_air_temperature_of_current_month == None :
            G = 0.07 * (mean_air_temperature_of_next_month - mean_air_temperature_of_previous_month)

        elif mean_air_temperature_of_next_month == None :
            G = 0.14 * (mean_air_temperature_of_current_month - mean_air_temperature_of_previous_month)

        return G
    

    def For_hourly_or_shorter_periods(
        mode: str,
        net_radiation_at_the_crop_surface : float
    )-> float:

        """
        Description
        -----------
        calculate Soil_heat_flux_density with Effective soil depth - eq 45 & 46 FAO56
        ----------
        mode : str 
            night or day
        net_radiation_at_the_crop_surface : float
            net radiation at the crop surface in MJ / m**2 /day
                
        Returns
        -------
        soil_heat_flux_density : float
            soil heat flux density in MJ / m**2 /day
        """
        if mode == 'day':
            G = 0.1 * net_radiation_at_the_crop_surface

        elif mode == 'night':
            G = 0.5 * net_radiation_at_the_crop_surface

        return G



def wind_speed_at_2m_above_ground_surface(
    altitude_at_which_wind_speed_is_measured : float, 
    measured_wind_speed : float
) -> float:

    """
    Description
    -----------
    calculate Wind speed at 2m above ground surface with Measured speed and height - eq 47 FAO56
    ----------
        
    altitude_at_which_wind_speed_is_measured : float
        Altitude at which wind speed is measured in meter
    measured_wind_speed : float 
        Measured wind speed in meter / second
            
    Returns
    -------
    wind_speed_at_2m_above_ground_surface : float
        wind speed at 2m above ground surface in meter / second
    """
        
    return measured_wind_speed * (4.87 / (math.log((67.8 *altitude_at_which_wind_speed_is_measured) - 5.42)))



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
