from selenium import webdriver

driver = webdriver.Chrome('D:/dev/chromedriver_win32/chromedriver.exe')

driver.get('https://www.ddanzi.com/?mid=login&act=dispMemberLoginForm')

driver.find_element_by_name('user_id').send_keys('tetra3')
driver.find_element_by_name('password').send_keys('~gnqlwjr1')

driver.find_element_by_id('regularsubmit').click()



#목표를 정하자
#목표는 바로 딴지일보를 똑같이 자동댓글 달도록 코딩을 하는 것이다.
