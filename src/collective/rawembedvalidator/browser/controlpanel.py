# -*- coding: utf-8 -*-
"""Control panel."""
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout

from collective.rawembedvalidator import _
from collective.rawembedvalidator.interfaces import IRawEmbedValidatorSchema


# TODO: personalizzare il controlpanel per aggiungere una textarea in cui provare
# i pattern

class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = IRawEmbedValidatorSchema
    schema_prefix = 'collective.rawembedvalidator'
    label = u"Embed Validator Settings"



SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
