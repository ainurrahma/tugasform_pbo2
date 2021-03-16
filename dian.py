# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.m_panel3 = wx.Panel( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"helowx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		fgSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer3 )
		self.m_panel3.Layout()
		fgSizer3.Fit( self.m_panel3 )
		sbSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Ainurrahma Diananda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"192410101144", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( fgSizer4 )
		self.m_panel6.Layout()
		fgSizer4.Fit( self.m_panel6 )
		sbSizer1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( sbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


