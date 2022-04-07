#from pywinauto.application import Application
# app = Application(backend = "uia").start("notepad.exe")
#app = Application(backend = "uia").connect(title="RBS-DS-메모리-Emergency - Desktop Viewer")

import pywinauto as pwa
import sys
import time
import keyboard
# 특정 프로그램을 윈도우 Top으로 전환하는 함수
def setFocus(title_reg):
    app = pwa.application.Application()
    # title 이름 정규표현식
    t = title_reg
    print('find title : ' + str(title_reg))
    try:
        # title 을 기반으로 window handle 을 가져옴 
        handle = pwa.findwindows.find_windows(title_re=t)[0]
        # 해당 윈도우 Control을 위해 라이브러리와 연결
        app.connect(handle=handle)
        print('title: ' + str(t) + 'handle: ' + str(handle) + ' Setted')
    except:
        print('No title exist on window ')
        exit(5)
    # 어플리케이션의 window를 가져옴 
    window = app.window(handle=handle)
    try:
        # 해당 윈도우를 탑으로 설정 
        
        
        while True:
            window.set_focus()
            window.move_mouse(coords=(500, 500))
            window.click()
            window.send_keystrokes("{UP}{DOWN}")
            #window.minimize()
            
            window.send_keystrokes("dont like asb")
            time.sleep(10)  # 60 seconds
            print(".")
            if keyboard.is_pressed('q') : 
                print("\nkey In Ok, Exit")
                break
                

    except Exception as e:
        print('[error]setFocuse : ' + str(e))
    return window

def setFocusRBS():
    #  RBS 어플에 focus주기
    t = u'RBS-DS*'
    return setFocus(t)
if __name__=="__main__":
    setFocusRBS()