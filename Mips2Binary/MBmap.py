'''
Map
'''

import re

INDETERMINACY_BINARY_CODE = 'XXXXXX'

Mips2BinaryMap = {
    'add': '000000',
    'sub': '000001',
    'addiu': '000010',
    'and': '010000',
    'andi': '010001',
    'ori': '010010',
    'xori': '010011',
    'sll': '011000',
    'slti': '100110',
    'slt': '100111',
    'sw': '110000',
    'lw': '110001',
    'beq': '110100',
    'bne': '110101',
    'bltz': '110110',
    'j': '111000',
    'jr': '111001',
    'jal': '111010',
    'halt': '111111',
    'or': INDETERMINACY_BINARY_CODE
}

InstructionType = {
    'add': 'R',
    'sub': 'R',
    'addiu': 'I',
    'and': 'R',
    'andi': 'I',
    'ori': 'I',
    'xori': 'I',
    'sll': 'R',
    'slti': 'I',
    'slt': 'R',
    'sw': 'I',
    'lw': 'I',
    'beq': 'I',
    'bne': 'I',
    'bltz': 'I',
    'j': 'J',
    'jr': 'J',
    'jal': 'J',
    'halt': 'J',
    'or': 'R',
}

Binary2MipsMap = {
    '000000': 'add',
    '000001': 'sub',
    '000010': 'addiu',
    '010000': 'and',
    '010001': 'andi',
    '010010': 'ori',
    '010011': 'xori',
    '011000': 'sll',
    '100110': 'slti',
    '100111': 'slt',
    '110000': 'sw',
    '110001': 'lw',
    '110100': 'beq',
    '110101': 'bne',
    '110110': 'bltz',
    '111000': 'j',
    '111001': 'jr',
    '111010': 'jal',
    '111111': 'halt'
}


def create_map():
    '''
    在单方面地修改 mips 到 二进制 代码的映射后,
    在本代码文件中, 执行此函数,
    会把更新的 二进制 到 mips 的新映射的字符串(字典) 追加到文件末尾.
    本函数功能不全, 待完善.
    '''
    string = ""
    for key in Mips2BinaryMap:
        string += f"    "
        string += f"'" + Mips2BinaryMap.get(key) + f"'"
        string += " : " + f"'" + key + f"'" + ',' + '\n'
    with open(__file__, 'a') as f:
        f.write("\nBinary2MipsMap =" + "{\n" + string + "}")


class ParseError(Exception):
    def __init__(self):
        super(ParseError, self).__init__()
        self.message = "ParseError"

    def __str__(self):
        return self.message

    def getMessage(self):
        return self.message


def D2B(decimal, num=8):
    try:
        d = int(decimal)
        if 0 <= d < (2 ** num):
            return (str(bin(d))[2:].zfill(num))
        else:
            raise ParseError
    except:
        raise ParseError


def D2Bcomplement(decimal, num=8):
    try:
        d = int(decimal)
        if 0 <= d < (2 ** (num - 1)):
            return (str(bin(d))[2:].zfill(num))
        elif -(2 ** (num - 1)) <= d < 0:
            return (str(bin((2 ** num) + d))[2:])
        else:
            raise ParseError
    except:
        raise ParseError


def D2H(deciaml, num=2):
    return B2H(D2B(deciaml, num * 4), num)


def D2Hcomplememt(decimal, num=2):
    return B2H(D2Bcomplement(decimal, num * 4), num)


def B2H(binary, num=8):
    try:
        binary = binary.replace(' ', '')
        if re.search('[^01]', binary):
            return 'ParseError'
        else:
            return hex(int('0b' + binary, 2))[2:].zfill(num)
    except:
        return 'ParseError'


def H2B(hex, num=8):
    try:
        hex = hex.replace(' ', '')
        if re.search('[^0-9A-Ea-e]', hex):
            return 'ParseError'
        else:
            return bin(int('0x' + hex, 16))[2:].zfill(num)
    except:
        return 'ParseError'


def getType(mips_opcode):
    type = InstructionType.get(mips_opcode)
    if type is not None:
        return type
    else:
        raise ParseError


def getBinaryOp(mips_opcode):
    return Mips2BinaryMap.get(mips_opcode)


def getBinaryFunc(mips_func):
    return '000000'  # 6个0


def getBinarySa(mips_sa):
    return D2B(mips_sa, 5)


def getBinaryRs(mips_rs):
    return D2B(mips_rs[1:], 5)


def getBinaryRt(mips_rt):
    return D2B(mips_rt[1:], 5)


def getBinaryRd(mips_rd):
    return D2B(mips_rd[1:], 5)


def getBinaryImm16(mips_imm16):
    return D2Bcomplement(mips_imm16, 16)


def getBinaryImm26(mips_imm26):
    if mips_imm26[0:2] == '0x' or mips_imm26 == '0X':
        return H2B(mips_imm26[2:], 26)
    else:
        return D2Bcomplement(mips_imm26, 26)


def isShiftInstruction(mips_opcode):
    si_opcode = ('sll', 'srl')
    return (mips_opcode in si_opcode)


def isBranchInstruction(mips_opcode):
    bi_opcode = ('beq', 'bne', 'bltz')
    return (mips_opcode in bi_opcode)


def isMemInstruction(mips_opcode):
    mi_opcode = ('sw', 'lw')
    return (mips_opcode in mi_opcode)


def isALUopInstruction(mips_opcode):
    ai = ('addiu', 'addi', 'subi', 'andi', 'ori', 'xori', 'slti', 'add', 'sub', 'and', 'or', 'xor', 'slt')
    return (mips_opcode in ai)


def isJumpInstruction(mips_opcode):
    ji = ('j', 'jr', 'jal', 'halt')
    return (mips_opcode in ji)


def parseRtype(mips_list):
    if (len(mips_list) == 4) and (mips_list[1][0] == mips_list[2][0] == '$'):
        if isALUopInstruction(mips_list[0]) and mips_list[3][0] == '$':
            op = getBinaryOp(mips_list[0])
            rs = getBinaryRs(mips_list[1])
            rt = getBinaryRt(mips_list[2])
            rd = getBinaryRd(mips_list[3])
            sa = getBinarySa('00000')  # 5个0
            func = getBinaryFunc(mips_list[0])
        elif isShiftInstruction(mips_list[0]):
            print('sa')
            op = getBinaryOp(mips_list[0])
            rs = getBinaryRs('00000')
            rt = getBinaryRt(mips_list[2])
            rd = getBinaryRd(mips_list[1])
            sa = getBinarySa(mips_list[3])
            func = getBinaryFunc(mips_list[0])
        else:
            raise ParseError
        return (op + ' ' + rs + ' ' + rt + ' ' + rd + ' ' + sa + ' ' + func)
    else:
        raise ParseError


def parseItype(mips_list):
    if (len(mips_list) == 3) and (mips_list[1][0] == '$'):
        if isBranchInstruction(mips_list[0]):
            op = getBinaryOp(mips_list[0])
            rs = getBinaryRs(mips_list[1])
            rt = getBinaryRt('00000')
            imm16 = getBinaryImm16(mips_list[2])
        elif isMemInstruction(mips_list[0]):
            op = getBinaryOp(mips_list[0])
            rs = getBinaryRs((re.findall(r'[(](.*?)[)]', mips_list[2]))[0])
            rt = getBinaryRt(mips_list[1])
            imm16 = getBinaryImm16(re.sub(r'[(](.*?)[)]', "", mips_list[2]))
        else:
            raise ParseError

        return (op + ' ' + rs + ' ' + rt + ' ' + imm16)

    elif (len(mips_list) == 4) and (mips_list[1][0] == mips_list[2][0] == '$'):
        if isBranchInstruction(mips_list[0]):
            op = getBinaryOp(mips_list[0])
            rs = getBinaryRs(mips_list[1])
            rt = getBinaryRt(mips_list[2])
            imm16 = getBinaryImm16(mips_list[3])
        elif isALUopInstruction(mips_list[0]):
            op = getBinaryOp(mips_list[0])
            rs = getBinaryRs(mips_list[2])
            rt = getBinaryRs(mips_list[1])
            imm16 = getBinaryImm16(mips_list[3])
        else:
            raise ParseError

        return (op + ' ' + rs + ' ' + rt + ' ' + imm16)
    else:
        raise ParseError


def parseJtype(mips_list):
    if len(mips_list) == 2 and isJumpInstruction(mips_list[0]):
        if mips_list[0] == 'jr' and mips_list[1][0] == '$':
            j = getBinaryOp(mips_list[0])
            addr = getBinaryRs(mips_list[1]) + ' ' + D2B('0', 21)
        elif mips_list[0] in ('j', 'jal'):
            j = getBinaryOp(mips_list[0])
            addr = getBinaryImm26(mips_list[1])
        else:
            raise ParseError

        return (j + ' ' + addr)
    elif len(mips_list) == 1 and mips_list[0] == 'halt':
        j = getBinaryOp(mips_list[0])
        addr = getBinaryImm26('0')

        return (j + ' ' + addr)
    else:
        raise ParseError


def M2B(mips):
    binary = ""
    try:
        mips = mips.replace(',', ' ')
        mips_list = mips.split()  # 按空格切分
        type = getType(mips_list[0])
        if type == 'R':
            binary = parseRtype(mips_list)
        elif type == 'I':
            binary = parseItype(mips_list)
        elif type == 'J':
            binary = parseJtype(mips_list)
        else:
            raise ParseError
    except Exception as e:
        binary = "ParseError"
    return binary


if __name__ == '__main__':
    pass
