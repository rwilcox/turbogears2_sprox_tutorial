# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from turbogears2_sprox_tutorial.lib.base import BaseController
from turbogears2_sprox_tutorial.model import DBSession, metadata
from turbogears2_sprox_tutorial.controllers.error import ErrorController

from turbogears2_sprox_tutorial import model

from formencode import Schema
from formencode.validators import FieldsMatch, Email, NotEmpty
from tw.forms import TextField
from sprox.formbase import AddRecordForm

from turbogears2_sprox_tutorial.model.newsletter_subscriber import NewsletterSubscriber

__all__ = ['RootController']

from catwalk.tg2 import Catwalk

newsletter_validator = Schema(chained_validators = (FieldsMatch("email_address", "verify_email_address", messages={"invalidNoMatch": "Email addresses do not match"}), ))
# validator to make sure fields match. From the example at <http://sprox.org/index.html>

class UnSecuredCatwalk(Catwalk):
    allow_only = None

class NewsletterAddForm(AddRecordForm):
    """A form that is an Add-A-Record form. Sprox has classes for all the CRUD operations"""
    __model__ = NewsletterSubscriber                            # required
    __omit_fields__ = ['id']                                    # skip display for the ID field (would be disabled anyway)
    #__require_fields = ["full_name", "email_address"]           # auto validation of these fields
    # auto validation doesn't work when we override __base_validator__
    
    email_address = Email()
    # formencode has an Email validator. We override the default validation behavor of the control to provide special
    # validation
    
    full_name = NotEmpty()                                      # explicitly set this validation up because __require_fields__ doesn't work in our case
    verify_email_address = TextField("verify_email_address")    #add a non-model field, which our validator will compare
    __base_validator__ = newsletter_validator                   # hook up our special validator to make sure two fields match

new_newsletter_sub_form = NewsletterAddForm(DBSession)

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
    
    @expose("turbogears2_sprox_tutorial.templates.newsletter_form")
    def newsletter(self, **kw):
        """Handle the newsletter sign up form page"""
        tmpl_context.widget = new_newsletter_sub_form
        # tmpl_context is a special variable in Turbogears. I'm a little
        # confused as to what it does, and why we can't just pass the Sprox form
        # However, the template on the other side expects to get the form through the tmpl_context
        return dict(page="newsletter signup", value=kw)
    
    # This is the reason why we needed to instantiate the Sprox form (instead of instantiating in the action
    # like you might expect): we need to use that same form instance to validate
    # the user's input
    @validate(new_newsletter_sub_form, error_handler=newsletter)
    @expose()
    def post_newsletter(self, full_name, email_address, **kw):
        subber = NewsletterSubscriber(full_name=full_name, email_address=email_address)
        DBSession.add(subber)
        flash("Thank you for subscribing to our newsletter")
        redirect( url("/index") )



