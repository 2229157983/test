import requests
import unittest

class FindAllStudentTest(unittest.TestCase):
      def testfindAllStudent(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
          data = {

          }
          expect = 200

          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"
          code = response.status_code
          txt = response.text

          print(txt)
          self.assertEqual(expect, code)