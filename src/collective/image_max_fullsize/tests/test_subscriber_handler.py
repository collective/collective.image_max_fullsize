# -*- coding: utf-8 -*-
from collective.image_max_fullsize.testing import COLLECTIVE_IMAGE_MAX_FULLSIZE_FUNCTIONAL_TESTING
from collective.image_max_fullsize.testing import COLLECTIVE_IMAGE_MAX_FULLSIZE_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class SubscriberIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_IMAGE_MAX_FULLSIZE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])


class SubscriberFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_IMAGE_MAX_FULLSIZE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
