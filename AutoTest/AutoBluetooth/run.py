"""
#####################################################################################
#
# Copyright (c) 2013 M.R.Z <zgd1348833@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#====================================================================================
#
#
#####################################################################################
"""
import time;
import sys;
#import pydoc;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

testCount = 1000
TAG = "AutoBluetooth"
DEBUG = 1
NOT_FOUND = -1

cmps=''
module='com.android.settings/com.android.settings.Settings'
androidL_module='com.android.settings/.bluetooth.BluetoothSettings'
OPEN_CLOSE_X = 368
OPEN_CLOSE_Y = 182

def checkParams():
	global OPEN_CLOSE_X
	global OPEN_CLOSE_Y
	global cmps
	dType = sys.argv[1]
	print "%s" %(dType)
	print "dType.length=%d" %(len(dType))

	# Just show all characters of get from args
	"""
	for i in range(0,len(dType)):
		print "dType[%d]=%c" %(i, dType[i])
	"""

	""" Modify for this just because sys.argv, which is get from shell,
	which contain some special non-display character
	"""
	tmp = dType
	if(NOT_FOUND != tmp.find("7060S")):
		OPEN_CLOSE_X = 340;
		OPEN_CLOSE_Y = 330;
		cmps = str(module)
	elif(NOT_FOUND != tmp.find("7061")):
		OPEN_CLOSE_X = 335;
		OPEN_CLOSE_Y = 325;
		cmps = str(module)
	elif(NOT_FOUND != tmp.find("FLY_FS502")):
		print "find SW07 in %s" %(tmp)
		OPEN_CLOSE_X = 370
		OPEN_CLOSE_Y = 220
		cmps = str(androidL_module)
	elif(NOT_FOUND != tmp.find("YourType")):
		""" If you want add devices, just modify bellow
		Add your device's position here.
		"""
		print "What you want to show"
	else:
		print "Why are you goto here"

def LOGD(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] %s: %s" %(t, TAG, msg)

def doClick(keycode, action):
	TAG = "doClick"
	LOGD(TAG, "Do " + keycode + " click " + action)
	device.press(keycode, action);
	MonkeyRunner.sleep(1);


#def main():
print "start"
checkParams()
device = MonkeyRunner.waitForConnection()
#width = MonkeyDevice.getProperty(display.width);
#height = MonkeyDevice.getProperty(display.height);
doClick('KEYCODE_BACK', 'DOWN_AND_UP');
doClick('KEYCODE_BACK', 'DOWN_AND_UP');
print "cmps = %s ,OPEN_CLOSE_X = %d ,OPEN_CLOSE_Y = %d" %(cmps,OPEN_CLOSE_X,OPEN_CLOSE_Y)
device.startActivity(component=cmps);
MonkeyRunner.sleep(2);
for i in range(0,testCount):
	MonkeyRunner.sleep(2);
	LOGD(TAG, str(i)+" click open and close 1st-click.")
	device.touch(OPEN_CLOSE_X,OPEN_CLOSE_Y,MonkeyDevice.DOWN_AND_UP);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	MonkeyRunner.sleep(2);
	LOGD(TAG, str(i)+" click open and close 2nd-click.")
	device.touch(OPEN_CLOSE_X,OPEN_CLOSE_Y,MonkeyDevice.DOWN_AND_UP);

