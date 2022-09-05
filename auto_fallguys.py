import os
import pyautogui as pgui
import time
import win32gui
import win32con

path_picdir = "auto_fallguys\pic\\"

# Image check
def ky(chk_imgpath, sKey, cd = 0.7):
    if pgui.locateOnScreen(chk_imgpath, confidence = cd) is not None:
        k(sKey)

# Key input
def k(sKey):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    print("key operation : " + sKey + " down")
    pgui.keyDown(sKey)
    time.sleep(0.1)
    pgui.keyUp(sKey)

print("auto_fallguys start")
hwnd = win32gui.FindWindow(None, 'FallGuys_client')
win_x1,win_y1,win_x2,win_y2 = win32gui.GetWindowRect(hwnd)
print(u"app coordinates : "+str(win_x1)+"/"+str(win_y1))
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

match_counter = 1
time_counter = 0

while(1):

    ky(os.path.join(path_picdir, 'play1.jpg'), 'enter', 0.8)  
    time.sleep(0.1)
    ky(os.path.join(path_picdir, 'OK_big.jpg'), 'enter', 0.8)
    time.sleep(0.1)

    # Match count, match time measurement
    if pgui.locateOnScreen('auto_fallguys\pic\qualified.jpg', confidence = 0.8) is not None and time_counter == 0:
            print("In play")
            t1 = time.time()
            time_counter += 1

    # Match end processing
    if pgui.locateOnScreen('auto_fallguys\pic\クリア.jpg', confidence = 0.8) is not None:
        print("Match end processing start")
        t2 = time.time()
        elapsed_time = t2 - t1
        print(f"elapsed_time : {elapsed_time}")
        print("number of plays : " + str(match_counter))
        time_counter = 0
        match_counter += 1
        t1 = 0
        t2 = 0
        
        while(1):
            ky(os.path.join(path_picdir, 'Esc.jpg'), 'esc', 0.8)
            time.sleep(0.1)
            ky(os.path.join(path_picdir, 'OK_small.jpg'), 'enter', 0.8)
            time.sleep(0.1)
            ky(os.path.join(path_picdir, 'OK_big.jpg'), 'enter', 0.8)
            time.sleep(0.1)
            if pgui.locateOnScreen('auto_fallguys\pic\決定.jpg', confidence = 0.8) is not None:
                ky(os.path.join(path_picdir, '決定.jpg'), 'enter', 0.8)
                print("Match end processing end")
                break          

    time.sleep(0.1)