#!/usr/bin/env python3

import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk, Gdk as gdk, GLib as glib
from gi.repository.GdkPixbuf import Pixbuf, Colorspace


# def set_mask(win: gtk.Window) -> None:
#     size = win.get_size()
#     print(size)
#     # bitmap = Pixbuf.new(win, size[0], size[1], 1)
#     # bitmap = Pixbuf.new(has_alpha=True, width=size[0], height=size[0], bits_per_sample=1)
#     bitmap = Pixbuf.new(Colorspace.RGB, True, 8, size[0], size[1])
#     # bitmap.rectangle((0, 0) + size)
#     bitmap.fill(0.0, 0.0, 0.0, 0.5)

#     # cr = bitmap.cairo_create()
#     # cr.set_operator(cairo.OPERATOR_SOURCE)
#     # cr.set_source_rgba(0.0, 0.0, 0.0, 0.5)
#     # cr.rectangle((0, 0) + size)
#     # cr.fill()

#     win.input_shape_combine_mask(bitmap, 0, 0)
#     print('ready')


def main() -> None:
    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    win.show_all()
    glib.timeout_add(1000, set_mask, win)
    gtk.main()


if __name__ == '__main__':
    main()
