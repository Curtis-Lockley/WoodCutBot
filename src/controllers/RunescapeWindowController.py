import time

import pyautogui
import os
from pywinauto import Application
from pywinauto.keyboard import send_keys

WINDOW_WIDTH_PX = 2000;
WINDOW_HEIGHT_PX = 1000;

def openRunescape():
  #  app = Application().start("notepad.exe")
   # print("opened!")
    #app.window().move_window(0,0,WINDOW_WIDTH_PX,WINDOW_WIDTH_PX)
    #end_keys("Curtis_L",with_spaces=True )
    logs = []

    # prev = None
    # while True:
    #  loc = pyautogui.position()
    #  x = loc.x;
    #  y = loc.y;
    #
    #  print(loc)
    #  if prev:
    #    prevX = prev.x
    #    prevY = prev.y
    #    xDiff = abs(x - prevX)
    #    yDiff = abs(y - prevY)
    #    print("Diff: "+ str(xDiff) + ", " + str(yDiff))
    #
    #  prev = loc;
    #  input()

    matches = list(pyautogui.locateAllOnScreen("./assets/icons/Oak_logs_detail_scale_150.png",confidence=0.90))
    print(len(matches))
    for possibleLog in matches:
      x = possibleLog.left;
      y = possibleLog.top;
      conflictingLog = False
      for log in logs:
        logX = log.left;
        logY = log.top;

        xDiff = abs(x - logX);
        yDiff = abs(y - logY);
        if xDiff <= 60 and yDiff <= 50:
          conflictingLog = True
          break
      if not conflictingLog:
        logs.append(possibleLog)


    print(len(logs))
    for log in logs:
      print("moving to log")
      x = log.left
      y = log.top
      pyautogui.moveTo(x,y)
      time.sleep(1)



