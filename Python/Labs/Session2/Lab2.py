def SET_BIT(REG, BIT):
    REG = REG |(1<< BIT)
    return REG
def CLEAR_BIT(REG, BIT):
    REG = REG & (~(1<< BIT))
    return REG
def GET_BIT(REG, BIT):
    return ((REG >> BIT)&1)

def TOGGLE_BIT(REG, BIT):
    REG = REG ^(1<<BIT)
    return REG

Data = 7

print(Data) #Data = 7  0b0000 0111
Data = SET_BIT(Data, 3) #Set Bit 3, 0b0000 1111  =  15
print(Data)#Data = 15
Data = CLEAR_BIT(Data, 3)#Clear Bit 3, 0b0000 0111  =  7
print(Data)#Data = 7
Data = TOGGLE_BIT(Data, 3)#Toggle Bit 3, 0b0000 1111  =  15
print(Data)#Data = 15
BIT = GET_BIT(Data, 3)
print(BIT)#BIT = 1