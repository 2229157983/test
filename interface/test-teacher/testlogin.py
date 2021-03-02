import requests
import unittest

class LoginTest(unittest.TestCase):
      def testlogin(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet"
          data = {
              "method":"login",
              "loginname":"root11",
              "password":"1111111"
          }
          expect = "菜单"
          response = requests.get(url=url,data = data)
          response.encoding = "utf-8"
          data = response.text

          self.assertIn(expect,data)