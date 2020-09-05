#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Wed Jul  8 16:22:26 2020
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):

    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((500, 200))
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_FIXEDWIDTH | wx.NB_TOP)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.checkbox_artist = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.checkbox_bpm = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.checkbox_date = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.checkbox_duration = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.checkbox_mapper = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.checkbox_title = wx.CheckBox(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.button_export = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "export\n")
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.text_ctrl_1 = wx.SearchCtrl(self.notebook_1_pane_2, wx.ID_ANY, "")
        self.check_list_box_ = wx.CheckListBox(self.notebook_1_pane_2, wx.ID_ANY, choices=["choice 1"],
                                               style=wx.LB_ALWAYS_SB | wx.LB_MULTIPLE)
        self.button_right = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, ">>\n")
        self.button_left = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, "<<\n")
        self.check_list_box_1 = wx.CheckListBox(self.notebook_1_pane_2, wx.ID_ANY, choices=["choice 1", ""],
                                                style=wx.LB_ALWAYS_SB | wx.LB_MULTIPLE)
        self.frame_statusbar = self.CreateStatusBar(1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Synth Playlist Wizard")
        self.text_ctrl_1.ShowCancelButton(True)
        self.check_list_box_1.SetSelection(1)
        self.frame_statusbar.SetStatusWidths([-1])

        # statusbar fields
        frame_statusbar_fields = ["frame_statusbar"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        # Templates
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.FlexGridSizer(2, 3, 0, 0)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 7, 4, 5)
        label_artist = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Artist")
        grid_sizer_1.Add(label_artist, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_artist, 0, 0, 0)
        label_bpm = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Bpm\n")
        grid_sizer_1.Add(label_bpm, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_bpm, 0, 0, 0)
        label_date = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Date\n")
        grid_sizer_1.Add(label_date, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_date, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_duration = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Duration\n\n")
        grid_sizer_1.Add(label_duration, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_duration, 0, 0, 0)
        label_mapper = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Mapper")
        grid_sizer_1.Add(label_mapper, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_mapper, 0, 0, 0)
        label_title = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Title")
        grid_sizer_1.Add(label_title, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_title, 0, 0, 0)
        grid_sizer_1.Add(self.button_export, 0, 0, 0)
        self.notebook_1_pane_1.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableCol(0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(2)
        grid_sizer_1.AddGrowableCol(3)
        grid_sizer_1.AddGrowableCol(4)
        grid_sizer_1.AddGrowableCol(5)
        grid_sizer_1.AddGrowableCol(6)

        # Edit Playlists
        sizer_14.Add(self.text_ctrl_1, 0, 0, 0)
        sizer_14.Add((0, 0), 0, 0, 0)
        sizer_14.Add((150, 20), 0, wx.EXPAND, 0)
        sizer_14.Add(self.check_list_box_, 2, wx.EXPAND, 0)
        sizer_15.Add((20, 150), 0, wx.EXPAND, 0)
        sizer_15.Add(self.button_right, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_15.Add(self.button_left, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_14.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_14.Add(self.check_list_box_1, 0, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_14)
        sizer_14.AddGrowableRow(1)
        sizer_14.AddGrowableCol(0)
        sizer_14.AddGrowableCol(1)
        sizer_14.AddGrowableCol(2)

        self.notebook_1.AddPage(self.notebook_1_pane_1, "Templates")
        # self.notebook_1.AddPage(self.notebook_1_pane_2, "Edit Playlist")
        sizer_8.Add(self.notebook_1, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_8)
        self.Layout()
        # end wxGlade

# end of class MyFrame


class GUI(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


if __name__ == "__main__":
    gettext.install("app")  # replace with the appropriate catalog name

    app = GUI(0)
    app.MainLoop()