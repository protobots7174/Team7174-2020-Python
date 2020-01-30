import wpilib
import wpilib.drive
from ctre import WPI_TalonSRX


class Drivetrain:
	def __init__(self):		
		self.LF = WPI_TalonSRX(1)
		self.LR = WPI_TalonSRX(2) 
        #self.LF.setInverted(True)

		self.RF = WPI_TalonSRX(3)
		self.RR = WPI_TalonSRX(4)
		self.left = wpilib.SpeedControllerGroup(self.LF,self.LR)
		self.right = wpilib.SpeedControllerGroup(self.RF, self.RR)
        #self.RF.setInverted(True)

		self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
		self.drive.setSafetyEnabled(True)

		self.LeftEncoderCount = 0
		self.RightEncoderCount = 0
		self.PrevLeftEncoderCount = self.LF.getSelectedSensorPosition()
		self.PrevRightEncoderCount = self.RF.getSelectedSensorPosition()

	def arcadeDrive(self,speed,angle):
		self.drive.setSafetyEnabled(True)
		self.drive.arcadeDrive(speed,angle)

	def updateEncoderCount(self):
		currentEncoderCount = self.LF.getSelectedSensorPosition()
		self.LeftEncoderCount += currentEncoderCount - self.PrevLeftEncoderCount
		self.PrevLeftEncoderCount = currentEncoderCount

		currentEncoderCount = self.RF.getSelectedSensorPosition()
		self.RightEncoderCount += currentEncoderCount - self.PrevRightEncoderCount
		self.PrevRightEncoderCount = currentEncoderCount
	def printEncoderPosition(self):
		
		print(self.LeftEncoderCount)
		print(self.RightEncoderCount)

