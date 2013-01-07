# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging,os
from pyh import *

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
        self._create_context_menu()
        self.AboutDialog = AboutSlashmPlayerDialog
        self.PreferencesDialog = PreferencesSlashmPlayerDialog
        self.maximize()
        self.browsewindow = self.builder.get_object("browsewindow")        
        self.webview=WebKit.WebView()        
        self.browsewindow.add(self.webview)
        settings = self.webview.get_settings()
        settings.set_property('enable-default-context-menu', False)
        self.webview.show()
        self.webview.set_settings(settings)
        self.folderselect = self.builder.get_object("folderselect")
        self.folderbutton = self.builder.get_object("folderbutton")
        self.librarybutton = self.builder.get_object("librarybutton")
        # Code for other initialization actions should be added here.
        self.connect('button_press_event', self._on_button_press_event)
    
    def _create_context_menu(self):
        """Create the context menu."""
        self.menu = Gtk.Menu()
        delete_menu = Gtk.MenuItem("Delete Task")
        self.menu.append(delete_menu)
    
    def _on_button_press_event(self, widget, event):
        """Deal with the button press event."""
        if event.button == 3:
            self.menu.popup(None, None, None, None, event.button, event.time)
            self.menu.show_all()

        
        


    def on_folderselect_clicked(self,widget):
        folder_selector = Gtk.FileChooserDialog("select a folder",self,Gtk.FileChooserAction.SELECT_FOLDER,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,"Select", Gtk.ResponseType.OK))        
        folder_selector.show()
        response=folder_selector.run()
        if response == Gtk.ResponseType.OK:

            config_file = open('slashplayer.conf', 'a')
            config_html = open('config.html','a+')
            config_file.write(folder_selector.get_filename()+'\n')

            
            config_html.write('<a href = "'+ folder_selector.get_filename()+'">'+os.path.basename(folder_selector.get_filename())+'</a> <br>')
            config_file.close()
        folder_selector.destroy()


    def on_folderbutton_clicked(self,widget):
        f = open('slashplayer.conf', 'r')        
        doc = PyH('')
        for line in f:
            doc << a(os.path.basename(line),href=line)
            doc << br()
        #doc.a.href=("http://www.google.com")
        doc.render()
        #doc.               
        self.webview.load_html_string(str(doc.render()),'#')


    

        
        
    def on_librarybutton_clicked(self,widget):
        #list_of_files_in_cwd = os.listdir(".")
        #open config file and make an array of all the items in it named locations
        config_file = open('slashplayer.conf', 'r')
        locations = config_file.readlines()
        for index, location in enumerate(locations):
            location = location[:-1]
            os.listdir(location) 
            
        
        
        
        
        

        
        
