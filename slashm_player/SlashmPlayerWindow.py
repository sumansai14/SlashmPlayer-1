# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging,os
logger = logging.getLogger('slashm_player')

from slashm_player_lib import Window
from slashm_player.AboutSlashmPlayerDialog import AboutSlashmPlayerDialog
from slashm_player.PreferencesSlashmPlayerDialog import PreferencesSlashmPlayerDialog

# See slashm_player_lib.Window.py for more details about how this class works
class SlashmPlayerWindow(Window):
    __gtype_name__ = "SlashmPlayerWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002(
        """Set up the main window"""
        super(SlashmPlayerWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutSlashmPlayerDialog
        self.PreferencesDialog = PreferencesSlashmPlayerDialog
        self.maximize()
        self.browsewindow = self.builder.get_object("browsewindow")        
        self.webview=WebKit.WebView()        
        self.browsewindow.add(self.webview)
        self.webview.show()
        #self.webview.open("file:///home/sai/Desktop/test.html")
        self.folderselect = self.builder.get_object("folderselect")
        self.folderbutton = self.builder.get_object("folderbutton")
        # Code for other initialization actions should be added here.
    def on_folderselect_clicked(self,widget):
        test = Gtk.FileChooserDialog("select a folder",self,Gtk.FileChooserAction.SELECT_FOLDER,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,"Select", Gtk.ResponseType.OK))        
        test.show()
        response=test.run()
        if response == Gtk.ResponseType.OK:
            f = open('slashplayer.conf', 'a')
            f.write(test.get_filename()+'\n')
            f.close()
        test.destroy()
    def on_folderbutton_clicked(self,widget):
        f = open('slashplayer.conf', 'r')
        k = open('config.html','a+')
        for line in f:
            k.write('<a href="' +line+'">'+os.path.basename(line)+ '</a><br>')
        self.webview.open('file:///home/sai/slashm-player/config.html')
        
        
