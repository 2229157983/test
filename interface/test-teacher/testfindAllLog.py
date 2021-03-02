import requests
import unittest

class FindAllLogTest(unittest.TestCase):
      def testfindAllLog(self):
          url = "http://www.jasonisoft.cn:8080/HKR/LogServlet?method=findAllLog"
          data = {

          }
          #期望数据
          expect = 200
          #调用测试接口
          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"

          #取出状态码和响应数据
          code = response.status_code
          txt = response.text

          #断言
          print(txt)
          self.assertEqual(expect,code)