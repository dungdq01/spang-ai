from human.relation.relation_config import PersonCreate
from human.script import ngu_hanh, KIM, MOC, THUY, THO, HOA, check_sinh
from human import human
from datetime import date


class RelationHuman:
    def __init__(self,person1, person2):
        self.person1 = person1
        self.person2 = person2
    
    def stroke_human(self):
        a,b,c = self.person1["a"], self.person1["b"],self.person1["c"]
        a1,b1,c1 = self.person2["a"], self.person2["b"],self.person2["c"]
        return a,b,c,a1,b1,c1

    def create_human(self):
        sky,human,land,galaxy = self.person1["sky"], self.person1["human"],self.person1["land"],self.person1["galaxy"]
        sky1,human1,land1,galaxy1 = self.person2["sky"], self.person2["human"],self.person2["land"],self.person2["galaxy"]
        return sky,human,land,galaxy,sky1,human1,land1,galaxy1

    def hknh(self,phu_mau, tat_ach,tu_nu,menh_cung):
        number_mc = (menh_cung // 10 + menh_cung % 10) % 9
        number_tu_nu = (tu_nu // 10 + tu_nu % 10) % 9
        number_tat_ach = (tat_ach // 10 + tat_ach % 10) % 9

        return number_mc, number_tu_nu, number_tat_ach 
    

    def khien_ban(self):
        a,b,c,a1,b1,c1 = self.stroke_human()
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()

        _number,_number_tu_tuc,_number_tat_ach = self.hknh(sky,human,land,galaxy)
        # print( f"A+B {_number_tat_ach} , B+C {_number_tu_tuc}, A+B+C {_number}")

        number_1,number_tu_tuc_1,number_tat_ach_1 = self.hknh(sky1,human1,land1,galaxy1)
        # print( f"A+B {number_tat_ach_1} , B+C {number_tu_tuc_1}, A+B+C {number_1}")

        if (_number_tat_ach != number_tu_tuc_1 and _number_tu_tuc != number_tat_ach_1 and _number_tu_tuc !=  number_1 and _number != number_tu_tuc_1) :
            return False
        else:
            return True
        
    def result_khien_ban(self):
        if self.khien_ban() == True:
            return "A4f1"
        else:
            return "A4f2"

    def doi_luu(self,sky,human,land,galaxy, sky1,human1,land1,galaxy1):
        text1 = "đối lưu trực tiếp -> A4f3"
        text2 = "đối lưu gián tiếp -> A4f4"

        ngu_hanh_phu_mau_1 = ngu_hanh[sky % 10]
        ngu_hanh_phu_mau_2 = ngu_hanh[sky1 % 10]

        ngu_hanh_tat_ach_1 = ngu_hanh[human % 10]
        ngu_hanh_tat_ach_2 = ngu_hanh[human1 % 10]

        ngu_hanh_tu_nu_1 = ngu_hanh[land % 10]
        ngu_hanh_tu_nu_2 = ngu_hanh[land1 % 10]


        x1 = ngu_hanh_phu_mau_1
        x2 = ngu_hanh_tat_ach_1
        x3 = ngu_hanh_tu_nu_1
        y1 = ngu_hanh_phu_mau_2
        y2 = ngu_hanh_tat_ach_2
        y3 = ngu_hanh_tu_nu_2

        # print(x1,x2,x3)
        # print(y1,y2,y3)


        if x2 == 0:
            if x1 == 1 or x3 == 1:
                if (y1 == 1 and y2 == 2) or (y1 == 2 and y2 == 1) or (y2 == 1 and y3 == 2) or (y2 == 2 and y3 == 1):
                    # print(text1)

                    return True
                if (y1 == 2 and y2 == 3) or (y1 == 3 and y2 == 2) or (y2 == 3 and y3 == 2) or (y2 == 2 and y3 == 3):
                    # print(text2)
                    return True
            if x1 == 2 or x3 == 2:
                if (y1 == 2 and y2 == 4) or (y1 == 4 and y2 == 2) or (y2 == 2 and y3 == 4) or (y2 == 4 and y3 == 2):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 1) or (y1 == 1 and y2 == 4) or (y2 == 1 and y3 == 4) or (y2 == 4 and y3 == 1):
                    # print(text2)
                    return True
            if x1 == 0 or x3 == 0:
                if (y1 == 1 and y2 == 1) or (y2 == 1 and y3 == 1):
                    # print(text1)
                    return True
                if (y1 == 2 and y2 == 2) or (y2 == 2 and y3 == 2):
                    # print(text2)
                    return True
            if x1 == 3 or x3 == 3:
                if (y1 == 0 and y2 == 2) or (y1 == 2 and y2 == 0) or (y2 == 0 and y3 == 2) or (y2 == 2 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 2 and y2 == 4) or (y1 == 4 and y2 == 2) or (y2 == 2 and y3 == 4) or (y2 == 4 and y3 == 2):
                    # print(text2)
                    return True
            if x1 == 4 or x3 == 4:
                if (y1 == 0 and y2 == 1) or (y1 == 1 and y2 == 0) or (y2 == 0 and y3 == 1) or (y2 == 1 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 1 and y2 == 2) or (y1 == 2 and y2 == 1) or (y2 == 2 and y3 == 1) or (y2 == 1 and y3 == 2):
                    # print(text2)
                    return True


        if x2 == 1:
            if x1 == 2 or x3 == 2:
                if (y1 == 3 and y2 == 2) or (y1 == 2 and y2 == 3) or (y2 == 3 and y3 == 2) or (y2 == 2 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 3) or (y1 == 3 and y2 == 4) or (y2 == 3 and y3 == 4) or (y2 == 4 and y3 == 3):
                    # print(text2)
                    return True
            if x1 == 3 or x3 == 3:
                if (y1 == 3 and y2 == 0) or (y1 == 0 and y2 == 3) or (y2 == 3 and y3 == 0) or (y2 == 0 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 2 and y2 == 0) or (y1 == 0 and y2 == 2) or (y2 == 2 and y3 == 0) or (y2 == 0 and y3 == 2):
                    # print(text2)
                    return True
            if x1 == 1 or x3 == 1 or (x1 == 1 and x3 == 1):
                if (y1 == 2 and y2 == 2) or (y2 == 2 and y3 == 2):
                    # print(text1)
                    return True
                if (y1 == 3 and y2 == 3) or (y2 == 3 and y3 == 3):
                    # print(text2)
                    return True
            if x1 == 0 or x3 == 0:
                if (y1 == 1 and y2 == 2) or (y1 == 2 and y2 == 1) or (y2 == 1 and y3 == 2) or (y2 == 2 and y3 == 1):
                    # print(text1)

                    return True
                if (y1 == 2 and y2 == 3) or (y1 == 3 and y2 == 2) or (y2 == 3 and y3 == 2) or (y2 == 2 and y3 == 3):
                    # print(text2)
                    return True
            if x1 == 4 or x3 == 4:
                if (y1 == 1 and y2 == 3) or (y1 == 3 and y2 == 1) or (y2 == 1 and y3 == 3) or (y2 == 3 and y3 == 1):
                    # print(text1)
                    return True
                if (y1 == 3 and y2 == 0) or (y1 == 0 and y2 == 3) or (y2 == 3 and y3 == 0) or (y2 == 0 and y3 == 3):
                    # print(text2)
                    return True


        if x2 == 2:
            if x1 == 3 or x3 == 3:
                if (y1 == 3 and y2 == 4) or (y1 == 4 and y2 == 3) or (y2 == 3 and y3 == 4) or (y2 == 4 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 0) or (y1 == 0 and y2 == 4) or (y2 == 0 and y3 == 4) or (y2 == 4 and y3 == 0):
                    # print(text2)
                    return True
            if x1 == 4 or x3 == 4:
                if (y1 == 4 and y2 == 1) or (y1 == 1 and y2 == 4) or (y2 == 4 and y3 == 1) or (y2 == 1 and y3 == 4):
                    # print(text1)
                    return True
                if (y1 == 3 and y2 == 1) or (y1 == 1 and y2 == 3) or (y2 == 3 and y3 == 1) or (y2 == 1 and y3 == 3):
                    # print(text2)
                    return True
            if x1 == 2 or x3 == 2:
                if (y1 == 3 and y2 == 3) or (y2 == 3 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 4) or (y2 == 4 and y3 == 4):
                    # print(text2)
                    return True
            if x1 == 0 or x3 == 0:
                if (y1 == 2 and y2 == 4) or (y1 == 4 and y2 == 2) or (y2 == 2 and y3 == 4) or (y2 == 4 and y3 == 2):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 1) or (y1 == 1 and y2 == 4) or (y2 == 1 and y3 == 4) or (y2 == 4 and y3 == 1):
                    # print(text2)
                    return True
            if x1 == 1 or x3 == 1:
                if (y1 == 3 and y2 == 2) or (y1 == 2 and y2 == 3) or (y2 == 3 and y3 == 2) or (y2 == 2 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 3) or (y1 == 3 and y2 == 4) or (y2 == 3 and y3 == 4) or (y2 == 4 and y3 == 3):
                    # print(text2)
                    return True

        if x2 == 3:
            if x1 == 4 or x3 == 4:
                if (y1 == 0 and y2 == 4) or (y1 == 4 and y2 == 0) or (y2 == 0 and y3 == 4) or (y2 == 4 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 1 and y2 == 0) or (y1 == 0 and y2 == 1) or (y2 == 0 and y3 == 1) or (y2 == 1 and y3 == 0):
                    # print(text2)
                    return True
            if x1 == 0 or x3 == 0:
                if (y1 == 0 and y2 == 2) or (y1 == 2 and y2 == 0) or (y2 == 0 and y3 == 2) or (y2 == 2 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 2 and y2 == 4) or (y1 == 4 and y2 == 2) or (y2 == 2 and y3 == 4) or (y2 == 4 and y3 == 2):
                    # print(text2)
                    return True
            if x1 == 3 or x3 == 3:
                if (y1 == 4 and y2 == 4) or (y2 == 4 and y3 == 4):
                    # print(text1)
                    return True
                if (y1 == 0 and y2 == 0) or (y2 == 0 and y3 == 0):
                    # print(text2)
                    return True
            if x1 == 2 or x3 == 2:
                if (y1 == 3 and y2 == 4) or (y1 == 4 and y2 == 3) or (y2 == 3 and y3 == 4) or (y2 == 4 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 4 and y2 == 0) or (y1 == 0 and y2 == 4) or (y2 == 0 and y3 == 4) or (y2 == 4 and y3 == 0):
                    # print(text2)
                    return True
            if x1 == 1 or x3 == 1:
                if (y1 == 3 and y2 == 0) or (y1 == 0 and y2 == 3) or (y2 == 3 and y3 == 0) or (y2 == 0 and y3 == 3):
                    # print(text1)
                    return True
                if (y1 == 2 and y2 == 0) or (y1 == 0 and y2 == 2) or (y2 == 2 and y3 == 0) or (y2 == 0 and y3 == 2):
                    # print(text2)
                    return True


        if x2 == 4:
            if x1 == 0 or x3 == 0:
                if (y1 == 0 and y2 == 1) or (y1 == 1 and y2 == 0) or (y2 == 0 and y3 == 1) or (y2 == 1 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 1 and y2 == 2) or (y1 == 2 and y2 == 1) or (y2 == 2 and y3 == 1) or (y2 == 1 and y3 == 2):
                    # print(text2)
                    return True
            if x1 == 1 or x3 == 1:
                if (y1 == 1 and y2 == 3) or (y1 == 3 and y2 == 1) or (y2 == 1 and y3 == 3) or (y2 == 3 and y3 == 1):
                    # print(text1)
                    return True
                if (y1 == 3 and y2 == 0) or (y1 == 0 and y2 == 3) or (y2 == 3 and y3 == 0) or (y2 == 0 and y3 == 3):
                    # print(text2)
                    return True
            if x1 == 4 or x3 == 4:
                if (y1 == 0 and y2 == 0) or (y2 == 0 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 1 and y2 == 1) or (y2 == 1 and y3 == 1):
                    # print(text2)
                    return True
            if x1 == 3 or x3 == 3:
                if (y1 == 0 and y2 == 4) or (y1 == 4 and y2 == 0) or (y2 == 0 and y3 == 4) or (y2 == 4 and y3 == 0):
                    # print(text1)
                    return True
                if (y1 == 1 and y2 == 0) or (y1 == 0 and y2 == 1) or (y2 == 0 and y3 == 1) or (y2 == 1 and y3 == 0):
                    # print(text2)
                    return True
            if x1 == 2 or x3 == 2:
                if (y1 == 4 and y2 == 1) or (y1 == 1 and y2 == 4) or (y2 == 4 and y3 == 1) or (y2 == 1 and y3 == 4):
                    # print(text1)
                    return True
                if (y1 == 3 and y2 == 1) or (y1 == 1 and y2 == 3) or (y2 == 3 and y3 == 1) or (y2 == 1 and y3 == 3):
                    # print(text2)
                    return True
        return False


    def check_doi_luu(self):
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        doi_luu_1 = self.doi_luu(sky,human,land,galaxy,sky1,human1,land1,galaxy1)
        # print(doi_luu_1)
        doi_luu_2 = self.doi_luu(sky1,human1,land1,galaxy1,sky,human,land,galaxy)
        # print(doi_luu_2)
        if doi_luu_1 == False and doi_luu_2 == False:
            return "A4f4"
        else:
            return "A4f3"


    def f5_f6(self):
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        doi_luu_1 = self.doi_luu(sky,human,land,galaxy,sky1,human1,land1,galaxy1)
        if self.check_doi_luu() == "A4f3":
            if doi_luu_1 == True:
                return "A4f5"
            else:
                return "A4f6"
        else:
            # print("kiểm tra lại đối lưu")
            return "A4f6"


    def f7_f8(self):
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        doi_luu_2 = self.doi_luu(sky1,human1,land1,galaxy1,sky,human,land,galaxy)
        print(doi_luu_2)
        if self.check_doi_luu() == "A4f3":
            if doi_luu_2 == True:
                return "A4f7"
            else:
                return "A4f8"
        else:
            return "A4f8"
        

    def tai_loc(self):

        mc_1,mc_2 = self.person1["galaxy"],self.person2["galaxy"]
        number_mc_1 = (mc_1 // 10 + mc_1 % 10) % 9
        number_mc_2 = (mc_2 // 10 + mc_2 % 10) % 9

        text = "A4f9"
        text2 = "A4f10"

        x = abs(number_mc_1 - number_mc_2)
        if x == 1:
            return text
        else :
            return text2


    def nghiep_chuong(self):
        mc_1,mc_2 = self.person1["galaxy"],self.person2["galaxy"]
        number_mc_1 = (mc_1 // 10 + mc_1 % 10) % 9
        number_mc_2 = (mc_2 // 10 + mc_2 % 10) % 9

        text3 = "A4f11"
        text4 = "A4f12"

        x = abs(number_mc_1 - number_mc_2)
        if x == 2:
            return text3
        else :
            return text4
        
    def g1_2(self):
        if self.khien_ban() == True:
            return("A4g1")
        else:
            return("A4g2")
        
    def g3_g4(self):
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        doi_luu_1 = self.doi_luu(sky,human,land,galaxy,sky1,human1,land1,galaxy1)
        # doi_luu_2 = self.doi_luu(phu_mau_2,tat_ach_2,tu_nu_2,phu_mau_1,tat_ach_1,tu_nu_1)
        doi_luu_2 = self.doi_luu(sky1,human1,land1,galaxy1,sky,human,land,galaxy)
        if doi_luu_1 == False and doi_luu_2 == False:
            return("A4g4")
        else:
            return("A4g3")

        
    def khac_cot_ghi_tam(self):
        a,b,c,a1,b1,c1 = self.stroke_human()
        param = [0,1,2,3,4,4,3,2,1,0]
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        _number,_number_tu_tuc,_number_tat_ach = self.hknh(sky,human,land,galaxy)
        _number1,_number_tu_tuc1,_number_tat_ach1 = self.hknh(sky1,human1,land1,galaxy1)

        ngu_hanh_mc = param[(abs(_number - _number1)) % 9]
        ngu_hanh_a = param[(abs(_number_tat_ach - _number_tu_tuc)) % 9]
        ngu_hanh_b = param[(abs(_number_tat_ach1 - _number_tu_tuc1 )) % 9]

        if ngu_hanh_mc == ngu_hanh_a or ngu_hanh_mc == ngu_hanh_b:
            return("A4g5")
        else:
            return("A4g6")
        
    def g7_g8_1(self,a,b,c,a1,b1,c1):
        phu_mau_1 = a+1
        tat_ach_1 = a+b
        tu_nu_1 = b+(c if c > 0 else 1)
        phu_mau_2 = a1+1
        tat_ach_2 = a1+b1
        tu_nu_2 = b1+(c1 if c1 > 0 else 1)


        mc_1 = phu_mau_1 + tat_ach_1 + tu_nu_1
        mc_2 = phu_mau_2 + tat_ach_2 + tu_nu_2

        don_vi_phu_mau_1 = phu_mau_1 % 10
        don_vi_phu_mau_2 = phu_mau_2 % 10

        don_vi_tat_ach_1 = tat_ach_1 % 10
        don_vi_tat_ach_2 = tat_ach_2 % 10

        don_vi_tu_nu_1 = tu_nu_1 % 10
        don_vi_tu_nu_2 = tu_nu_2 % 10

        hang_chuc_tat_ach_1 = (tat_ach_1 - don_vi_tat_ach_1) // 10

        hang_chuc_tat_ach_2 = (tat_ach_2 - don_vi_tat_ach_2) // 10

        hang_chuc_tu_nu_1 = (tu_nu_1 - don_vi_tu_nu_1) // 10

        hang_chuc_tu_nu_2 = (tu_nu_2 - don_vi_tu_nu_2) // 10

        num_hknh_tat_ach_1 = (don_vi_tat_ach_1 + hang_chuc_tat_ach_1) % 9
        num_hknh_tat_ach_2 = (don_vi_tat_ach_2 + hang_chuc_tat_ach_2) % 9
        num_hknh_tu_nu_1 = (don_vi_tu_nu_1 + hang_chuc_tu_nu_1) % 9
        num_hknh_tu_nu_2 = (don_vi_tu_nu_2 + hang_chuc_tu_nu_2) % 9


        ngu_hanh_phu_mau_1 = ngu_hanh[don_vi_phu_mau_1]
        ngu_hanh_phu_mau_2 = ngu_hanh[don_vi_phu_mau_2]

        ngu_hanh_tat_ach_1 = ngu_hanh[don_vi_tat_ach_1]
        ngu_hanh_tat_ach_2 = ngu_hanh[don_vi_tat_ach_2]

        ngu_hanh_tu_nu_1 = ngu_hanh[don_vi_tu_nu_1]
        ngu_hanh_tu_nu_2 = ngu_hanh[don_vi_tu_nu_2]

        hknh_tat_ach_1 = ngu_hanh[num_hknh_tat_ach_1]
        hknh_tat_ach_2 = ngu_hanh[num_hknh_tat_ach_2]

        hknh_tu_nu_1 = ngu_hanh[num_hknh_tu_nu_1]
        hknh_tu_nu_2 = ngu_hanh[num_hknh_tu_nu_2]

        # print(f"A: {hknh_tat_ach_1} {hknh_tu_nu_1} B : {hknh_tat_ach_2}  {hknh_tu_nu_2} ")
        # print(f"A: {ngu_hanh_phu_mau_1} {ngu_hanh_tat_ach_1} {ngu_hanh_tu_nu_1} B : {ngu_hanh_phu_mau_2} {ngu_hanh_tat_ach_2}  {ngu_hanh_tu_nu_2} ")


        if (abs(ngu_hanh_tat_ach_1 - ngu_hanh_tu_nu_1) in [1, 4]) or ((ngu_hanh_tat_ach_1 == ngu_hanh_tu_nu_1) and (abs(ngu_hanh_tat_ach_1 - ngu_hanh_phu_mau_1) in [0,1,4] )) :
            # if abs(ngu_hanh_tat_ach_1 - ngu_hanh_tu_nu_1) in [1, 4] :
                hknh_tat_ach_1_n = (hknh_tat_ach_1 + 1 ) % 5
                hknh_tu_nu_1_n = (hknh_tu_nu_1 + 1 ) % 5
                # print(f"A: {hknh_tat_ach_1_n} {hknh_tu_nu_1_n} B :{ngu_hanh_phu_mau_2} {ngu_hanh_tat_ach_2}  {ngu_hanh_tu_nu_2} ")


                if (hknh_tat_ach_1_n == ngu_hanh_tat_ach_2 and hknh_tu_nu_1_n == ngu_hanh_tu_nu_2):
                    # print(f"A: {hknh_tat_ach_1_n} {hknh_tu_nu_1_n} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_tu_nu_2} ")
                    return True
                if (hknh_tat_ach_1_n == ngu_hanh_tu_nu_2 and hknh_tu_nu_1_n == ngu_hanh_tat_ach_2):
                    # print(f"A: {hknh_tat_ach_1_n} {hknh_tu_nu_1_n} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_tu_nu_2} ")
                    return True

                if (hknh_tat_ach_1_n == ngu_hanh_tat_ach_2 and hknh_tu_nu_1_n == ngu_hanh_phu_mau_2):
                    # print(f"A: {hknh_tat_ach_1_n} {hknh_tu_nu_1_n} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_phu_mau_2} ")
                    return True
                if (hknh_tat_ach_1_n == ngu_hanh_phu_mau_2 and hknh_tu_nu_1_n == ngu_hanh_tat_ach_2):
                    # print(f"A: {hknh_tat_ach_1_n} {hknh_tu_nu_1_n} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_phu_mau_2} ")
                    return True

        if (abs(ngu_hanh_tat_ach_1 - ngu_hanh_tu_nu_1) in [2,3]) or ((ngu_hanh_tat_ach_1 == ngu_hanh_tu_nu_1) and (abs(ngu_hanh_tat_ach_1 - ngu_hanh_phu_mau_1) in [2,3] )) :
                if (hknh_tat_ach_1 == ngu_hanh_tat_ach_2 and hknh_tu_nu_1 == ngu_hanh_tu_nu_2):
                    # print(f"A: {hknh_tat_ach_1} {hknh_tu_nu_1} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_tu_nu_2} ")
                    return True
                if (hknh_tat_ach_1 == ngu_hanh_tu_nu_2 and hknh_tu_nu_1 == ngu_hanh_tat_ach_2):
                    # print(f"A: {hknh_tat_ach_1} {hknh_tu_nu_1} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_tu_nu_2} ")
                    return True

                if (hknh_tat_ach_1 == ngu_hanh_tat_ach_2 and hknh_tu_nu_1 == ngu_hanh_phu_mau_2):
                    # print(f"A: {hknh_tat_ach_1} {hknh_tu_nu_1} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_phu_mau_2} ")
                    return True
                if (hknh_tat_ach_1 == ngu_hanh_phu_mau_2 and hknh_tu_nu_1 == ngu_hanh_tat_ach_2):
                    # print(f"A: {hknh_tat_ach_1} {hknh_tu_nu_1} B : {ngu_hanh_tat_ach_2}  {ngu_hanh_phu_mau_2} ")
                    return True

        return False


    def g7_g8_2(self):
        phu_mau_1,tat_ach_1,tu_nu_1,phu_mau_2,tat_ach_2,tu_nu_2 = self.stroke_human()
        # sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        # _number,num_hknh_tu_nu_1,num_hknh_tat_ach_1 = self.hknh(sky,human,land,galaxy)
        # _number1,num_hknh_tu_nu_2,num_hknh_tat_ach_2 = self.hknh(sky1,human1,land1,galaxy1)

        x = self.g7_g8_1(phu_mau_1,tat_ach_1,tu_nu_1,phu_mau_2,tat_ach_2,tu_nu_2)
        y = self.g7_g8_1(phu_mau_2,tat_ach_2,tu_nu_2,phu_mau_1,tat_ach_1,tu_nu_1)
        if (x == False and y == False):
            return("A4g8")
        else:
            return("A4g7")

    def g9_g10(self):
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        _number,num_hknh_tu_nu_1,num_hknh_tat_ach_1 = self.hknh(sky,human,land,galaxy)
        _number1,num_hknh_tu_nu_2,num_hknh_tat_ach_2 = self.hknh(sky1,human1,land1,galaxy1)

        hknh_tat_ach_1 = ngu_hanh[num_hknh_tat_ach_1]
        print(hknh_tat_ach_1)
        hknh_tat_ach_2 = ngu_hanh[num_hknh_tat_ach_2]
        print(hknh_tat_ach_2)

        hknh_tu_nu_1 = ngu_hanh[num_hknh_tu_nu_1]
        print(hknh_tu_nu_1)
        hknh_tu_nu_2 = ngu_hanh[num_hknh_tu_nu_2]
        print(hknh_tu_nu_2)

        if hknh_tat_ach_1 != hknh_tu_nu_1:
            if (hknh_tat_ach_1 == hknh_tu_nu_2) and (hknh_tat_ach_2 == hknh_tu_nu_1):
                return("A4g9")
            else:
                return("A4g10")
        else:
            return("A4g10")
        
    def g11_g12(self):
        phu_mau_1,tat_ach_1,tu_nu_1,phu_mau_2,tat_ach_2,tu_nu_2 = self.stroke_human()
        sky,human,land,galaxy,sky1,human1,land1,galaxy1 = self.create_human()
        _number,num_hknh_tu_nu_1,num_hknh_tat_ach_1 = self.hknh(sky,human,land,galaxy)
        _number1,num_hknh_tu_nu_2,num_hknh_tat_ach_2 = self.hknh(sky1,human1,land1,galaxy1)

        nh_tu_nu_1 = ngu_hanh[land % 9]
        nh_tu_nu_2 = ngu_hanh[land1 % 9]
        nh_galaxy = ngu_hanh[galaxy % 9]
        nh_galaxy1 = ngu_hanh[galaxy1 % 9]
        print(land1,land,galaxy1, galaxy)
        print(nh_tu_nu_1,nh_tu_nu_2,nh_galaxy,nh_galaxy1)
        # print()

        if ((abs(land1 - land) == 1) and (nh_tu_nu_1 != nh_tu_nu_2)) :
            return("A4g11")
        if ((abs(galaxy- galaxy1) == 1) and (nh_galaxy != nh_galaxy1)):
            return("A4g11")
        return("A4g12")
   

