target = 0x12345678

target1 = target >> 16
end = target & 0x0000FFFF
print(hex(target1), hex(end))