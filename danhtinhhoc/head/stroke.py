from head import chinese_simplify_stroke, chinese_traditional_stroke

class stroke_name:
    def __init__(self,family_name_stroke,given_name_stroke):
        self.family_name_stroke = family_name_stroke
        self.given_name_stroke =  given_name_stroke
        
    def get_stroke_name(self):
        sky_name_stroke_list = list(filter(None,self.family_name_stroke.values()))
        land_name_stroke_list = list(filter(None,self.given_name_stroke.values()))

        sky_name_stroke = sum(sky_name_stroke_list) if sky_name_stroke_list else 0
        human_stroke = land_name_stroke_list[0] if land_name_stroke_list else 0
        land_name_stroke = sum(land_name_stroke_list[1:]) if len(land_name_stroke_list) > 1 else 0
        
        if len(land_name_stroke_list) == 1:
            land_name_stroke = 0

        return sky_name_stroke, human_stroke, land_name_stroke 
    
