# -*- coding: utf-8 -*-

import os
import six
from kodi_six import xbmc, xbmcaddon, xbmcgui, xbmcvfs

__addonID__ = 'script.module.metahandler'
__addon__ = xbmcaddon.Addon(__addonID__)

METAFOLDER = __addon__.getSetting('meta_folder_location')
METAFOLDER = xbmc.translatePath(METAFOLDER) if six.PY2 else xbmcvfs.translatePath(METAFOLDER)
if not METAFOLDER:
    if six.PY2:
        METAFOLDER = xbmc.translatePath("special://profile/addon_data/script.module.metahandler/")
    else:
        METAFOLDER = xbmcvfs.translatePath("special://profile/addon_data/script.module.metahandler/")
METAFOLDER = os.path.join(METAFOLDER, 'meta_cache')
DBLOCATION = os.path.join(METAFOLDER, 'video_cache.db')


def remove_DataBase():
    xbmc.log("metahandler - deleting database...")
    try:
        if xbmcvfs.exists(DBLOCATION):
            xbmcvfs.delete(DBLOCATION)
    except:
        if os.path.exists(DBLOCATION):
            os.remove(DBLOCATION)
    xbmcgui.Dialog().ok("Metahandler", "Database deleted")
    xbmc.log("Metahandler - Clearing database cache. Done!")


if (__name__ == "__main__"):
    remove_DataBase()
