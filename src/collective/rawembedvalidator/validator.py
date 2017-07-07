
from plone import api
import re
from z3c.form import validator
from zope.interface import Invalid

from collective.rawembedvalidator import _
from collective.rawembedvalidator import logger

# TODO: questi andranno nel registry e gestiti
# da un controlpanel specifico
# TODO: definire delle macro per URL, WORD, NUMBER, ...
'''
PATTERNS = [
    """
<a class="twitter-timeline" href="https://twitter.com/[^"]+">[^<]+</a>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
""",

    """
ab
abd
cd ef

""",

]
'''

class RawEmbedValidator(validator.SimpleFieldValidator):
    """ z3c.form validator class for embed regexp """

    def validate(self, value):
        """ ... """
        if not value:
            return

        try:
            settings = api.portal.get_registry_record(
                name='collective.rawembedvalidator.patterns')
        except api.exc.InvalidParameterError:
            settings = None

        if not settings:
            logger.warning(
                'missing collective.rawembedvalidator.patterns registry key for %s',
                api.portal.get())
            return

        # TODO: verificare il browserlayer della vista? qui o nella dichiarazione
        # dell'adapter?
        value = re.sub('\s+', ' ', value).strip()

        for pattern in settings.values():
            # TODO: il pattern arriva qui gia' stripped o va strippato qui?
            pattern = re.sub('\s+', ' ', pattern).strip()
            if re.match(pattern, value):
                return

        # TODO: se si ha il ruolo di administrator sul contesto,
        # anzichè lanciare l'eccezione del validtore
        # emettere uno statusmessage warning

        raise Invalid(_(u"embed code not accepted"))


try:
    from plone.app.standardtiles.rawembed import IRawEmbedTile
    validator.WidgetValidatorDiscriminators(
        RawEmbedValidator, field=IRawEmbedTile['html_snippet'])
except ImportError:
    logger.warning('missing plone.app.standardtiles.rawembed')
