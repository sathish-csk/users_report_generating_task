import unittest
import users_report as report
import requests

class Testing(unittest.TestCase):
   def test_user_reports(self):
       all_user = report.get_all_user_details()
       self.assertEqual(all_user.status_code, 200)

       all_user_details = all_user.json()

       for user in all_user_details:
           if user["id"] % 20 == 0:
               specific_user= report.get_specific_user_details(user["login"])
               self.assertEqual(specific_user.status_code, 200)
               single_user_details = specific_user.json()

               followers=report.get_followers_details(single_user_details["login"])
               self.assertEqual(followers.status_code, 200)

if __name__ == '__main__':
    unittest.main()
