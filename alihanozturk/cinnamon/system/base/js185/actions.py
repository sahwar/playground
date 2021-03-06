# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "js-1.8.5/js/src"

def setup():
   shelltools.export("CPPFLAGS", get.CXXFLAGS())
   autotools.configure("--with-system-nspr \
                        --enable-threadsafe")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    pisitools.rename("/usr/bin/js-config", "js185-config")
