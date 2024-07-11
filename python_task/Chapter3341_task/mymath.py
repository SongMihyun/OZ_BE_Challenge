pi = 3.14
    

def tri_area(x:float, y:float)->float:
    tri_area = x * y / 2
    return float(tri_area)
    
def cir_area(r:float) ->float:
    cir_area = r*2*pi
    return float(cir_area)
    
def rect_area(x:float, y:float, z:float)->float:
    rect_area = 2*((x*y)+(x*z)+(y*z))
    return float(rect_area)