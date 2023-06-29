def check_baggage(bw):
    if(bw>=0 and bw<=40):
        return True
    else:
        return False

def check_immigration(ey):
    if(ey>=2030 and ey<=2050):
        return True
    else:
        return False
    
def check_security(noc):
    if(noc.lower()=='valid'):
        return True
    else:
        return False
    
def traveller(t_id,t_name,bw,ey,noc):
    if(check_baggage(bw), check_immigration(ey), check_security(noc)):
        print(t_id)
        print(t_name)
        print("Allow traveller to fly!")
    else:
        print(t_id)
        print(t_name)
        print("Detain traveller for re-checking!")    
