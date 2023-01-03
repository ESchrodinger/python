from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

# 百度实战
# url = "https://www.baidu.com"
# driver.get(url)
# driver.maximize_window()
# tag = driver.find_elements_by_tag_name("input")
# 可以使用find_element_……等等方法进行定位元素

# driver.find_element_by_id("kw").send_keys("python中单引号和双引号")
# driver.find_element("id", "kw").send_keys("python中单引号和双引号")
# driver.find_element_by_xpath("//form[@id='from']/span/input").send_keys("你好啊")
# driver.find_element("id", "su").click()

# for t in tag:
#     if t.get_attribute("autocomplete") == "off":
#         t.send_keys("江哥最帅")
# driver.find_element("id", "su").click()
# sleep(5)
# 停止五秒
# driver.quit()


# 定位进行注册简书
# driver.get("https://www.jianshu.com/sign_in")
# sleep(2)
# # 定位注册按钮
# js_register = 'document.getElementById("js-sign-up-btn").click()'
# driver.execute_script(js_register)
# sleep(2)

# 使用jQuery定位进行登录操作
# 成功但是需要人工验证
# driver.get("https://www.jianshu.com/sign_in")
# js_login = 'document.getElementsByClassName("active")[0].click();'
# sleep(2)
# driver.execute_script(js_login)
# js_input = 'document.getElementsByTagName("input")[2].value="13712666109";'
# driver.execute_script(js_input)
# js_password = 'document.getElementsByTagName("input")[3].value="Lzj13712189180";'
# driver.execute_script(js_password)
# js_clickLogin = 'document.querySelectorAll(".sign-in-button")[0].click();'
# driver.execute_script(js_clickLogin)

# 进行鼠标操作实战
driver.get("https://www.baidu.com")
driver.maximize_window()

# 这里使用了actionChains
# 1、打开百度的搜索设置(失败)
# setting = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(setting).perform()
# sleep(1)
# driver.find_element_by_link_text("搜索设置").click()
# # driver.find_element_by_link_text("学术").click()
# sleep(5)

# 2、鼠标右键
# context = driver.find_element_by_id("su")
# ActionChains(driver).context_click().perform()
# sleep(5)

# 3、鼠标双击
driver.find_element_by_id('kw').send_keys("双击一下")
searchBtn = driver.find_element_by_id('su')
ActionChains(driver).double_click(searchBtn).perform()
sleep(5)
