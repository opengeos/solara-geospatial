import solara

@solara.component
def Page():

    markdown = """
    ## Solara for Geospatial Applications
    
    ### Introduction

    **A collection of [solara](https://github.com/widgetti/solara) web apps for geospatial applications.**

    Just a proof-of-concept for now. Not all features are working yet. More features will be added in the future. Click on the menu above to see the other pages.

    - Web App: <https://giswqs-solara-geospatial.hf.space>
    - Solara-Geospatial: <https://github.com/opengeos/solara-geospatial>

    ### Demos

    #### Cesium

    ![](https://i.imgur.com/6quoDtN.gif)

    #### Mapbox

    ![](https://i.imgur.com/4uIEnAJ.gif)

    #### MapLibre

    ![](https://i.imgur.com/o2ZHeTL.gif)

    """

    solara.Markdown(markdown)
