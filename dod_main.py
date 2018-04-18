from PIL import ImageGrab
import cv2
import numpy as np
import time
import win32api
import win32con


def CatchImg():
	imSize = (0, 0, 450, 400)
	im = np.array(ImageGrab.grab(imSize))
	# print(im.shape)
	# im_rgb = [[ im[i,j][::-1] for j in range(im.shape[0]) ] for i in range(im.shape[1])]
	# im = np.array(im_rgb)
	return im

def isSame(img1, img2):
	difference = cv2.subtract(img1, img2)
	return not np.any(difference)

def Main(window_name='main'):
	cv2.namedWindow(window_name)
	
	preImg = CatchImg()
	hasRead = False
	while True:
		key = cv2.waitKey(1000) & 0xFF
		if key == 27:
			break

		nowImg = CatchImg()
		cv2.imshow(window_name, nowImg)

		if isSame(preImg, nowImg):
			print('same...')
			hasRead = False
		else:
			if not hasRead:
				print('different')
				keyboardInput()
				hasRead = True
		preImg = nowImg

	cv2.destroyAllWindows()

def keyboardInput():

	# tab键
	win32api.keybd_event(9,0,0,0)
	win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
	# print('tab')

	# ↑键
	win32api.keybd_event(38,0,0,0)
	win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)
	# print('↑')

	# 右键
	win32api.keybd_event(0x5D,0,0,0)
	win32api.keybd_event(0x5D,0,win32con.KEYEVENTF_KEYUP,0)
	time.sleep(0.2)
	# print('right')

	# c键
	win32api.keybd_event(67,0,0,0)
	win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0)
	time.sleep(0.2)
	# print('c')

	# ctrl+v
	win32api.keybd_event(17,0,0,0)
	win32api.keybd_event(86,0,0,0)
	win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
	# print('ctrl+v')

	# 回车键
	win32api.keybd_event(13,0,0,0)
	win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
	# print('回车')

if __name__ == '__main__':
	time.sleep(2)
	Main('testing')