# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from nikola.plugin_categories import RestExtension
from nikola.utils import LOGGER, makedirs


class Plugin(RestExtension):

    name = "rest_podcast"

    def set_site(self, site):
        self.site = site
        directives.register_directive('podcast', Podcast)
        return super(Plugin, self).set_site(site)


class Podcast(Directive):
    """ Restructured text extension for inserting podcasts

        Usage:

            .. Podcast:: filename.mp3

   """

    has_content = True
    def run(self):
        node_list = []
        mp3 = str(self.content[0])
        txt='<object type="application/x-shockwave-flash" data="/podcast/dewplayer.swf" width="200" height="20" id="dewplayer" name="dewplayer"> <param name="wmode" value="transparent" /><param name="movie" value="/podcast/dewplayer.swf" /> <param name="flashvars" value="mp3=%s" /> </object>'% mp3
        node_list.append(nodes.raw('', txt, format='html'))
        return node_list

