.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=============================
collective.image_max_fullsize
=============================

Reduces the size of huge images down to a defined maximum, to keep the original image size decent.

Features
--------

- provides an event handle to reduce the original image size down to a maximum.



Installation
------------

Install collective.image_max_fullsize by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.image_max_fullsize


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.image_max_fullsize/issues
- Source Code: https://github.com/collective/collective.image_max_fullsize


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the GPLv2.
