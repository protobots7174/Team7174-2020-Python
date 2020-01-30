import drivetrain
import wpilib
from math import pi
from ctre import WPI_TalonSRX

class MyRobot(wpilib.TimedRobot): 
    def robotInit(self):
        print("init")
        

        self.drivetrain = drivetrain.Drivetrain()
        # self.motor_test = WPI_TalonSRX(3)
        # self.motor_test2 = WPI_TalonSRX(4)
        
        # self.motor5 = WPI_TalonSRX(5)
        # self.motor6 = WPI_TalonSRX(6)
        # self.motor7 = WPI_TalonSRX(7)
        # self.motor8 = WPI_TalonSRX(8)
        # self.motor0 = WPI_TalonSRX(0)
       

        #self.motor.setInverted(True)
        self.encoderCPR = 2048 * 10.71 #one wheel rotation
        self.wheelDiameterFt = 6/12 #6 inches
        self.rightDistanceTraveledFt = 0
        self.leftDistanceTraveledFt = 0
        self.goalDistanceFt = 10

    def autonomousInit(self):
        print("auto init")

    def autonomousPeriodic(self):
        self.drivetrain.updateEncoderCount()
        print("encoders updated")
        self.leftDistanceTraveledFt = ((pi * self.wheelDiameterFt) / self.encoderCPR) * self.drivetrain.LeftEncoderCount
        self.rightDistanceTraveledFt = ((pi * self.wheelDiameterFt) / self.encoderCPR) * self.drivetrain.RightEncoderCount
    
        if self.rightDistanceTraveledFt < self.goalDistanceFt and self.leftDistanceTraveledFt < self.goalDistanceFt: 
            self.drivetrain.arcadeDrive(-.3,0)
            print("not there yet")
        else:
            self.drivetrain.arcadeDrive(0,0)
            print("arrived")
        print("auto periodic")

    def teleopInit(self): 
        print('init')
        self.controller = wpilib.XboxController(0)
    def teleopPeriodic(self):
        lJoyX = self.controller.getX(0)
        lJoyY = self.controller.getY(0)
        rJoyX = self.controller.getX(1)
        rJoyY = self.controller.getY(1)

        self.drivetrain.arcadeDrive(rJoyY,lJoyX)
        self.drivetrain.updateEncoderCount()
        self.drivetrain.printEncoderPosition()
        #   print(rJoyY)



if __name__ == "__main__":
    wpilib.run(MyRobot)