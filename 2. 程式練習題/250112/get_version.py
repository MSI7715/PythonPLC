import serial
import modbus_tk
import modbus_tk.defines as modbusdef
import time
from modbus_tk import modbus_rtu

port = 'COM4'
master = modbus_rtu.RtuMaster(serial.Serial(port = port, baudrate = 19200, bytesize = 8, parity = 'N', stopbits = 0))
master.set_timeout(2.0)
master.set_verbose(True)
value = master.execute(3, modbusdef.READ_HOLDING_REGISTERS, 0x10f0, 1)
print(value)

#set_servo_on_off = 1 # 控制Servo開關狀態，0開啟/1關閉

def set_servo_on_off(servo_on_off):
    if servo_on_off:
        control = 0        
    else:
        control = 1
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2011, 1, [control])   

def set_ORG_on_off(ORG_on_off):
     master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2041, 1, 0)
     master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2041, 1, 1)

set_servo_on_off(True)
set_ORG_on_off()

# target = 3000 # 3cm

def move(target):
    end = target & 0xFFFF
    start = target >> 16
    # master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2002, 2, [start, end])
    # master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x201E, 1, [1])
    # 設定一個點位
    '''
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9010, 1, [1])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9011, 2, [start, end])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9013, 1[10])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9014, 1, [1000])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9016, 1, [0, 0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9018, 1, [0, 0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x901A, 1, [500])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x901B, 1, [500])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x901C, 1, [0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x901D, 1, [65535])
    '''

    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x9010, 11, [1, (start, end), 10, 1000, (0, 0), (0, 0), 500, 500, 0, 65535])

    # 第一個點位
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2044, 1, [0])
    '''
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2045, 1, [1])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2046, 1, [0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2047, 1, [0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2048, 1, [0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2049, 1, [0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x204A, 1, [0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x204B, 1, [0])
    '''
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2045, 7, [1, 0, 0, 0, 0, 0, 0])
    master.execute(3, modbusdef.WRITE_MULTIPLE_REGISTERS, 0x2044, 1, [1])

def move_fake(target):
    print("It is move", target)

move_motor = move_fake

move_motor(3000)
time.sleep(10)
move_motor(200)
time.sleep(0.1)
move_motor(10)
master.close()


