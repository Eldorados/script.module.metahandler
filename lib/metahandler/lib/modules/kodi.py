"""
    Metahandler Addon for Kodi
    Copyright (C) 2021 Eldorado

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from kodi_six import xbmcaddon, xbmcgui, xbmc, xbmcvfs
import six
from six.moves import urllib_parse
import sys
import os
from . import constants

addon = xbmcaddon.Addon(constants.addon_id)
get_setting = addon.getSetting
show_settings = addon.openSettings
sleep = xbmc.sleep


def get_path():
    return addon.getAddonInfo('path')


def get_profile():
    return addon.getAddonInfo('profile')


def translate_path(path):
    return xbmcvfs.translatePath(path) if six.PY3 else xbmc.translatePath(path)


def set_setting(id, value):
    if not isinstance(value, str):
        value = str(value)
    addon.setSetting(id, value)


def get_version():
    return addon.getAddonInfo('version')


def get_id():
    return addon.getAddonInfo('id')


def get_name():
    return addon.getAddonInfo('name')


def open_settings():
    return addon.openSettings()


def get_keyboard(heading, default=''):
    keyboard = xbmc.Keyboard()
    keyboard.setHeading(heading)
    if default:
        keyboard.setDefault(default)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return keyboard.getText()
    else:
        return None


def get_plugin_url(queries):
    try:
        query = urllib_parse.urlencode(queries)
    except UnicodeEncodeError:
        for k in queries:
            if isinstance(queries[k], str):
                queries[k] = queries[k].encode('utf-8')
        query = urllib_parse.urlencode(queries)

    return sys.argv[0] + '?' + query


def parse_query(query):
    q = {'mode': 'main'}
    if query.startswith('?'):
        query = query[1:]
    queries = urllib_parse.parse_qs(query)
    for key in queries:
        if len(queries[key]) == 1:
            q[key] = queries[key][0]
        else:
            q[key] = queries[key]
    return q


def notify(header=None, msg='', duration=2000, sound=None):
    if header is None:
        header = get_name()
    if sound is None:
        sound = get_setting('mute_notifications') == 'false'
    icon_path = os.path.join(get_path(), 'icon.png')
    try:
        xbmcgui.Dialog().notification(header, msg, icon_path, duration, sound)
    except:
        builtin = "Notification(%s,%s, %s, %s)" % (header, msg, duration, icon_path)
        xbmc.executebuiltin(builtin)
