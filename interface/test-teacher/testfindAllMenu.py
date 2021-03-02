import requests
import unittest

class FindAllMenuTest(unittest.TestCase):
      def testfindAllMenu(self):
          url = "http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllMenu"
          data = {

          }
          expect = 200

          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"
          code = response.status_code
          txt = response.text

          print(txt)
          self.assertEqual(expect, code)