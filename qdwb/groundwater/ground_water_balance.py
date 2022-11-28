


class GroundWaterBalance :


    def __init__(self,
        deep_perculation: float,
        entrance_groundwater: float,
        outlet_groundwater: float,
        evaporation_from_groundwater: float,
        penetration_from_free_surface_water: float,
        penetration_from_alluvial_fan: float,
        infiltration_by_artificial_feeding_projects: float,
        rate_of_water_leakage_from_underground_water_to_surface_water: float,
        withdrawal_from_springs: float,
        withdrawal_from_aqueducts: float,
        withdrawal_from_wells: float,
        R_fg: float,
        depth_of_undergroundwater: float,
        discharge_from_the_spring_at_time_i: float,
        discharge_from_the_spring_at_time_i1: float
    ):
        
        self.deep_perculation = deep_perculation
        self.entrance_groundwater = entrance_groundwater
        self.outlet_groundwater = outlet_groundwater
        self.evaporation_from_groundwater = evaporation_from_groundwater
        self.penetration_from_free_surface_water = penetration_from_free_surface_water
        self.penetration_from_alluvial_fan = penetration_from_alluvial_fan
        self.infiltration_by_artificial_feeding_projects = infiltration_by_artificial_feeding_projects
        self.rate_of_water_leakage_from_underground_water_to_surface_water = rate_of_water_leakage_from_underground_water_to_surface_water
        self.withdrawal_from_springs = withdrawal_from_springs
        self.withdrawal_from_aqueducts = withdrawal_from_aqueducts
        self.withdrawal_from_wells = withdrawal_from_wells
        self.R_fg = R_fg
        self.depth_of_undergroundwater = depth_of_undergroundwater
        self.discharge_from_the_spring_at_time_i = discharge_from_the_spring_at_time_i
        self.discharge_from_the_spring_at_time_i1 = discharge_from_the_spring_at_time_i1
    

    def ground_water_balance(
        deep_perculation: float,
        entrance_groundwater: float,
        outlet_groundwater: float,
        evaporation_from_groundwater: float,
        penetration_from_free_surface_water: float,
        penetration_from_alluvial_fan: float,
        infiltration_by_artificial_feeding_projects: float,
        rate_of_water_leakage_from_underground_water_to_surface_water: float,
        withdrawal_from_springs: float,
        withdrawal_from_aqueducts: float,
        withdrawal_from_wells: float,
        R_fg: float
    ) -> float:
        """
        Description
        -----------
        Calculation Ground Water Blance By Class GroundWaterBalance
    
        Parameters
        ----------

        deep_perculation : float
            Deep perculation caused by rain in m^3
    
        entrance_groundwater : float
            Entrance to Ground water in m^3
        
        outlet_groundwater : float
            Exit from underground water in m^3
        
        evaporation_from_groundwater : float
            Evaporation from groundwater in m^3
        
        penetration_from_free_surface_water : float
            Deep perculation from the free surface of water in m^3
        
        penetration_from_alluvial_fan : float
            Deep perculation in the alluvial fan in m^3

        infiltration_by_artificial_feeding_projects : float
            Deep perculation by artificial feeding projects in m^3
        
        rate_of_water_leakage_from_underground_water_to_surface_water : float
            The rate of water leakage from underground water to surface water in m^3
        
        withdrawal_from_springs : float
            Withdrawal from underground water by spring in m^3

        withdrawal_from_aqueducts: float
            Withdrawal from underground water by aqueducts in m^3

        withdrawal_from_wells: float
            Withdrawal from underground water by wells in m^3

        R_fg: float
            Return water to underground watr sources in m^3
        
        
        Returns
        -------
        delta_Storage_ground_water : float
            delta_Storage_ground_water in m^3
    
        """

        delta_Sg = (deep_perculation + (entrance_groundwater - outlet_groundwater) + R_fg -
                    evaporation_from_groundwater + penetration_from_free_surface_water + penetration_from_alluvial_fan +
                    infiltration_by_artificial_feeding_projects - rate_of_water_leakage_from_underground_water_to_surface_water -
                    (withdrawal_from_springs + withdrawal_from_wells + withdrawal_from_aqueducts))
        
        return delta_Sg
            