import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 使用 pytest fixture 来启动和结束 Appium 会话
@pytest.fixture(scope='module')
def driver():
    # 设置 UiAutomator2Options 配置
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.android.chrome',  # 确保这是正确的应用包名
        'appActivity': 'com.google.android.apps.chrome.Main',  # 确保这是正确的 Activity 名称
        'noReset': True  # 防止 Appium 清除数据
    })

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    yield driver  # 使得 driver 在测试用例执行后自动释放资源

    driver.quit()  # 测试完成后关闭 Appium 会话

def test_open_chrome(driver):
    driver.implicitly_wait(10)  # 等待应用加载
    driver.activate_app('com.android.chrome')  # 使用 activate_app 来启动应用

    # 获取当前活动并验证应用是否成功启动
    current_activity = driver.current_activity
    assert current_activity == 'com.google.android.apps.chrome.Main', f"Expected to open Chrome, but opened {current_activity}"
