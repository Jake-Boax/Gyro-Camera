import serial

ser = serial.Serial('/dev/ttyACM0')  # open serial port
def Read():
#while True:
    num = [0, 0, 0]   
    text = ser.readline()
    text = text.decode("utf-8")
    text = text.strip()
    text = text.split()
    num[0] = text[1]
    num[1] = text[3]
    num[2] = text[5]
    x = round((float(num[0]) + 15) *100)
    y = round((float(num[1]) + 15) *100)
    z = round((float(num[2]) + 15) *100)
    nums = [x, y, z]
    print(nums)
    return(nums)

Read()