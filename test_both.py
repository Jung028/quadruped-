from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

def starting_pos(): 
    #-------------------------STARTING POSITION
    # LEFT BACK
    # elbow 
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 160

    # LEFT FRONT
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 135

    # RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 30
    # shoulder
    kit.servo[8].angle = 15

    # RIGHT FRONT
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)

    # ----------------------------- 




starting_pos()

#sitting
for _ in range(5):

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow


    # ----------------------------- POINT 2 (Left right and right back lift up )

    #LEFT BACK
    # elbow
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 160

    #LEFT FRONT
    # elbow
    kit.servo[3].angle = 140
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 133

    #RIGHT BACK
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 30
    # shoulder
    kit.servo[8].angle = 15

    #RIGHT FRONT
    # shoulder
    kit.servo[9].angle = 20
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 120


    time.sleep(1)

    # ----------------------------- 



    # ----------------------------- POINT 3 (Left right and right back touch bring forward and touch ground)

    #LEFT BACK 
    # elbow
    kit.servo[0].angle = 110
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 165

    #LEFT FRONT 
    # elbow
    kit.servo[3].angle = 70
    # shoulder
    kit.servo[4].angle = 120
    # inner 
    kit.servo[5].angle = 133


    #RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 100
    # shoulder
    kit.servo[8].angle = 50

    #RIGHT FRONT 
    # shoulder
    kit.servo[9].angle = 10
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 130

    time.sleep(1)

    # ----------------------------- 





    # ----------------------------- POINT 4 (Left right and right back push back ) 

    #LEFT BACK 
    kit.servo[0].angle = 90
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 175

    #LEFT FRONT 
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 160
    # inner 
    kit.servo[5].angle = 130

    #RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 20
    # elbow

    #RIGHT FRONT 
    # shoulder
    kit.servo[9].angle = 20
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 160

    time.sleep(1)

    # ----------------------------- 



    # ----------------------------- POINT 5 (Right front and left back lift up )
    
    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 70
# elbow
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 118
    # shoulder 
    kit.servo[2].angle = 160
   
    time.sleep(1)
       #LEFT FRONT 
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 170
    # inner 
    kit.servo[5].angle = 130

    #RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 10
    # elbow


 
  
    # ----------------------------- 



    # ----------------------------- POINT 6 (Right front and left back bring forward)

    #left back and right front bring forward

    # LEFT BACK 
    # elbow 
    kit.servo[0].angle = 130 # THIS 
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 130

    # LEFT FRONT
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    # RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 0

    # RIGHT FRONT
    # shoulder
    kit.servo[9].angle = 70
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 90 #THIS

    time.sleep(1)


    # ----------------------------- 




    # ----------------------------- POINT 7 (Right front and left back push back)
 
    # right front
    # shoulder
    kit.servo[9].angle = 10
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 180


   # LEFT FRONT
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    # RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 0

    time.sleep(1)
    # ----------------------------- 



    



 


 