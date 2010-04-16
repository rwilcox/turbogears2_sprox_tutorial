# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from turbogears2_sprox_tutorial.lib.base import BaseController
from turbogears2_sprox_tutorial.model import DBSession, metadata
from turbogears2_sprox_tutorial.controllers.error import ErrorController

from turbogears2_sprox_tutorial import model

__all__ = ['RootController']

from catwalk.tg2 import Catwalk

class UnSecuredCatwalk(Catwalk):
    allow_only = None

class RootController(BaseController):
    """
    The root controller for the turbogears2-sprox-tutorial application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()
    catwalk = UnSecuredCatwalk(model, DBSession)

    @expose('turbogears2_sprox_tutorial.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('turbogears2_sprox_tutorial.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('turbogears2_sprox_tutorial.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment=request.environ)

    @expose('turbogears2_sprox_tutorial.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)


