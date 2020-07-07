# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.image_max_fullsize


class CollectiveImageMaxFullsizeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.image_max_fullsize)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.image_max_fullsize:default')


COLLECTIVE_IMAGE_MAX_FULLSIZE_FIXTURE = CollectiveImageMaxFullsizeLayer()


COLLECTIVE_IMAGE_MAX_FULLSIZE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_IMAGE_MAX_FULLSIZE_FIXTURE,),
    name='CollectiveImageMaxFullsizeLayer:IntegrationTesting',
)


COLLECTIVE_IMAGE_MAX_FULLSIZE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_IMAGE_MAX_FULLSIZE_FIXTURE,),
    name='CollectiveImageMaxFullsizeLayer:FunctionalTesting',
)


COLLECTIVE_IMAGE_MAX_FULLSIZE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_IMAGE_MAX_FULLSIZE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveImageMaxFullsizeLayer:AcceptanceTesting',
)
