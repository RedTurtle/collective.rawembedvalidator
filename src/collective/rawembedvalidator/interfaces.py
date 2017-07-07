# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema


from collective.rawembedvalidator import _


class ICollectiveRawembedvalidatorLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRawEmbedValidatorSchema(Interface):

    patterns = schema.Dict(
        title=_(u'patterns'),
        description=_(u'TODO'),
        key_type=schema.TextLine(title=u'provider'),
        value_type=schema.Text(title=u'pattern'),
        # TODO: move defaults to registry.xml ?
        default={
            "twitter-timeline": """
<a class="twitter-timeline"( data-lang="[a-z]+")?( data-limit="[0-9]+")?( data-dnt="true")? href="https://twitter.com/[^"]+">[^<]+</a>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
""",
            "twitter-grid": """
<a class="twitter-grid"( data-lang="[a-z]+")?( data-limit="[0-9]+")?( data-dnt="true")? href="https://twitter.com/[^"]+">[^<]*</a>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
""",
        },
        missing_value={},
        required=False,
    )