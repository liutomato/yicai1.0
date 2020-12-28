
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver

class Action(object):
   #通过resource-i定位
   def findId(driver, id):
       f=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_id(id))
       return f

   #通过class定位
   def findClassName(driver, name):
     f=WebDriverWait(driver,30).until(lambda driver:driver.find_elment_by_class_name(name))
     return f

   #通过text定位
   def findAU(driver, name):
       f=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_android_uiautomator('text(\"' + name +'\")'))
       return f

   #通过父子定位
   def findChild(driver,id,name):
       # 报错的代码：son = 'resourceId("{0}").childSelector(text(“{1}))'.format(id, name)
       son='resourceId("{0}").childSelector(text("{1}"))'.format(id,name)
       #son= 'resourceId(\"' + id +'\").childSelector(text(\"' + name +'\"))'#需要研究一下为什么要这样写
       f=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_android_uiautomator(son))
       return f

   #通过xpath定位
   def findXpath(driver, xpath):
       print(xpath)
       f=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath(xpath))
       print(f)
       return f

   #通过content-desc定位
   def findAI(driver, content_desc):
       f=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_accessibility_id(content_desc))
       return f

   #精准坐标点滑动
   def swipepoint(driver,x1,y1,x2,y2):
       WebDriverWait(driver,30).until(lambda driver:driver.swipe(x1, y1, x2, y2, duration=1000))

   #向上滑动屏幕
   def swipeUp(driver):
       t=500
       n=1
       l = driver.get_window_size()
       x1 = l['width'] * 0.5
       y1 = l['height'] * 0.75
       y2 = l['height'] * 0.25
       for i in range(n):
           driver.swipe(x1, y1, x1, y2, t)
   # #向下滑动屏幕
   # def swipeDown(driver, t=500, n=1):
   #     '''向下滑动屏幕'''
   #     l = driver.get_window_size()
   #     x1 = l['width'] * 0.5
   #     y1 = l['height'] * 0.25
   #     y2 = l['height'] * 0.75
   #     for i in range(n):
   #         driver.swipe(x1, y1, x1, y2, t)
   #
   # #向左滑动屏幕
   # def swipLeft(driver, t=500, n=1):
   #     l = driver.get_window_size()
   #     x1 = l['width'] * 0.75
   #     y1 = l['height'] * 0.5
   #     x2 = l['width'] * 0.25
   #     for i in range(n):
   #         driver.swipe(x1, y1, x2, y1, t)
   #
   # #向右滑动屏幕
   # def swipRight(driver, t=500, n=1):
   #     l = driver.get_window_size()
   #     x1 = l['width'] * 0.25
   #     y1 = l['height'] * 0.5
   #     x2 = l['width'] * 0.75
   #     for i in range(n):
   #         driver.swipe(x1, y1, x2, y1, t)


