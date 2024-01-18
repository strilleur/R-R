from PIL import Image, ImageTk
import tkinter
import os
from tkintermapview import TkinterMapView
import tkintermapview

class window_mapview():
 
    def __init__(self): 
        # create tkinter window
        root_tk = tkinter.Tk()
        root_tk.geometry(f"{1920}x{1080}")
        root_tk.title("map_view_example.py")

        # create map widget
        map_widget = tkintermapview.TkinterMapView(root_tk, width=1920, height=1080, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        map_widget.set_position(48.72315748863436, -3.9510462382878546)  # Paris, France
        map_widget.set_zoom(10)
        marker_2 = map_widget.set_marker(48.72315748863436, -3.9510462382878546, text="48.72315748863436, -3.9510462382878546 \n Roscoff")
        marker_3 = map_widget.set_marker(50.800767318062235, -1.0958410684472506, text="50.800767318062235, -1.0958410684472506")
        path_1 = map_widget.set_path([(48.72315748863436, -3.9510462382878546),(49.86529375795098, -3.027101134290339), (50.800767318062235, -1.0958410684472506)])

        

        root_tk.mainloop()

window_mapview=window_mapview()

# methods
"""
        path_1.set_position_list(new_position_list)
        path_1.add_position(position)
        path_1.remove_position(position)
        path_1.delete()
        """