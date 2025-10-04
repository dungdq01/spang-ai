from human import human

class PersonCreate:
    def __init__(self, a,b,c, date, a1,b1,c1, date1):
            self.sky = a
            self.human = b
            self.land = c
            self.date = date
            self.sky1 = a1
            self.human1 = b1
            self.land1 = c1
            self.date1 = date1

    # def hknh(self,phu_mau, tat_ach,tu_nu,menh_cung):
    #     number_mc = (menh_cung // 10 + menh_cung % 10) % 9
    #     number_tu_nu = (tu_nu // 10 + tu_nu % 10) % 9
    #     number_tat_ach = (tat_ach // 10 + tat_ach % 10) % 9

    #     return number_mc, number_tu_nu, number_tat_ach 
    
    def create_cungso(self):
        cungso = human.CungSo(self.sky, self.human, self.land, self.date )
        cungso1 = human.CungSo(self.sky1, self.human1, self.land1,self.date1)
        __sky = cungso.phu_mau_cung()
        __human = cungso.tat_ach_cung()
        __land= cungso.tu_nu_cung()
        __galaxy = cungso.menh_cung()
        __sky1 = cungso1.phu_mau_cung()
        __human1 = cungso1.tat_ach_cung()
        __land1 = cungso1.tu_nu_cung()
        __galaxy1 = cungso1.menh_cung()
        return __sky,__human[0],__land[0], __galaxy[0],__sky1,__human1[0],__land1[0],__galaxy1[0]
    
                
    def create_person(self):
        __sky,__human,__land, __galaxy,__sky1,__human1,__land1,__galaxy1 = self.create_cungso()
        self.person1 = {"a": self.sky,
                        "b": self.human,
                        "c": self.land,
                        "galaxy": __galaxy,
                        "sky":__sky,
                        "human": __human,
                        "land": __land,
                        "date": self.date}

        self.person2 =  {   "a": self.sky1,
                            "b": self.human1,
                            "c": self.land1,
                            "galaxy": __galaxy1,
                            "sky":__sky1,
                            "human": __human1,
                            "land": __land1,
                            "date": self.date1}
        return self.person1, self.person2