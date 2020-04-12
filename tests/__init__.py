import unittest


def suite():
    suite = unittest.TestSuite()
    add_test_case(suite)
    return suite

def add_test_case(suite: unittest.TestSuite):
    from tests.services.checker import TestCheckers
    suite.addTest(TestCheckers('test_jwt_checker'))