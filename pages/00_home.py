import solara

@solara.component
def Page():

    markdown = """
    ## Solara for Geospatial Applications
    
    Just a proof-of-concept for now. Not all features are working yet. More features will be added in the future. Click on the menu above to see the other pages.

    GitHub: <https://github.com/opengeos/solara-geospatial>
    Solara: <https://github.com/widgetti/solara>

    ![](https://i.imgur.com/1PbtnQE.gif)
    """

    solara.Markdown(markdown)
