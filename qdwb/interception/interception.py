
from check import *
from asset import *

class interception :


    def __init__(self,
        type_of_basin_canopy : str,
        precipitation : float,
        is_growing_season : bool
    ):

        self.type_of_basin_canopy = type_of_basin_canopy
        self.precipitation = precipitation
        self.is_growing_season = is_growing_season



    def bucket(
        type_of_basin_canopy : str,
        precipitation : float,
        is_growing_season : bool
    )-> float :
    
        """
        Description
        -----------
        calculate interception from precipitation value and type of basin canopy
        **reference**based on researches of alizade (1391) & fasihi payan name

        Parameters
        -----------
        type_of_basin_canopy : str
            type_of_basin_canopy include : ['Forest&Mixed' , 'Evergreen_Forest' , 'Other']

        precipitation : float
            precipitation : zero or postive value in mm

        is_growing_season : bool
            is_growing_season include :  [True : 'growing' , False : 'none growing']

        Returns
        -------
        interception : float
            interception in mm
        """
        
    
        check_precipitation(precipitation = precipitation)
    

        if (type_of_basin_canopy == 'Forest&Mixed') and (is_growing_season == True)  :
            interception = 0.06 * precipitation
            
        elif (type_of_basin_canopy == 'Forest&Mixed') and (is_growing_season == False) :
            interception = 0.03 * precipitation
            
        elif type_of_basin_canopy == 'Evergreen_Forest' :
            interception = 0.1 * precipitation

        elif type_of_basin_canopy == 'Other' :
            interception = 0

        else :
            raise ValueError(f'enter correct type_of_basin_canopy and { type_of_basin_canopy} is not defined')
                        
            
        return(interception)
    


    def gash(
        total_precipitation_of_day : float,
        canopy_storage_capacity : float,
        canopy_cover : float,
        evaporation_to_rainfall_ratio: float,
        trunk_storage_capacity : float,
        stem_flow: float
    )-> float:
        
        """
        Description
        -------------------------
        calculate interception by Gash mathod 
        **reference**based on researches of Gash(1995):
        SWB Version 2.0—A ,page :27 & 28 ,
        A Modified Gash Model for Estimating Rainfall Interception
        Loss of Forest Using Remote Sensing Observations at
        Regional Scale_ Yaokui Cui  and Li Jia _2014
        parameters
        -------------------------
        type input :
            total_precipitation_of_day :float
            saturated_precipitation : float
            ratio_of_trunk_Storage_Capacity_to_stem_flow : float
            canopy_cover : float
            evaporation_to_rainfall_ratio : float
            trunk_Storage_Capacity : float 
        type output :
        interception : float
        ------------------------
        unit:
        total_precipitation_of_day : inch
            saturated_precipitation : inch
            ratio_of_trunk_Storage_Capacity_to_stem_flow : constant value
            canopy_cover :  dimentionless
            Evaporation_to_Rainfall_Ratio : dimentionless
            trunk_Storage_Capacity : constant value 
            interception : inch

        """  
        sp = saturated_precipitation (
            canopy_storage_capacity = canopy_storage_capacity,
            canopy_cover = canopy_cover,
            evaporation_to_rainfall_ratio = evaporation_to_rainfall_ratio
        )
        ratio = ratio_of_trunk_storage_capacity_to_stem_flow (
            trunk_storage_capacity = trunk_storage_capacity,
            stem_flow = stem_flow
        )
        
        check_precipitation(precipitation = total_precipitation_of_day)

        check_evaporation_to_rainfall_ratio(evaporation_to_rainfall_ratio = evaporation_to_rainfall_ratio)
        
        if total_precipitation_of_day < sp :
            interception = canopy_cover * total_precipitation_of_day
            
        elif ( total_precipitation_of_day >= sp and total_precipitation_of_day <= ratio):
            interception = (canopy_cover * sp) + (canopy_cover * evaporation_to_rainfall_ratio * (total_precipitation_of_day - sp)) + (stem_flow * total_precipitation_of_day)

        elif (total_precipitation_of_day >= sp and total_precipitation_of_day > ratio):
            interception = (canopy_cover * sp) + (canopy_cover * evaporation_to_rainfall_ratio * (total_precipitation_of_day - sp)) + trunk_storage_capacity

        return(interception)