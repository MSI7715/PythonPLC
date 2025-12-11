import modbus_tk
import modbus_tk.defines as tkdef
import modbus_tk.modbus
import serial
from modbus_tk import modbus_rtu

com = 'COM10'


s = serial.Serial(port = com, baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1)
master = modbus_rtu.RtuMaster(s)
master.set_timeout(5.0)

try:  
    master.set_verbose(True)  
    value = master.execute(1, tkdef.READ_HOLDING_REGISTERS, 0, 3)
    print(value[0])
    master.execute(1, tkdef.WRITE_MULTIPLE_REGISTERS, 8, 1, [36])
    master.close()
except modbus_tk.exceptions.ModbusInvalidResponseError as err:
    print("Error Occur!\n", err)
