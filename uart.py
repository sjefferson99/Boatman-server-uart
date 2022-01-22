import serial

def start_uart():
  ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )
  return ser

def send(ser, skdata):
  ser.write(skdata.encode('utf-8'))
  return 0