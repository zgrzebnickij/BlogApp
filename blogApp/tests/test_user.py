from blogApp.tests.base import BasicTestCase
import unittest
from blogApp.models import User
from blogApp import db, bcrypt 

class UserTests(BasicTestCase):
  ########################
  #### helper methods ####
  ########################

  def dbInsertUser(self, username='Flasker', email='patkennedy79@gmail.com', password='FlaskIsAwesome'):
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

  def register(self, username , email, password, confirm_password):
    return self.app.post(
        '/register',
        data=dict(username=username, email=email, password=password, confirm_password=confirm_password),
        follow_redirects=True
    )
  
  def login(self, email, password, remember=False):
    return self.app.post(
        '/login',
        data=dict(email=email, password=password),
        follow_redirects=True
    )
  
  def logout(self):
    return self.app.get(
        '/logout',
        follow_redirects=True
    )

#   ########################
#   #### register tests ####
#   ########################

  def test_valid_user_registration(self):
    response = self.register('Flasker', 'patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b"Your account has been created! You are now able to log in.", response.data)

  def test_invalid_user_registration_different_passwords(self):
    response = self.register('Flasker', 'patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsNotAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Field must be equal to password.', response.data)

  def test_invalid_user_registration_duplicate_email(self):
    self.dbInsertUser()
    response = self.register('Flasker1', 'patkennedy79@gmail.com', 'FlaskIsReallyAwesome', 'FlaskIsReallyAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'That email is taken. Please choose another one.', response.data)

  def test_invalid_user_registration_duplicate_username(self):
    self.dbInsertUser()
    response = self.register('Flasker', 'patkennedy70@gmail.com', 'FlaskIsReallyAwesome', 'FlaskIsReallyAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'That username is taken. Please choose another one.', response.data)

  #########################
  ##### login tests #######
  #########################
    
  def test_valid_user_logging(self):
    self.dbInsertUser()
    response = self.login('patkennedy79@gmail.com', 'FlaskIsAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome Flasker', response.data)

  def test_invalid_user_logging_diferent_email(self):
    self.dbInsertUser()
    response = self.login('patkennedy70@gmail.com', 'FlaskIsAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Login unsuccessful!', response.data)

  def test_invalid_user_logging_diferent_password(self):
    self.dbInsertUser()
    response = self.login('patkennedy79@gmail.com', 'FlaskIsawesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Login unsuccessful!', response.data)

  #########################
  ##### logout tests #######
  #########################

  def test_valid_user_logout(self):
    self.dbInsertUser()
    response = self.login('patkennedy79@gmail.com', 'FlaskIsAwesome')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome Flasker', response.data)
    response = self.logout()
    self.assertIn(b'See you soon Flasker.', response.data)
    

if __name__ == "__main__":
    unittest.main()