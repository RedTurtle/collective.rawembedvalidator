# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.rawembedvalidator


class CollectiveRawembedvalidatorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.rawembedvalidator)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.rawembedvalidator:default')


COLLECTIVE_RAWEMBEDVALIDATOR_FIXTURE = CollectiveRawembedvalidatorLayer()


COLLECTIVE_RAWEMBEDVALIDATOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_RAWEMBEDVALIDATOR_FIXTURE,),
    name='CollectiveRawembedvalidatorLayer:IntegrationTesting'
)


COLLECTIVE_RAWEMBEDVALIDATOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_RAWEMBEDVALIDATOR_FIXTURE,),
    name='CollectiveRawembedvalidatorLayer:FunctionalTesting'
)


COLLECTIVE_RAWEMBEDVALIDATOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_RAWEMBEDVALIDATOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveRawembedvalidatorLayer:AcceptanceTesting'
)
