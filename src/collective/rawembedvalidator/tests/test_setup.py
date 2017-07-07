# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.rawembedvalidator.testing import COLLECTIVE_RAWEMBEDVALIDATOR_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.rawembedvalidator is properly installed."""

    layer = COLLECTIVE_RAWEMBEDVALIDATOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.rawembedvalidator is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.rawembedvalidator'))

    def test_browserlayer(self):
        """Test that ICollectiveRawembedvalidatorLayer is registered."""
        from collective.rawembedvalidator.interfaces import (
            ICollectiveRawembedvalidatorLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveRawembedvalidatorLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RAWEMBEDVALIDATOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.rawembedvalidator'])

    def test_product_uninstalled(self):
        """Test if collective.rawembedvalidator is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.rawembedvalidator'))
