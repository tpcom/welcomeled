from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] or "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
while True:
    ser.write("2".encode())
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) #显示当前坐标
    #检测四周的9块区域是否有亮的红石灯
    for x in range(3):
        for z in range(3):
           if mc.getBlock(pos.x-1+x,pos.y,pos.z-1+z)==124:
               print("red stone ligh found")
               ser.write("y".encode()) 
    if pos.x<-11 and pos.x>-22 and pos.y==131 and pos.z<=254 and pos.z>244:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        #回到家给串口送一个y，arduino收到串口点亮一盏led
        ser.write("1".encode())
        print("1 send")
        time.sleep(1)
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
            #回到家给串口送一个g，arduino收到串口点亮另一盏led
            ser.write("g".encode())
            print("g send")
            time.sleep(1)
    else:
        stayed_time=0
        
     
