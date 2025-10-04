from human.script import ngu_hanh, KIM, MOC, THUY, THO, HOA, check_sinh
from human import human
from datetime import date


class OnlyHuman:
    """
    scirpt :  
    """

    def __init__(self, sky, human, land, galaxy, date):
        self.sky = sky
        self.human = human
        self.land = land
        self.galaxy = galaxy
        self.date = date
    
    def number_five_element(self):

        don_vi_tat_ach = self.human % 10
        don_vi_tu_nu = self.land % 10
        hang_chuc_tat_ach = (self.human - don_vi_tat_ach)//10
        hang_chuc_tu_nu = (self.land - don_vi_tu_nu)//10
        # print(don_vi_tat_ach,hang_chuc_tat_ach,don_vi_tu_nu,hang_chuc_tu_nu)

        tat_ach_sum = (don_vi_tat_ach + hang_chuc_tat_ach) 
        tu_nu_sum = (don_vi_tu_nu + hang_chuc_tu_nu)
        # print(tat_ach_sum,tu_nu_sum)

        return don_vi_tat_ach, don_vi_tu_nu, tat_ach_sum, tu_nu_sum


    def tai_khi(self):
        """
        logic : 
        """

        don_vi_tat_ach, don_vi_tu_nu, tat_ach_sum, tu_nu_sum = self.number_five_element()
        result_tai_khi = "A4c"
        pre_tk = (abs(tat_ach_sum%9 - tu_nu_sum%9))
        tai_khi = pre_tk if pre_tk < 5 else 9 - pre_tk 
        if tai_khi == 0:
            tai_khi += 5
        result_tai_khi+=str(tai_khi)

        return result_tai_khi
    
    
    def tai_kho(self) :

        don_vi_tat_ach, don_vi_tu_nu, tat_ach_sum, tu_nu_sum = self.number_five_element()

        nguhanh_tat_ach = ngu_hanh[don_vi_tat_ach]
        nguhanh_tu_nu = ngu_hanh[don_vi_tu_nu]

        menh = check_sinh(nguhanh_tat_ach, nguhanh_tu_nu)
        menh_dao = check_sinh(nguhanh_tu_nu, nguhanh_tat_ach)

        result_tai_kho = ""
        if menh_dao == "sinh" or menh_dao == "khac":
            result_tai_kho+=str("A4c6")
            return result_tai_kho
            # return menh_dao
        if menh == "sinh":
            result_tai_kho+=str("A4c7")
            return result_tai_kho
        if menh == "khac":
            result_tai_kho+=str("A4c8")
            return result_tai_kho
        if nguhanh_tat_ach == nguhanh_tu_nu:
            result_tai_kho+=str("A4c9")
        
        return result_tai_kho


    def menh_cach(self):

        result_menh_cach = []
        don_vi_phu_mau = self.sky % 10
        don_vi_tat_ach = self.human % 10
        don_vi_tu_nu = self.land % 10

        ngu_hanh_phu_mau = ngu_hanh[don_vi_phu_mau]
        ngu_hanh_tat_ach = ngu_hanh[don_vi_tat_ach]
        ngu_hanh_tu_nu = ngu_hanh[don_vi_tu_nu]

        quan_he =["sinh", "khac", "bi_khac", "duoc_sinh"]

        x = ngu_hanh_phu_mau
        y = ngu_hanh_tat_ach
        z = ngu_hanh_tu_nu

        sk2 = check_sinh(ngu_hanh_tat_ach,ngu_hanh_phu_mau)
        sk1 = check_sinh(ngu_hanh_tat_ach, ngu_hanh_tu_nu)
        sk3 = check_sinh(ngu_hanh_phu_mau, ngu_hanh_tu_nu)

        print(f"sk1: {sk1} ,  sk2: {sk2}")

        if ngu_hanh_tat_ach == 0:

            if ngu_hanh_phu_mau == 1:
                result_menh_cach.append("A4a6")
            if ngu_hanh_phu_mau == 2:
                result_menh_cach.append("A4a2")
            if ngu_hanh_phu_mau == 3:
                result_menh_cach.append("A4a1")
            if ngu_hanh_phu_mau == 4:
                result_menh_cach.append("A4a8")
            if ngu_hanh_tu_nu == 1:
                result_menh_cach.append("A4a6")
            if ngu_hanh_tu_nu == 2:
                result_menh_cach.append("A4a2")
            if ngu_hanh_tu_nu == 3:
                result_menh_cach.append("A4a1")
            if ngu_hanh_tu_nu == 4:
                result_menh_cach.append("A4a8")

        if ngu_hanh_tat_ach == 1:
            if ngu_hanh_phu_mau == 0:
                result_menh_cach.append("A4a6")
            if ngu_hanh_phu_mau == 2:
                result_menh_cach.append("A4a9")
            if ngu_hanh_phu_mau == 3:
                result_menh_cach.append("A4a5")
            if ngu_hanh_phu_mau == 4:
                result_menh_cach.append("A4a4")
            if ngu_hanh_tu_nu == 0:
                result_menh_cach.append("A4a6")
            if ngu_hanh_tu_nu == 2:
                result_menh_cach.append("A4a9")
            if ngu_hanh_tu_nu == 3:
                result_menh_cach.append("A4a5")
            if ngu_hanh_tu_nu == 4:
                result_menh_cach.append("A4a4")

        if ngu_hanh_tat_ach == 2:
            if ngu_hanh_phu_mau == 0:
                result_menh_cach.append("A4a2")
            if ngu_hanh_phu_mau == 1:
                result_menh_cach.append("A4a9")
            if ngu_hanh_phu_mau == 3:
                result_menh_cach.append("A4a7")
            if ngu_hanh_phu_mau == 4:
                result_menh_cach.append("A4a3")
            if ngu_hanh_tu_nu == 0:
                result_menh_cach.append("A4a2")
            if ngu_hanh_tu_nu == 1:
                result_menh_cach.append("A4a9")
            if ngu_hanh_tu_nu == 3:
                result_menh_cach.append("A4a7")
            if ngu_hanh_tu_nu == 4:
                result_menh_cach.append("A4a3")

        if ngu_hanh_tat_ach == 3:
            if ngu_hanh_phu_mau == 0:
                result_menh_cach.append("A4a1")
            if ngu_hanh_phu_mau == 1:
                result_menh_cach.append("A4a5")
            if ngu_hanh_phu_mau == 2:
                result_menh_cach.append("A4a7")
            if ngu_hanh_phu_mau == 4:
                result_menh_cach.append("A4a10")
            if ngu_hanh_tu_nu == 0:
                result_menh_cach.append("A4a1")
            if ngu_hanh_tu_nu == 1:
                result_menh_cach.append("A4a5")
            if ngu_hanh_tu_nu == 2:
                result_menh_cach.append("A4a7")
            if ngu_hanh_tu_nu == 4:
                result_menh_cach.append("A4a10")

        if ngu_hanh_tat_ach == 4:
            if ngu_hanh_phu_mau == 0:
                result_menh_cach.append("A4a8")
            if ngu_hanh_phu_mau == 1:
                result_menh_cach.append("A4a4")
            if ngu_hanh_phu_mau == 2:
                result_menh_cach.append("A4a3")
            if ngu_hanh_phu_mau == 3:
                result_menh_cach.append("A4a10")
            if ngu_hanh_tu_nu == 0:
                result_menh_cach.append("A4a8")
            if ngu_hanh_tu_nu == 1:
                result_menh_cach.append("A4a4")
            if ngu_hanh_tu_nu == 2:
                result_menh_cach.append("A4a3")
            if ngu_hanh_tu_nu == 3:
                result_menh_cach.append("A4a10")

        result_only = []
        if ngu_hanh_phu_mau == ngu_hanh_tat_ach == ngu_hanh_tu_nu:
            if x == 0:
                result_only.append("A4a11")
            if x == 2:
                result_only.append("A4a12")
            if x == 4:
                result_only.append("A4a13")
            if x == 1:
                result_only.append("A4a14")
            if x == 3: 
                result_only.append("A4a15")


        result_sinh_khac = []

        if (sk1 == "binh" and (sk2 in quan_he )) or (sk2 == "binh" and (sk1 in quan_he )) or ((sk1 == sk2 and sk1 in quan_he )) :
            result_sinh_khac.append("A4a16")
        if sk1 == sk2 == "binh" :
            result_sinh_khac.append("A4a21")

        if (sk1 in quan_he ) and sk2 == "binh" :
            result_sinh_khac.append(f"A4a18" )
        if (sk2 in quan_he ) and sk1 == "binh":
            result_sinh_khac.append("A4a19")
        if ((sk1 == "sinh" ) and (sk2 == "bi_khac")) or ((sk2 == "sinh" ) and (sk1 == "bi_khac" )) or ((sk1 == "khac" ) and (sk2 == "duoc_sinh")) or ((sk2 == "khac" ) and (sk1 == "duoc_sinh" )):
            result_sinh_khac.append("A4a20")

        if (sk1 in quan_he) and (sk2 in quan_he) and (sk3 in quan_he):
            result_sinh_khac.append("A4a17")
        # print(sk1,sk2)
    
        return [result_menh_cach,result_only,result_sinh_khac] if len(result_only) != 0 else [result_menh_cach,result_sinh_khac]


    def hon_nhan(self):
        """Phân tích hôn nhân dựa trên tứ trụ và ngũ hành."""

        result_hon_nhan = []
        ngu_hanh_hon_nhan = "A4d"
        x = ""

        # Tính toán hàng đơn vị và hàng chục (giữ nguyên cách tính cũ)
        don_vi_tat_ach,don_vi_tu_nu, tat_ach_sum, tu_nu_sum = self.number_five_element()
        hknh_tu_nu_1 = ngu_hanh[tu_nu_sum % 9]
        print("tu_nu_hk",hknh_tu_nu_1,tu_nu_sum)
        hknh_tat_ach = ngu_hanh[tat_ach_sum % 9]
        print("tat_ach_hk",hknh_tat_ach,tat_ach_sum)

        if (hknh_tat_ach == 0 and hknh_tu_nu_1 == 1) or (hknh_tat_ach == 1 and hknh_tu_nu_1 == 0) :
            x+=str(3)
            y = "moc sinh hoa"
        if (hknh_tat_ach == 1 and hknh_tu_nu_1 == 2) or (hknh_tat_ach == 2 and hknh_tu_nu_1 == 1):
            x+=str(4)
            y = "hoa sinh tho"
        if (hknh_tat_ach == 2 and hknh_tu_nu_1 == 3) or (hknh_tat_ach == 3 and hknh_tu_nu_1 == 2):
            x+=str(5)
            y = "tho sinh kim"
        if (hknh_tat_ach == 3 and hknh_tu_nu_1 == 4) or (hknh_tat_ach == 4 and hknh_tu_nu_1 == 3):
            x+=str(6)
            y = "kim sinh thuy"
        if (hknh_tat_ach == 4 and hknh_tu_nu_1 == 0) or ( hknh_tat_ach == 0 and hknh_tu_nu_1 == 4 ):
            x+=str(7)
            y = "thuy sinh moc"
        if (hknh_tat_ach == 3 and hknh_tu_nu_1 == 0) or (hknh_tat_ach == 0 and hknh_tu_nu_1 == 3) :
            x+=str(9)
            y = "kim khac moc"
        if (hknh_tat_ach == 0 and hknh_tu_nu_1 == 2) or (hknh_tat_ach == 2 and hknh_tu_nu_1 == 0) :
            x+=str(10)
            y = "moc khac tho"
        if (hknh_tat_ach == 2 and hknh_tu_nu_1 == 4) or (hknh_tat_ach == 4 and hknh_tu_nu_1 == 3) :
            x+=str(11)
            y = "tho khac thuy"
        if (hknh_tat_ach == 1 and hknh_tu_nu_1 == 4) or (hknh_tat_ach == 4 and hknh_tu_nu_1 == 1) :
            x+=str(12)
            y = "thuy khac hoa"
        if (hknh_tat_ach == 3 and hknh_tu_nu_1 == 1) or (hknh_tat_ach == 1 and hknh_tu_nu_1 == 3) :
            x+=str(13)
            y = "hoa khac kim"


        quan_he = check_sinh(hknh_tat_ach, hknh_tu_nu_1)
        tuong_va_mo_ta = {
            "sinh": ("Vượng Tượng", "A4d1", "tương sinh"),
            "duoc_sinh": ("Đạm Tượng", "A4d2", "được tương sinh"),
            "khac": ("Phá Tượng", "A4d8", "tương khắc"),
            "bi_khac": ("Phá Tượng", "A4d8", "bị tương khắc"),
            "binh": ("Bình Song", "", ""),  # Giá trị tạm thời cho "binh"
        }
        if quan_he in tuong_va_mo_ta:
            tuong, content_tuong, mo_ta = tuong_va_mo_ta[quan_he]  # Gán giá trị tạm thời cho mo_ta
            if quan_he == "binh":
                content_tuong = "A4d14" if (tu_nu_sum % 2 == tat_ach_sum % 2) else "A4d15"
                mo_ta = "equal" if (tu_nu_sum % 2 == tat_ach_sum % 2) else "double"
            ngu_hanh_hon_nhan += str(x)
            result_hon_nhan.append(ngu_hanh_hon_nhan)
            result_hon_nhan.append(content_tuong)
            result_hon_nhan.append(mo_ta)
        # Chuẩn hóa output chỉ trả về mã
        # result_hon_nhan có thể gồm: [ngu_hanh_hon_nhan+x, content_tuong, mo_ta]
        # Ta chỉ lấy các mã, loại bỏ mô tả
        result_codes = []
        for item in result_hon_nhan:
            # Loại bỏ mô tả nếu có (vd: 'A4d1', 'A4d8', 'A4d14', ...)
            if isinstance(item, str) and item.startswith('A4'):
                result_codes.append(item)
        # Nếu chỉ có 1 mã thì trả về string, nhiều mã trả về list
        if len(result_codes) == 1:
            return result_codes[0]
        return result_codes

 

