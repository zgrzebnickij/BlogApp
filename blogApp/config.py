import os

class Config():
  #move to enviroment variables
  SECRET_KEY = '408573b3bb22fb76aa0c5ae611ffe5ab'
  SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
  #SQLALCHEMY_NATIVE_UNICODE = False

  MAIL_SERVER = "smtp.gmail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("EMAIL_USER")
  MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

class ConfigTests():
  TESTING = True
  WTF_CSRF_ENABLED = False
  DEBUG = False
  SECRET_KEY = '408573b3bb22fb76aa0c5ae611ffe5ab'
  SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

  #SQLALCHEMY_NATIVE_UNICODE = False

  # MAIL_SERVER = "smtp.gmail.com"
  # MAIL_PORT = 587
  # MAIL_USE_TLS = True
  # MAIL_USERNAME = os.environ.get("EMAIL_USER")
  # MAIL_PASSWORD = os.environ.get("EMAIL_PASS")