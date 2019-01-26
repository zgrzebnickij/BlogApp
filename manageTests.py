import unittest
import os
import coverage

from flask_script import Manager
from blogApp import create_app, db
from blogApp.config import ConfigTests

app = create_app(ConfigTests)
manager = Manager(app)

@manager.command
def run():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('blogApp/tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(
        branch=True,
        include='blogApp/*'
    )
    cov.start()
    tests = unittest.TestLoader().discover('blogApp/tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()

if __name__ == '__main__':
    manager.run()