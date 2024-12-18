#Registers
#20
a = 222018648
b = 0
c = 0

sol = ''

def combo_operand(val:int) -> int:
    if 0 <= val <= 3:
        return val
    elif val == 4:
        return a
    elif val == 5:
        return b
    elif val == 6:
        return c

def parse_instruction(opcode:int, val:int):
    global a,b,c
    global sol
    match opcode:
        #Division
        case 0:
            a = a//2**combo_operand(val)
        #Bitwise XOR between register and literal operand
        case 1:
            b = b^val
        #Modulo 8
        case 2:
            b = combo_operand(val)%8
        #Jump
        case 3:
            if a != 0:
                return val
        #XOR between register B and C
        case 4:
            b = b^c
        #Out
        case 5:
            sol += str(combo_operand(val)%8) + ','
        #Division (but store result in b)
        case 6:
            b = a//2**combo_operand(val)
        #Division (but store result in c)
        case 7:
            c = a//2**combo_operand(val)
    return -1


def read_program(code:str):
    i = 0
    while i < len(code):
        instruction = int(code[i])
        operator = int(code[i+1])
        ret = parse_instruction(instruction, operator)
        if ret == -1:
            i += 2
        else:
            i = ret



read_program('2416754614550330')
print(sol)