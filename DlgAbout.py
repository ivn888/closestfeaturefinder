
from ui.DlgAbout_ui import Ui_DlgAbout

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import resources

class DlgAbout(QDialog, Ui_DlgAbout):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.logo.setPixmap( QPixmap( ":/icons/faunalia_logo.png" ) )

		text = self.txt.toHtml()
		text = text.replace( "$PLUGIN_NAME$", self.title.text() )
		self.txt.setHtml(text)
