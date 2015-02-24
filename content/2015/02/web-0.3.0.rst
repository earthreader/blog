Released Earth Reader for Web 0.3.0
===================================

:date: 2015-02-24 7:57:36Z
:slug: web-0.3.0
:author: Kang Jinwon
:email: kjwonmail@gmail.com

We released Earth Reader for Web 0.3.0 with 0.1.2, and 0.2.2. It has these changes.


0.3.0
-----

- Run crawler thread by default.
- Error code ``circular-refernce``, which is a typo, was renamed to
  ``circular-reference``.
- Fixed auto scroll when entry has images.
- Fixed a bug that raises ``BuildError``.
- Became to need libearth 0.3.1 or later.
- Save theme setting.
- "Go to top" button on bottom.
- And a lot of changes (`Version 0.2.2`_).


0.2.2
-----

- Fixed a bug that enters a infinite loop when initilize
  :class:`~earthreader.web.CategoryEntryGenerator`
- Fix open link.
- And a lot of changes (`Version 0.1.2`_).


0.1.2
-----

- Entry list is cached by browser using :mailheader:`Last-Modified` and
  :mailheader:`If-Modified-Since` headers.
- Fix malformed session id on multi process.
- Fix error log when crawling.
- Force MIME type "test/html" when not given.
- Fix shortcut key.


GitHub
   https://github.com/earthreader/web/releases/tag/0.3.0

PyPI
   https://pypi.python.org/pypi/EarthReader-Web/0.3.0

You can install it using ``pip``:

.. code-block:: console

  $ pip install EarthReader-Web==0.3.0

| Thanks,
| Jinwon and the Earth Reader team
