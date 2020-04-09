from appium import webdriver
import time
import yaml

file = open('data.yaml',encoding='utf-8')
data = yaml.load(file,yaml.FullLoader)
notes = data.get('revenue and expenditure notes')

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "192.168.1.1:5555"
caps["appPackage"] = "com.yuukidach.ucount"
caps["appActivity"] = ".MainActivity"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)
for key in notes:
    el1 = driver.find_element_by_id("com.yuukidach.ucount:id/add_button")
    el1.click()
    if key=='revenue':
        print('收入,执行点击收入按钮')
        el2 = driver.find_element_by_id("com.yuukidach.ucount:id/add_earn_button")
        el2.click()
        money = notes[key]['money']
        str_money = str(money);
        user = notes[key]['user']
        id = notes[key]['id']
        detail = notes[key]['detail']
        print(detail)
        if(detail=='工资'):
            print('点击工资按钮')
            el3 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView")
            el3.click()
            for str_i in str_money:
                print(str_i)
                i = int(str_i)
                button_id = ''
                print(i)
                if i%10 == 1:
                    button_id = 'one'
                elif i%10 == 2:
                    button_id = 'two'
                elif i%10 == 3:
                    button_id = 'three'
                elif i%10 == 4:
                    button_id = 'four'
                elif i%10 == 5:
                    button_id = 'five'
                elif i%10 == 6:
                    button_id = 'six'
                elif i%10 == 7:
                    button_id = 'seven'
                elif i%10 == 8:
                    button_id = 'eight'
                elif i%10 == 9:
                    button_id = 'nine'
                elif i%10 == 0:
                    button_id = 'zero'
                else:button_id = 'dot'
                el_temp = driver.find_element_by_id("com.yuukidach.ucount:id/"+str(button_id))
                el_temp.click()
            el6 = driver.find_element_by_id("com.yuukidach.ucount:id/add_description")
            el6.click()
            el7 = driver.find_element_by_id("com.yuukidach.ucount:id/page3_edit")
            el7.click()
            el7.send_keys('姓名：'+user+' '+'学号：'+id+' '+'获得工资：'+str_money)
            el8 = driver.find_element_by_id("com.yuukidach.ucount:id/page3_done")
            el8.click()
            el9 = driver.find_element_by_id("com.yuukidach.ucount:id/add_finish")
            el9.click()
            time.sleep(5)
    elif key=='expenditure':
        print('支出')
        el11 = driver.find_element_by_id("com.yuukidach.ucount:id/add_cost_button")
        el11.click()
        money = notes[key]['money']
        str_money = str(money);
        user = notes[key]['user']
        id = notes[key]['id']
        detail = notes[key]['detail']
        print(detail)
        if(detail=='用餐'):
            print('点击用餐按钮')
            el3 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView")
            el3.click()
            for str_i in str_money:
                print(str_i)
                i = int(str_i)
                button_id = ''
                print(i)
                if i%10 == 1:
                    button_id = 'one'
                elif i%10 == 2:
                    button_id = 'two'
                elif i%10 == 3:
                    button_id = 'three'
                elif i%10 == 4:
                    button_id = 'four'
                elif i%10 == 5:
                    button_id = 'five'
                elif i%10 == 6:
                    button_id = 'six'
                elif i%10 == 7:
                    button_id = 'seven'
                elif i%10 == 8:
                    button_id = 'eight'
                elif i%10 == 9:
                    button_id = 'nine'
                elif i%10 == 0:
                    button_id = 'zero'
                else:button_id = 'dot'
                el_temp = driver.find_element_by_id("com.yuukidach.ucount:id/"+str(button_id))
                el_temp.click()
            el6 = driver.find_element_by_id("com.yuukidach.ucount:id/add_description")
            el6.click()
            el7 = driver.find_element_by_id("com.yuukidach.ucount:id/page3_edit")
            el7.click()
            el7.send_keys('姓名：'+user+' '+'学号：'+id+' '+'用餐支出：'+str_money)
            el8 = driver.find_element_by_id("com.yuukidach.ucount:id/page3_done")
            el8.click()
            el9 = driver.find_element_by_id("com.yuukidach.ucount:id/add_finish")
            el9.click()
            time.sleep(5)
        el19 = driver.find_element_by_id("com.yuukidach.ucount:id/show_money_button")
        el19.click()
        assert (float(el19.get_attribute("text")) == 4700.00)
# driver.background_app(5)
time.sleep(5)
driver.quit()