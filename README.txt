Turbogears2 Spox Tutorial shows you how to use Sprox: a quick way to generate forms for your model objects.

From the Sprox Website:
  Sprox is a widget generation library that has a slightly different take on
  the problem of creating custom web content directly from database schemas.
  Sprox provides an easy way to create forms for web content which are:
  automatically generated, easy to customize, and validated. Sprox also has
  powerful tools to help you display your content the way you want to with
  table and record viewers. Sprox provides a way to fill your widgets, whether
  they are forms or other content with customizable data.

In short: Sprox will generate your forms for you, easily giving you a reusable object to use throughout your application. It's also customizable so you can keep on using it when your needs grow.

References:
  * http://turbogears.org/2.1/docs/main/movie_tutorial.html
      How to customize your form's action, how to do basic customization of the form
  * http://sprox.org/tutorials/form.html
      From basics, to customization, to using the builtin Dojo support, custom fields, and validators.
  * http://formencode.org/modules/validators.html#module-formencode.validators
      validators for FormEncode (what Sprox uses on the back end...)

This sample application has the following domain: it's a newsletter sign up application.


Standard information follows:
===========================================================

Installation and Setup
======================

Install ``turbogears2-sprox-tutorial`` using the setup.py script::

    $ cd turbogears2-sprox-tutorial
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Then you are ready to go.
