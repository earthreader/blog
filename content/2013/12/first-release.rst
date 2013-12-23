Released Earth Reader for Web 0.1.0, and libearth 0.1.0
=======================================================

:date: 2013-12-22T19:07:30Z
:slug: first-release
:author: Hong Minhee
:email: minhee@dahlia.kr

Hi,

We are very pleased to announce our first two releases:
`Earth Reader for Web`_ 0.1.0, and libearth_ 0.1.0!
It provides the most of basic features including subscribing new feeds,
unsubscribing feeds, categorizing subscriptions, crawling subscriptions,
marking entries as read/unread/starred/unstarred, and synchronization__
between multiple devices through Dropbox_/`Google Drive`_/rsync_.

Earth Reader for Web is our first app.  You can install it on your server
to use it on web browsers including mobile browsers.
See the release page on GitHub and PyPI:

GitHub
   https://github.com/earthreader/web/releases/tag/0.1.0

PyPI
   https://pypi.python.org/pypi/EarthReader-Web/0.1.0

Use ``pip`` to install it:

.. code-block:: console

  $ pip install EarthReader-Web==0.1.0

See more on how to install and use it:

https://github.com/earthreader/web#install

Libearth is the shared common library for various Earth Reader apps.
It supports Python 2.6, 2.7, 3.2, 3.3, PyPy 2.0+, and IronPython 2.7.4+.
Earth Reader for Web also depends on it.
See the release page on GitHub and PyPI:

GitHub
   https://github.com/earthreader/libearth/releases/tag/0.1.0

PyPI
   https://pypi.python.org/pypi/libearth/0.1.0

You can install it using ``pip`` as like Earth Reader for Web:

.. code-block:: console

   $ pip install libearth==0.1.0

See the docs for libearth:

http://libearth.earthreader.org/en/0.1.0/

The Earth Reader team and other contributors put many efforts into this.
Thanks for `Choi Bochul`__, `Eunchong Yu`__, `Jihyeok Seo`__, and
`Jinwon Kang`__.  This is `Hong Minhee`__.

Regards,
Minhee and the Earth Reader team

.. _Earth Reader for Web: https://github.com/earthreader/web
.. _libearth: http://libearth.earthreader.org/
__ |filename|sync.rst
.. _Dropbox: https://www.dropbox.com/
.. _Google Drive: https://drive.google.com/
.. _rsync: http://rsync.samba.org/
__ https://github.com/viobo
__ https://github.com/Kroisse
__ https://github.com/limeburst
__ https://github.com/Kjwon15
__ https://github.com/dahlia
