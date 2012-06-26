import os.path

import pkg_resources

import tg
from pylons import c

from allura.app import Application, DefaultAdminController, SitemapEntry
from allura.lib.security import has_access
from allura.lib import helpers as h

from .djall_base import DjangoApp

import django.conf

django.conf.DATABASE_ROUTERS = [ 'djall.db.DatabaseRouter' ]

class RietveldApp(DjangoApp):
    __version__ = 0.1
    installable = True
    tool_label ='Code Review'
    default_mount_point = 'codereview'
    default_mount_label = 'Code Review'
    ordinal=200
    icons={
        24:'images/admin_24.png',
        32:'images/admin_32.png',
        48:'images/admin_48.png'
    }

    def is_visible_to(self, user):
        '''Whether the user can view the app.'''
        return has_access(c.project, 'create')(user=user)

    def main_menu(self):
        '''Apps should provide their entries to be added to the main nav
        :return: a list of :class:`SitemapEntries <allura.app.SitemapEntry>`
        '''
        return [ SitemapEntry(
                self.config.options.mount_label.title(),
                '.')]

    @property
    def sitemap(self):
        menu_id = self.config.options.mount_label.title()
        with h.push_config(c, app=self):
            return [
                SitemapEntry(menu_id, '.')[self.sidebar_menu()] ]

    def sidebar_menu(self):
        return [SitemapEntry('Sidebar', '.')]

    def admin_menu(self):
        return []

    def install(self, project):
        pass

    def uninstall(self, project): # pragma no cover
        pass

        