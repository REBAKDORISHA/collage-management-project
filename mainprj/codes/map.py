"""import tkinter as tk
import tkintermapview

root=tk.Tk()
root.geometry("900x700")
root.title("Map")
root.iconbitmap("https://www.google.co.in/maps/@13.1432585,80.1567951,11z?entry=ttu&g_ep=EgoyMDI1MDQwMi4xIKXMDSoASAFQAw%3D%3D")

my_lable=LabelFrame(root)
my_lable.pack(pady=20)
map_wideget=tkintermapview.TkinterMapView(my_lable, width=800,height=600,corner_radius=0)
map_wideget.pack()

root.mainloop()"""




import tkinter as tk
from tkhtmlview import HTMLLabel
import folium
# Removed unused import

# Create a basic map using folium
map_object = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India
folium.Marker([28.6139, 77.2090], popup="New Delhi").add_to(map_object)

# Save the map to an HTML file
map_file = "mymap.html"
map_object.save(map_file)

# Create the main GUI window
root = tk.Tk()
root.title("Map Viewer in Tkinter")
root.geometry("800x600")

# Read the map HTML content
with open(map_file, 'r', encoding='utf-8') as f:
    map_html = f.read()

# Show the map inside the Tkinter window
html_label = HTMLLabel(root, html=map_html)
html_label.pack(fill="both", expand=True)

root.mainloop()
