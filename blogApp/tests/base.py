from blogApp import db, mail, create_app
from blogApp.config import ConfigTests
from flask import url_for
import unittest
import flask_testing
import os
from manageTests import app


#app.app_context().push()

class BasicTestCase(unittest.TestCase):
  """
  Basic unittest setup
  """
  #execute prior to each test
  def setUp(self):
    self.app = app.test_client()
    db.create_all()

    # Disable sending emails during unit testing
    mail.init_app(app)
    self.assertEqual(app.debug, False)

  # executed after each test
  def tearDown(self):
    db.drop_all()
    pass


if __name__ == "__main__":
  unittest.main()