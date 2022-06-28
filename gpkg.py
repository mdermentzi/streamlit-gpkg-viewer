import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
import folium


st.title('EHRI Geopackage Viewer')

uploaded_gpkg = st.sidebar.file_uploader("Upload a .gpkg file to inspect its contents.",type=['gpkg'])

if uploaded_gpkg is not None:
    gdf = gpd.read_file(uploaded_gpkg)

    view = st.radio(
        "How would you like to inspect your data?",
        ('Map','Table'))

    if view == 'Map':
        # Create a geometry list from the GeoDataFrame
        map = folium.Map(location=[48.674646, 17.115542], zoom_start=5)

        geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry]
        i = 0
        for coordinates in geo_df_list:
            # Place the markers with the popup labels and data
            map.add_child(folium.CircleMarker(location=coordinates,
                                        radius=5,
                                        color="#3186cc",
                                        fill=True,
                                        fill_color="#3186cc",
                                        popup=
                                        "Coordinates: " + str(
                                            geo_df_list[i])+ '<br>' +
                                        "Index: " + str(i)
                                        ,
                                        )
                          )
            i = i + 1

        output = st_folium(map, width=725, height=500)
        st.write('Inspect an entry by its index:')
        index = st.text_input('Index', '')
        st.write('Selected Index:', index)
        if index:
            st.write(gdf.iloc[int(index)].tolist())
    else:
        st.write(gdf)

