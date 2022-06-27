import streamlit as st
import pandas as pd
import geopandas as gpd

st.title('Geopackage Viewer')


uploaded_gpkg = st.sidebar.file_uploader("Upload a .gpkg file to inspect its contents.",type=['gpkg'])

if uploaded_gpkg is not None:
    gdf = gpd.read_file(uploaded_gpkg)

    gdf['lon'] = gdf.geometry.apply(lambda p: p.x)
    gdf['lat'] = gdf.geometry.apply(lambda p: p.y)

    st.map(gdf)
    st.write(gdf)
