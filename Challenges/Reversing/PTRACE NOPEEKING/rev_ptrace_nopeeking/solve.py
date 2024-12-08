import operator
import struct

def unpack_dwords(data):
    count = len(data) >> 2

    result = []

    for index in range(count):
        result.append(struct.unpack('<l', data[index*4:index*4+4])[0])

    return result


data = b''

with open('nopeeking', 'rb') as f:
    data = f.read()

bits = unpack_dwords(data[0x2020:0x208c])

data_1 = unpack_dwords(data[0x20e0:0x2118])
data_2 = unpack_dwords(data[0x20a0:0x20d4])

result = ''

index_1 = 0
index_2 = 0

for (i, b) in enumerate(bits):
    v = 0
    if b == 0:
        v = data_2[index_1]
        index_1 += 1
    else:
        v = data_1[index_2]
        index_2 += 1

    mask = operator.and_(0xff, 0x2c * i)

    res = operator.xor(mask, v) - 0x1a + i + 1

    result += chr(res)

print(result)
