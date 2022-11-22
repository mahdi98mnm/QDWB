
from constant import *


class SoilContent :

    def __init__(self,
        soil_water_content_of_evaporation_layer_at_previous_step: float,
        infiltration: float,
        evaporation: float,
        field_capacity_soil_water_content_of_evaporation_layer: float,
        permanent_wilting_point_soil_water_content_of_evaporation_layer: float,
        coverd : bool,
        infiltration_to_transpiration_layer: float,
        infiltration_to_transition_layer: float,
        field_capacity_soil_water_content_of_transpiration_layer: float,
        permanent_wilting_point_soil_water_content_of_transpiration_layer: float,
        soil_water_content_of_transpiration_layer_at_previous_step: float,
        stress_coefficient : float,
        infiltration_from_evaporation_to_transpiration_layer : float,
        infiltration_from_transpiration_to_transition_layer : float,
        transpiration: float,
        upward_flux_from_transition_to_transpiration_layer: float,
        upward_flux_from_transpiration_to_evaporation_layer: float,
        root_depth: float,
        MAD: float,
        field_capacity_soil_water_content_of_transition_layer: float,
        permanent_wilting_point_soil_water_content_of_transition_layer: float,
        soil_water_content_of_transition_layer_at_previous_step: float,
        deep_percolation: float,
        hydraulic_conductivity_of_transpiration_layer: float,
        hydraulic_conductivity_of_transition_layer: float
    ):
        self.soil_water_content_of_evaporation_layer_at_previous_step = soil_water_content_of_evaporation_layer_at_previous_step
        self.infiltration = infiltration
        self.evaporation = evaporation
        self.field_capacity_soil_water_content_of_evaporation_layer = field_capacity_soil_water_content_of_evaporation_layer
        self.permanent_wilting_point_soil_water_content_of_evaporation_layer = permanent_wilting_point_soil_water_content_of_evaporation_layer
        self.coverd = coverd
        self.infiltration_to_transpiration_layer = infiltration_to_transpiration_layer
        self.infiltration_to_transition_layer = infiltration_to_transition_layer
        self.field_capacity_soil_water_content_of_transpiration_layer = field_capacity_soil_water_content_of_transpiration_layer
        self.permanent_wilting_point_soil_water_content_of_transpiration_layer = permanent_wilting_point_soil_water_content_of_transpiration_layer
        self.soil_water_content_of_transpiration_layer_at_previous_step = soil_water_content_of_transpiration_layer_at_previous_step
        self.stress_coefficient = stress_coefficient
        self.infiltration_from_evaporation_to_transpiration_layer = infiltration_from_evaporation_to_transpiration_layer
        self.infiltration_from_transpiration_to_transition_layer = infiltration_from_transpiration_to_transition_layer
        self.transpiration = transpiration
        self.upward_flux_from_transition_to_transpiration_layer
        self.upward_flux_from_transpiration_to_evaporation_layer = upward_flux_from_transpiration_to_evaporation_layer
        self.root_depth = root_depth
        self.MAD = MAD
        self.field_capacity_soil_water_content_of_transition_layer = field_capacity_soil_water_content_of_transition_layer
        self.permanent_wilting_point_soil_water_content_of_transition_layer = permanent_wilting_point_soil_water_content_of_transition_layer
        self.soil_water_content_of_transition_layer_at_previous_step = soil_water_content_of_transition_layer_at_previous_step
        self.deep_percolation = deep_percolation
        self.hydraulic_conductivity_of_transpiration_layer = hydraulic_conductivity_of_transpiration_layer
        self.hydraulic_conductivity_of_transition_layer = hydraulic_conductivity_of_transition_layer


    def upward_flux(
        coverd: bool,
        field_capacity_soil_water_content_of_evaporation_layer: float,
        field_capacity_soil_water_content_of_transition_layer: float,
        permanent_wilting_point_soil_water_content_of_evaporation_layer: float,
        permanent_wilting_point_soil_water_content_of_transition_layer: float,
        soil_water_content_of_evaporation_layer_at_previous_step: float,
        soil_water_content_of_transition_layer_at_previous_step: float,
        hydraulic_conductivity_of_transition_layer: float,
        field_capacity_soil_water_content_of_transpiration_layer: float = None,
        permanent_wilting_point_soil_water_content_of_transpiration_layer: float = None,
        soil_water_content_of_transpiration_layer_at_previous_step: float = None,
        hydraulic_conductivity_of_transpiration_layer: float = None,
        root_depth: float = None
    ) -> float:

        """
        Description
        ------------
        calculating soil water content of trans layer
        ------------
        coverd: bool
            corved yes(True) or not coverd no(False)
        root_depth: float
            root depth in cm
        field_capacity_soil_water_content_of_evaporation_layer : float
            field capacity soil water content of evaporation layer in percent
        field_capacity_soil_water_content_of_transpiration_layer: float
            field capacity soil water content of transpiration layer in percent
        field_capacity_soil_water_content_of_transition_layer: float
            field capacity soil water content of transition layer in percent
        permanent_wilting_point_soil_water_content_of_evaporation_layer : float
            permanent wilting point soil water content of evaporation layer in percent
        permanent_wilting_point_soil_water_content_of_transpiration_layer: float
            permanent wilting point soil water content of transpiration layer in percent
        permanent_wilting_point_soil_water_content_of_transition_layer: float
            permanent wilting point soil water content of transition layer in percent
        soil_water_content_of_evaporation_layer_at_previous_step : float
            soil water content of evaporation layer at previous step in milimeter
        soil_water_content_of_transpiration_layer_at_previous_step: float
            soil water content of transpiration layer at previous step in milimeter
        soil_water_content_of_transition_layer_at_previous_step: float
            soil water content of transition layer at previous step in milimeter
        hydraulic_conductivity_of_transpiration_layer: float
            hydraulic conductivity of transpiration layer in milimeter per day
        hydraulic_conductivity_of_transition_layer: float
            hydraulic conductivity of transition layer in milimeter per day
        ------------
        Returns
        ------------
        upward_transpiration_to_evaporation: float
            upward flux from transpiration to evaporation layer in milimeter
        upward_transition_to_transpiration
            upward flux from transition to transpiration layer in milimeter
        upward_transition_to_evaporation
            upward flux from transition to evaporation layer in milimeter
        """


        evaporation_layer_soil_depth = soil_depth.get('evaporation_layer_covered')
        transition_layer_soil_depth = soil_depth.get('transition_layer_covered')

        temp_1_fc = (field_capacity_soil_water_content_of_evaporation_layer / 100) * (evaporation_layer_soil_depth * 10)
        temp_3_fc = (field_capacity_soil_water_content_of_transition_layer / 100) * (transition_layer_soil_depth * 10)

        temp_1_pwp = (permanent_wilting_point_soil_water_content_of_evaporation_layer / 100) * (evaporation_layer_soil_depth * 10)
        temp_3_pwp = (permanent_wilting_point_soil_water_content_of_transition_layer / 100) * (transition_layer_soil_depth * 10)

        t1 = (soil_water_content_of_evaporation_layer_at_previous_step - temp_1_pwp) / (temp_1_fc - temp_1_pwp)
        t3 = (soil_water_content_of_transition_layer_at_previous_step - temp_3_pwp) / (temp_3_fc - temp_3_pwp)

        

        if coverd == True :
            if soil_water_content_of_transpiration_layer_at_previous_step >= soil_water_content_of_transition_layer_at_previous_step:
                upward_transition_to_transpiration = 0


            elif soil_water_content_of_evaporation_layer_at_previous_step >= soil_water_content_of_transpiration_layer_at_previous_step:
                upward_transpiration_to_evaporation = 0

            else:
                
                temp_2_fc = (field_capacity_soil_water_content_of_transpiration_layer / 100) * (root_depth * 10)
                

                
                temp_2_pwp = (permanent_wilting_point_soil_water_content_of_transpiration_layer / 100) * (root_depth * 10)
                

                
                t2 = (soil_water_content_of_transpiration_layer_at_previous_step - temp_2_pwp) / (temp_2_fc - temp_2_pwp)
                

                alpha_transpiration_to_evaporation = (t2 - t1)
                alpha_transition_to_transpiration = (t3 - t2)

                upward_transpiration_to_evaporation = alpha_transpiration_to_evaporation * hydraulic_conductivity_of_transpiration_layer
                upward_transition_to_transpiration = alpha_transition_to_transpiration * hydraulic_conductivity_of_transition_layer
                upward_transition_to_evaporation = None

        else:
            alpha_transition_to_evaporation = (t3 - t1)
            upward_transition_to_evaporation = alpha_transition_to_evaporation * hydraulic_conductivity_of_transition_layer
            upward_transition_to_transpiration = None
            upward_transpiration_to_evaporation = None


        return upward_transpiration_to_evaporation,upward_transition_to_transpiration,upward_transition_to_evaporation


    def evaporation_layer(
        soil_water_content_of_evaporation_layer_at_previous_step: float,
        infiltration: float,
        evaporation: float,
        field_capacity_soil_water_content_of_evaporation_layer: float,
        permanent_wilting_point_soil_water_content_of_evaporation_layer: float,
        coverd : bool,
        infiltration_to_transpiration_layer: float = 0,
        infiltration_to_transition_layer: float = 0
    ) -> float:
        """
        Description
        ------------
        calculating soil water content of evaporation layer
        ------------
        soil_water_content_of_evaporation_layer_at_previous_step: float
            soil water content of firts layer at previous step in milimeter
        infiltration: float
            infiltration in milimeter
        evaporation: float
            evaporation in milimeter
        field_capacity_soil_water_content_of_evaporation_layer: float
            field capacity soil water content of evaporation layer in percent
        permanent_wilting_point_soil_water_content_of_evaporation_layer: float
            permanent wilting point soil water content of evaporation layer in percent
        coverd: bool
            corved yes(True) or not coverd no(False)
        infiltration_to_transpiration_layer: float
            infiltration to transpiration layer in milimeter
        infiltration_to_transition_layer: float
            infiltration to transition layer in milimeter
        ------------
        Returns
        ------------
        
        soil_water_content_of_evaporation_layer: float
            soil water content of evaporation layer in milimeter
        """

        if coverd is True:
            evaporation_layer_soil_depth = soil_depth.get('evaporation_layer_covered')
            temp_1 = (soil_water_content_of_evaporation_layer_at_previous_step + infiltration - evaporation - infiltration_to_transpiration_layer)
        else:
            infiltration_to_transpiration_layer = 0
            evaporation_layer_soil_depth = soil_depth.get(
                'evaporation_layer_not_covered')
            temp_1 = (soil_water_content_of_evaporation_layer_at_previous_step + infiltration - evaporation - infiltration_to_transition_layer)


        temp_2 = (field_capacity_soil_water_content_of_evaporation_layer /100) * (evaporation_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_evaporation_layer / 100) * (evaporation_layer_soil_depth * 10)

        if temp_1 <= temp_3:
            temp_1 = temp_3
            evaporation = soil_water_content_of_evaporation_layer_at_previous_step - temp_3
            return temp_1

        elif temp_1 >= temp_2:
            if coverd is True:
                infiltration_to_transpiration_layer = temp_1 - temp_2
                temp_1 = temp_2
            else:
                infiltration_to_transition_layer = temp_1 - temp_2
                temp_1 = temp_2

            return temp_1

        else:
            return temp_1
    

    def transpiration_layer(
        coverd: bool,
        field_capacity_soil_water_content_of_transpiration_layer: float,
        permanent_wilting_point_soil_water_content_of_transpiration_layer: float,
        soil_water_content_of_transpiration_layer_at_previous_step: float,
        stress_coefficient : float,
        infiltration_from_evaporation_to_transpiration_layer : float = 0,
        infiltration_from_transpiration_to_transition_layer : float = 0,
        transpiration: float = 0,
        upward_flux_from_transition_to_transpiration_layer: float = 0,
        upward_flux_from_transpiration_to_evaporation_layer: float = 0,
        root_depth: float = 0,
        MAD: float = 0
    ) -> float:
        """
        Description
        ------------
        calculating soil water content of transpiration layer
        ------------
        coverd: bool
            corved yes(True) or not coverd no(False)
        field_capacity_soil_water_content_of_transpiration_layer: float
            feild capacity soil water content of transpiration layer in percent
        permanent_wilting_point_soil_water_content_of_transpiration_layer: float
            permanent wilting point soil water content of transpiration layer in percent
        soil_water_content_of_transpiration_layer_at_previous_step: float
            soil water content of transpiration layer at previous step in milimeter
        stress_coefficient : float
            deficit irrigation - between 0 - 1 in unitless
        infiltration_from_evaporation_to_transpiration_layer : float
            infiltration from evaporation to transpiration layer in milimeter
        infiltration_from_transpiration_to_transition_layer : float
            infiltration from transpiration to transition layer in milimeter
        transpiration: float
            transpiration in milimeter
        upward_flux_from_transition_to_transpiration_layer: float
            upward flux from transition to transpiration layer in milimeter
        upward_flux_from_transpiration_to_evaporation_layer: float
            upward flux from transpiration to evaporation layer in milimeter
        root_depth: float
            root depth in cm
        MAD: float
            MAD(Maximum Allowable Depletion) between 0 to 1
        ------------
        Returns
        ------------
        soil_water_content_of_transpiration_layer: float
            soil water content of transpiration layer in milimeter
        """
        
        

        if coverd is False:
            return "transpiration layer is not defined"
        else:
            if infiltration_from_evaporation_to_transpiration_layer > 0:
                upward_flux_from_transpiration_to_evaporation_layer = 0

            if infiltration_from_transpiration_to_transition_layer > 0:
                upward_flux_from_transition_to_transpiration_layer = 0
            
            if infiltration_from_transpiration_to_transition_layer > 0:
                upward_flux_from_transpiration_to_evaporation_layer = 0
            
            transpiration_layer_soil_depth = root_depth

            temp_1 = (soil_water_content_of_transpiration_layer_at_previous_step + infiltration_from_evaporation_to_transpiration_layer + upward_flux_from_transition_to_transpiration_layer
                    - transpiration - upward_flux_from_transpiration_to_evaporation_layer - infiltration_from_transpiration_to_transition_layer)

            temp_2 = (field_capacity_soil_water_content_of_transpiration_layer / 100) * (transpiration_layer_soil_depth * 10)

            temp_3 = (permanent_wilting_point_soil_water_content_of_transpiration_layer / 100) * (transpiration_layer_soil_depth * 10)
            
            if temp_1 <= temp_3:
                temp_1 = temp_3
                transpiration = (soil_water_content_of_transpiration_layer_at_previous_step - temp_3 + upward_flux_from_transition_to_transpiration_layer)
                # transpiration = (soil_water_content_of_transpiration_layer_at_previous_step - upward_flux_from_transpiration_to_evaporation_layer + upward_flux_from_transition_to_transpiration_layer)
                # in porside she ke kodom dorste - faghat toye manfi tafafod dare

                return temp_1

            elif temp_1 >= temp_2:
                infiltration_from_transpiration_to_transition_layer = temp_1 - temp_2
                temp_1 = temp_2

                return temp_1

            elif temp_3 < temp_1 < temp_2:
                temp_4 = (temp_2 - temp_3) * MAD
                if temp_1 >= temp_4:

                    return temp_1

                else:
                    irrigation_requirement = stress_coefficient * (temp_2 - temp_1)
                    temp_1 = temp_2
                    return temp_1
    


    def transition_layer(
        coverd: bool,
        field_capacity_soil_water_content_of_transition_layer: float,
        permanent_wilting_point_soil_water_content_of_transition_layer: float,
        soil_water_content_of_transition_layer_at_previous_step: float,
        deep_percolation: float,
        infiltration_from_transpiration_to_transition_layer : float = 0,
        upward_flux_from_transition_to_transpiration_layer: float = 0
    ) -> float:
        """
        Description
        ------------
        calculating soil water content of transition layer
        ------------
        coverd: bool
            corved yes(True) or not coverd no(False)
        field_capacity_soil_water_content_of_transition_layer: float
            field capacity soil water content of transition layer in percent
        permanent_wilting_point_soil_water_content_of_transition_layer: float
            permanent wilting point soil water content of transition layer in percent
        soil_water_content_of_transition_layer_at_previous_step: float
            soil water content of transition layer at previous step in milimeter
        deep_percolation: float
            deep percolation in milimeter
        infiltration_from_transpiration_to_transition_layer : float
            infiltration from transpiration to transition layer in milimeter
        upward_flux_from_transition_to_transpiration_layer: float
            upward flux from transition to transpiration layer in milimeter
        ------------
        Returns
        ------------
        soil_water_content_of_transition_layer: float
            soil water content of transition layer in milimeter
        """
        
        if coverd is False:

            return('while there is no crop, transition layer is not defined ')

            
        else:

            transition_layer_soil_depth = soil_depth.get('transition_layer_covered')

            if infiltration_from_transpiration_to_transition_layer > 0:
                upward_flux_from_transition_to_transpiration_layer = 0
        
            if upward_flux_from_transition_to_transpiration_layer > 0:
                infiltration_from_transpiration_to_transition_layer = 0


            temp_1 = (soil_water_content_of_transition_layer_at_previous_step + infiltration_from_transpiration_to_transition_layer
                    - deep_percolation - upward_flux_from_transition_to_transpiration_layer)

            temp_2 = (field_capacity_soil_water_content_of_transition_layer / 100) * (transition_layer_soil_depth * 10)

            temp_3 = (permanent_wilting_point_soil_water_content_of_transition_layer / 100) * (transition_layer_soil_depth * 10)


            if temp_1 < temp_3:
                upward_flux_from_transition_to_transpiration_layer = upward_flux_from_transition_to_transpiration_layer - (temp_3 - temp_1) 
                temp_1 = temp_3

                return temp_1

            elif temp_1 > temp_2:
                deep_percolation = (temp_1 - temp_2)
                temp_1 = temp_2

                return temp_1

            else:
                return temp_1