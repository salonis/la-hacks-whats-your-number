import mraa  
import pyupm_i2clcd as lcd
import time
import unirest
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
display.clear()
display.setColor(159, 233, 237)
buttons = []
analogs = []
mapping = {9:0, 4:1, 3:2, 7:3, 6:4, 5:5, 8:6, 2:7, 1:8, 0:9}
mynum = 14089140368
for i in (4, 3, 2, 8, 7, 6, 5):
    buttons = buttons + [mraa.Gpio(i)]
for i in (0, 1,3):
    analogs = analogs + [mraa.Aio(i)]
#buttons = [mraa.Aio(3), mraa.Gpio(7), mraa.Gpio(8), mraa.Aio(0), mraa.Gpio(5),
endButton = mraa.Aio(2)
for button in buttons:
    button.dir(mraa.DIR_IN)
#for i in range(10):
#    if i != 0 and i != 3 and i!= 6:
#        buttons[i].dir(mraa.DIR_IN)
number = ''
last = time.time()                    
def sendText(message, recipient):
    response = unirest.post("https://twilio.p.mashape.com/ACb84b7b0c623e3af40003
        headers={                                                               
            "Authorization": "Basic QUNiODRiN2IwYzYyM2UzYWY0MDAwMzI5M2EzNjMyZjZj
            "X-Mashape-Key": "6xxzInhij6mshSN8h2oRc4HG9aNDp1VoTdbjsn32ZNtCAnb5gZ
            "Content-Type": "application/x-www-form-urlencoded",                
            "Accept": "text/plain"                              
        },                                                                      
        params={                                            
            "Body": message,                                                    
            "From": "(510) 270-4301",                                           
            "To": recipient #"15105792713"                      
        }                                                                       
    )                                
                                                                                
def updateLCD(info):                                                            
    global last                                                 
    elapsed = time.time() - last                                                
    if elapsed < .5:                
        time.sleep(.5 - elapsed)                                                
    display.clear()                                                             
    display.write(info)
while 1:                                                                        
    for i in range(10):                                         
        if endButton.read() > 500:                                              
            if len(number) > 0:                                                 
                display.clear()                                                 
                time.sleep(0.4)                                                 
                display.write("Sending...")                                     
                sendText("Someone just entered their number: " + str(number), my
                sendText("You just sent your number to: " + str(mynum), number) 
                display.clear()                                                 
                time.sleep(0.4)                                                 
                display.write("Sent! :)")                                       
                number = ''                                                    
        if  (i < 7 and (buttons[i].read())) or (i > 6 and analogs[i - 7].read() 
            #print buttons[i].read() + i                                       
            #while (buttons[i].read() - 1):                                     
            #    pass                                                           
            number = number + str(mapping[i])                                  
            display.clear()                                                     
            time.sleep(.1)                   
            display.write(number)                                               
            time.sleep(.9)                                                      
            #if len(number) == 10: 
            #    sendText(number)                                               
            print number          