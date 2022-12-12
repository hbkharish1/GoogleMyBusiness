
import hmac,base64,struct,hashlib,time
from selenium.webdriver.common.by import By

url = "https://www.google.com/"
# user_name = "corporatesales@poorvika.in"
# password = "corporate@3456"
# user_name = "poorvikacampaign@gmail.com"
# password = "PVK@Gmail1"
user_name = "dev@poorvika.in"
password = "Prdev@1855"
secret = 'amtjdiqegq5ekxt36wgul6wthce5pkdw'


class Google:
    def __init__(self, driver):
        self.driver = driver

    def next_button(self):
        for next_username in self.driver.find_elements(By.CLASS_NAME, "VfPpkd-vQzf8d"):
            if next_username.text == "Next":
                # print(next_username.text)
                next_username.click()
                break
        time.sleep(5)
        self.driver.implicitly_wait(3)

    def username(self):
        self.driver.find_element(By.TAG_NAME, "input").send_keys(user_name)
        Google.next_button(self)
        # time.sleep(15)

    def user_pass(self):

        self.driver.find_element(By.CLASS_NAME,"whsOnd").send_keys(password)
        Google.next_button(self)

    # def Authentication(self):
    #     try:
    #         self.driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
    #         print("firstway")
    #     except:
    #         try:
    #             self.driver.find_element(By.CLASS_NAME,"YZVTmd").click()
    #             print("anotherway")
    #         except:
    #             pass

    # def Popup(self):
    #     self.driver

    def get_token(secret,intervals_no = None):
        if intervals_no == None:
            intervals_no = int(time.time()) // 30
        key = base64.b32decode(secret, True)
        msg = struct.pack(">Q", intervals_no)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = h[19] & 15
        h = (struct.unpack(">I", h[o:o + 4])[0] & 0x7fffffff) % 1000000
        otp = str(h)
        # if len(str(h)) < 6:
        #     print("if")
        #     h = str(h)
        #     return h.zfill(6)
        # else:
        #     return h
        return otp.zfill(6)

    def Auth(self):
        key = Google.get_token(secret)
        for authkey in self.driver.find_elements(By.CLASS_NAME,"Xb9hP"):
            authkey.find_element(By.TAG_NAME, "input").send_keys(key)
            Google.next_button(self)

    def login(self):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        # self.driver.find_element(By.CLASS_NAME,"gb_2").click()
        self.driver.find_element(By.CLASS_NAME,"gb_7").click()
        self.driver.implicitly_wait(5)
        Google.username(self)
        # self.driver.implicitly_wait(5)
        # time.sleep(2)
        Google.user_pass(self)
        # Google.Authentication(self)
        Google.Auth(self)
        print("Google My business Login")
        time.sleep(2)







