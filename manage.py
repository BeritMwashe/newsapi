from flask_script import Manager,Server
from app import create_app


app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('app/tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# def test(coverage=False, test_name=None):
#     """Run the unit tests."""
#     import unittest
#     if test_name is None:
#         tests = unittest.TestLoader().discover('..tests',pattern='test*.py')
#     else:
#         tests = unittest.TestLoader().loadTestsFromName('tests.' + test_name)
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__=='__main__':
    manager.run()
    
# from app import create_app
# from flask_script import Manager,Server
# # Creating app instance
# app = create_app('development')
# manager = Manager(app)
# manager.add_command('server',Server)
# if __name__ == '__main__':
#     manager.run()
