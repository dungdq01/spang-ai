
from datetime import date 

class CungSo:

    def __init__(self, a, b, c, birth_day):
        self.a = a
        self.b = b
        self.c = c
        self.date = birth_day

    def menh_cung(self):
        no = self.a + self.b + self.c
        if no <=9 :
            no = 9
        if no >= 54:
            no = 54
        result_menh_cung= "A4b3 No." + str(no)
        return [no, result_menh_cung]

    def phu_mau_cung(self):
        no = self.a + 1
        return no

    def tat_ach_cung(self):
        no = self.a + self.b
        if no > 41 :
            no = 41
        result_tat_ach_cung= "A4b1 No." + str(no)
        return [no,result_tat_ach_cung ]

    def tu_nu_cung(self):
        if self.c == 0 or None:
            no = self.b + 1
        else:
            no = self.b + self.c

        if no <=9 :
            no = 9
        if no >= 40:
            no = 40
        result_tu_nu_cung = "A4b2 No." + str(no)
        return [no,result_tu_nu_cung ]

    def luu_nien(self):
        """Tính toán và in lưu niên đại vận. Chấp nhận nhiều định dạng ngày tháng."""
        # Tự động nhận dạng và chuyển đổi các định dạng ngày tháng phổ biến
        birth_day = birth_month = birth_year = None
        if '-' in self.date:
            parts = self.date.split('-')
            if len(parts[0]) == 4:
                # yyyy-mm-dd
                birth_year, birth_month, birth_day = map(int, parts)
            else:
                # dd-mm-yyyy
                birth_day, birth_month, birth_year = map(int, parts)
        elif '/' in self.date:
            parts = self.date.split('/')
            if len(parts[0]) == 4:
                # yyyy/mm/dd
                birth_year, birth_month, birth_day = map(int, parts)
            else:
                # dd/mm/yyyy
                birth_day, birth_month, birth_year = map(int, parts)
        else:
            raise ValueError(f"Ngày sinh không đúng định dạng chuẩn! Nhận được: {self.date}")
        current_date = date.today()
        birth_date = date(birth_year, birth_month, birth_day)
    
        age = current_date.year - birth_year + 1
        down_month = birth_date.month - 6 - current_date.month
        down_day = (current_date.day - birth_date.day)
        up_month = (current_date.month - ( birth_date.month + 6 ))
        up_day = (current_date.day - birth_date.day)

        if ( down_month > 0) or ( down_month == 0 and down_day < 0 ):
            age = age - 1
        if (up_month > 0) or (up_month == 0 and up_day >= 0):
            age = age + 1
            
        rate = ( self.a + self.b + self.c ) % 10
        default = 4
        number = (age) % 10

        default = ((number - rate) + default ) % 10
        if default == 0: default = 10 
        
        result_luu_nien = "A4e"+str(default)
        return [age, result_luu_nien]

    def house(self):
        mc = self.menh_cung()
        number_person = mc[0] % 10

        text = "Person"
        if number_person == 0:
            text1 = " A4h1 house number is 7 or 8"
            text2 = " A4h2 house number is 5 or 6 "
            text3 = " A4h3 house number is 4"
            text4 = " A4h4 house number is 9 or 0"

        if number_person == 1:
            text1 = " A4h1 house number is 0 or 9"
            text2 = " A4h2 house number is 7"
            text3 = " A4h3 house number is 5 or 6"
            text4 = " A4h4 house number is 1 or 2"

        if number_person == 2:
            text1 = " A4h1 house number is 0 or 9"
            text2 = " A4h2 house number is 7 or 8"
            text3 = " A4h3 house number is 6"
            text4 = " A4h4 house number is 1 or 2"

        if number_person == 3:
            text1 = " A4h1 house number is 1 or 2"
            text2 = " A4h2 house number is 9"
            text3 = " A4h3 house number is 7 or 8"
            text4 = " A4h4 house number is 3 or 4"

        if number_person == 4:
            text1 = " A4h1 house number is 1 or 2"
            text2 = " A4h2 house number is 9 or 0"
            text3 = " A4h3 house number is 8"
            text4 = " A4h4 house number is 3 or 4"


        if number_person == 5:
            text1 = " A4h1 house number is 3 or 4"
            text2 = " A4h2 house number is 1"
            text3 = " A4h3 house number is 9 or 0"
            text4 = " A4h4 house number is 5 or 6"

        if number_person == 6:
            text1 = " A4h1 house number is 3 or 4"
            text2 = " A4h2 house number is 1 or 2"
            text3 = " A4h3 house number is 0"
            text4 = " A4h4 house number is 5 or 6"

        if number_person == 7:
            text1 = " A4h1 house number is 5 or 6"
            text2 = " A4h2 house number is 3"
            text3 = " A4h3 house number is 1 or 2"
            text4 = " A4h4 house number is 7 or 8"

        if number_person == 8:
            text1 = " A4h1 house number is 5 or 6"
            text2 = " A4h2 house number is 3 or 4"
            text3 = " A4h3 house number is 2 "
            text4 = " A4h4 house number is 7 or 8"

        if number_person == 9:
            text1 = " A4h1 house number is 7 or 8"
            text2 = " A4h2 house number is 5"
            text3 = " A4h3 house number is 3 or 4"
            text4 = " A4h4 house number is 9 or 0"
        
        code_list = ["A4h1", "A4h2", "A4h3", "A4h4"]
        text_list = [text1, text2, text3, text4]
        return code_list, text_list
    

    def bad_year(self):

        def calculate_age_ranges(base_age, step=9, num_steps=10):
            # Tạo một dãy số cách đều bắt đầu từ base_age và tăng dần hoặc giảm dần theo step
            ages = [] 
            for i in range(-num_steps, num_steps + 1):
                ages.append((base_age+1) + i * step if i >= 0 else (base_age - 1) + i * step )
                result_age = [x for x in ages if 0 <= x <= 110]  # Tạo giá trị và thêm vào danh sách
            return result_age # bỏ base_age đi, lấy danh sách age từ nhỏ nhất.

        tu_nu = self.tu_nu_cung()
        tat_ach = self.tat_ach_cung()

        age_tat_ach = calculate_age_ranges(tat_ach[0])
        age_tu_nu = calculate_age_ranges(tu_nu[0])

        code_list = ["A4i1", "A4i2"]
        text_list = [age_tat_ach, age_tu_nu]
        return code_list, text_list

