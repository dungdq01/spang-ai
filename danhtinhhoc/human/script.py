MOC=0
HOA=1
THO=2
KIM=3
THUY=4

ngu_hanh = [THUY, MOC, MOC, HOA,HOA, THO, THO, KIM, KIM, THUY] 

def check_sinh(i,j):
    sinhkhac = (j-i+5)%5
    name = ["binh", "sinh", "khac", "bi_khac", "duoc_sinh"]
    return name[sinhkhac] 