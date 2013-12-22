Synchronizing data without losing control
=========================================

:date: 2013-12-22T15:35:25Z
:slug: sync
:author: Hong Minhee
:email: minhee@dahlia.kr

`Our goal`_ is to achieve the following subgoals at the same time:

1. The whole data should be controlled by the owner.  It means data will be
   tangible and reachable on the file system.
2. It should be possible to synchronize data between multiple devices,
   without any conflict between simultaneous updates.

Earth Reader itself actually does not synchronize data.  Instead it simply
stores data into file system, and you should choose a synchronization method
e.g. Dropbox_, `Google Drive`_, or rsync_ if you're a computer expert.

Although there's no magic, we had to put effort under the hood in order to
make synchronization done smoothly.  Without any effort data becomes easily
corrupted during synchronization.  Because there could be a race condition
between two or more devices.

To resolve it Earth Reader separately stores data.  Each device has its
own isolated area, and never writes data to others' area, but can only read
from others'.  When each device reads data it merges all updates from others'
if there are any simultaneous changes.  We call it *read-time merge*.

All explained above are already implemented by libearth_, our shared common
library for various Earth Reader apps.  You can try out this right now by
installing Earth Reader for Web:

https://github.com/earthreader/web

| Thanks,
| Minhee and the Earth Reader team

.. _Our goal: |filename|../11/goal.rst
.. _Dropbox: https://www.dropbox.com/
.. _Google Drive: https://drive.google.com/
.. _rsync: http://rsync.samba.org/
.. _libearth: http://libearth.earthreader.org/
