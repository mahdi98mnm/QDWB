from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
from check import *
from global_variable import *
from datetime import date

class ReferenceEvapotranspiration :
    
    def __init__(self,
        tmean : float,
        tmin : float = None,
        tmax : float = None,
        ra : float = None,
        delta : float = None,
        rn : float = None,
        G : float = None,
        gamma : float = None,
        u2 : float = None,
        es : float = None,
        ea : float = None
    ):
        self.tmean = tmean
        self.tmin = tmin
        self.tmax = tmax
        self.ra = ra
        self.delta = delta
        self.rn = rn
        self.G = G
        self.gamma = gamma
        self.u2 = u2
        self.es = es
        self.ea = ea
        
        
    
    def hargreaves_samani(
        tmin : float,
        tmax : float,
        tmean : float,
        ra : float
    ) -> float:
        
        """
        Description
        -----------
        Estimate Reference Crop Evapotranspiration (ETo) Using the Hargreaves and Samani Method.
        **Reference**: Based on Equation 4 in Hargreaves and Samani (1985).
        
        Parameters
        ----------
        tmin : float
            Minimum Daily Temperature [°C]
        
        tmax : float
            Maximum Daily Temperature [°C]
        
        tmean : float
            Mean Daily Temperature [°C]
        
        ra : float
            Extraterrestrial Radiation [mm day-1]
            
        Returns
        -------
        ETo : float
            Reference Crop Evapotranspiration [mm/day]
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
        
        check_between(
            a=ra,
            min=0,
            max=SOLAR_CONSTANT * 24 * 60 * 0.408,
            name="Extraterrestrial Radiation"
        )
        
        return 0.0023 * (tmean + 17.8) * (tmax - tmin) ** 0.5 * ra
    
    
    def fao56_penman_monteith(
        delta : float,
        rn : float,
        G : float,
        gamma : float,
        tmean : float,
        u2 : float,
        es : float,
        ea : float
    ) -> float:
        
        """
        Description
        -----------
        Estimate reference evapotranspiration (ETo) from a hypothetical
        short grass reference surface using the FAO-56 Penman-Monteith equation.
        **Reference**: Based on equation 6 in Allen et al (1998).
        
        Parameters
        ----------
        
        rn : float
            Net Radiation at Crop Surface [MJ m-2 day-1].
        
        G : float
            Soil Heat Flux Density (G) [MJ m-2 day-1]
            
        tmean : float
            Mean Daily Air Temperature At 2m Height [°C]
        
        u2 : float
            Wind Speed at 2m Height [m s-1].
            
        es : float
            Saturation Vapour Pressure [kPa].
        
        ea : float
            Actual Vapour Pressure [kPa]
        
        delta : float
            Slope Vapour Pressure Curve [kPa °C-1].
            
        gamma : float
            Psychrometric Constant [kPa °C-1].
            
        Returns
        -------
        ETo : float
            Reference Evapotranspiration [mm day-1]
        """
        
        A = 0.408 * delta * (rn - G)
        B = gamma * (900 / (tmean + 273)) * u2 * (es - ea)
        C = delta + gamma * (1 + 0.34 * u2)
        
        return (A + B) / C



class EvaporationFromFreeWaterSurface :


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



class PotentialEvapotranspiration :


    def __init__(self,
        crop_coefficient_mid : float,
        crop_coefficient_end : float,
        crop_coefficient_ini : float = None,
        RH_min : float = None,
        maximum_crop_height : float = None,
        wind_speed_at_2m : float = None,
        length_ini_crop : int = None,
        length_dev_crop : int = None,
        length_mid_crop : int = None,
        length_late_crop : int = None,
        plant_date : str = None,
        modeling_date : str = None
    ):
        self.crop_coefficient_mid = crop_coefficient_mid
        self.crop_coefficient_end = crop_coefficient_end
        self.crop_coefficient_ini = crop_coefficient_ini
        self.RH_min = RH_min
        self.maximum_crop_height = maximum_crop_height
        self.wind_speed_at_2m = wind_speed_at_2m
        self.length_ini_crop = length_ini_crop
        self.length_dev_crop = length_dev_crop
        self.length_mid_crop = length_mid_crop
        self.length_late_crop = length_late_crop
        self.plant_date = plant_date
        self.modeling_date = modeling_date
    



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


    def calculate_single_crop_coefficient_for_linear_changes_steps(
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
    


class ActualEvapotranspiration :


    def __init__(self,
        moisture_reduction_function : float = None,
        crop_coefficient : float = None,
        crop_cover : float = None,
        reference_crop_evapotranspiration : float = None,
        ratio_of_actual_evaporable_water_to_total_evaporable_water : float = None,
        evaporation_noncovered_areas : float = None,
        evapotranspiration_covered_areas : float = None
    ):
        self.moisture_reduction_function = moisture_reduction_function
        self.crop_coefficient = crop_coefficient
        self.crop_cover = crop_cover
        self.reference_crop_evapotranspiration = reference_crop_evapotranspiration
        self.ratio_of_actual_evaporable_water_to_total_evaporable_water = ratio_of_actual_evaporable_water_to_total_evaporable_water
        self.evaporation_noncovered_areas = evaporation_noncovered_areas
        self.evapotranspiration_covered_areas = evapotranspiration_covered_areas



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

