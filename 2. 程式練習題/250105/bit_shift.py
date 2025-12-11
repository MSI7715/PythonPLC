value = 0x12345
print(hex(value))
value2 = value >> 16
print(hex(value2))
value3 = value & 0x0ffff
print(hex(value3))