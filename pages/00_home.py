import solara

@solara.component
def Page():

    markdown = """
    ## Solara for Geospatial Applications
    
    ### Introduction

    **A collection of [Solara](https://github.com/widgetti/solara) web apps for geospatial applications.**

    Just a proof-of-concept for now. Not all features are working yet. More features will be added in the future. Click on the menu above to see the other pages.

    - Web App: <https://giswqs-solara-geospatial.hf.space>
    - Solara-Geospatial: <https://github.com/opengeos/solara-geospatial>

    ### Demos

    ![](https://i.imgur.com/4uIEnAJ.gif)

    """

    solara.Markdown(markdown)
