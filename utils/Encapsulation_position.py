
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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
       # print(id)
       # print(name)
       son='resourceId("{0}").childSelector(text(“{1}))'.format(id,name)
       #son= 'resourceId(\"' + id +'\").childSelector(text(\"' + name +'\"))'#需要研究一下为什么要这样写
       print(son)
       f=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_android_uiautomator(son))
       return f

   #通过xpath定位
   def findXpath(driver, xpath):
       f=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath(xpath))
       return f

   #通过content-desc1
   def findAI(driver, content_desc):
       f=WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_accessibility_id(content_desc))
       return


