import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## Solara for Geospatial Applications
        
        ### Introduction

        **A collection of [Solara](https://github.com/widgetti/solara) web apps for geospatial applications.**

        Just a proof-of-concept for now. Not all features are working yet. More features will be added in the future. Click on the menu above to see the other pages.

        - Web App: <https://giswqs-solara-geospatial.hf.space>
        - GitHub: <https://github.com/opengeos/solara-geospatial>
        - Hugging Face: <https://huggingface.co/spaces/giswqs/solara-geospatial>

        ### Demos

        ![](https://i.imgur.com/4uIEnAJ.gif)

        """

        solara.Markdown(markdown)
