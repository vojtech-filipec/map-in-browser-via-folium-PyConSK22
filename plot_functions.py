## functions used in the main notebook

from folium import Popup, IFrame

def create_color(row):
    if row.cnt_tags < 5:
        color = '#ffeda0' # '#FFEDA0' works too
    elif row.cnt_tags < 7:
        color = '#fed976'
    elif row.cnt_tags < 9:
        color = '#feb24c'
    elif row.cnt_tags < 11:
        color = '#fd8d3c'
    elif row.cnt_tags < 13:
        color = '#fc4e2a'
    else:
        color = '#bd0026'
    return color


def create_popup(row):    
    return Popup(IFrame("""
        {name} 
        <br>
        # tags: <b> {cnt} </b>
        <br>
        <a href="https://www.openstreetmap.org/{object_type}/{object_id}">link to OSM detail</a>
        """.format(name= row.library_name, 
                   cnt = row.cnt_tags,
                   object_type = row.object_type,
                   object_id = row.object_id), 
                        
                        width=230, height=110))
