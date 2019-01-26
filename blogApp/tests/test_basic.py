from blogApp.tests.base import BasicTestCase
import unittest

class UserTests(BasicTestCase):
  ###############
  #### tests ####
  ###############
 
  def test_main_page(self):
      response = self.app.get('/home', follow_redirects=True)
      self.assertEqual(response.status_code, 200)

  ########################
  #### helper methods ####
  ########################
    
if __name__ == "__main__":
    unittest.main()