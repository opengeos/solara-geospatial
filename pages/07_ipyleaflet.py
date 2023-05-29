import ipyleaflet
import solara
import ipywidgets as widgets

zoom = solara.reactive(2)
center = solara.reactive((20, 0))


class Map(ipyleaflet.Map):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout.height = '600px'
        # Add what you want below

        label = widgets.Label('Clicked location')
        output = widgets.Output()
        widget = widgets.VBox([label, output])
        control = ipyleaflet.WidgetControl(widget=widget, position='bottomright')
        self.add_control(control)
        
        def handle_interaction(**kwargs):
            latlon = kwargs.get("coordinates")
            if kwargs.get("type") == "click":
                with output:
                    output.clear_output()
                    print(latlon)

        self.on_interaction(handle_interaction)


@solara.component
def Page():
    with solara.Column(style={"min-width": "500px"}):
        solara.SliderInt(label="Zoom level", value=zoom, min=1, max=20)
        Map.element(
            zoom=zoom.value,
            on_zoom=zoom.set,
            center=center.value,
            on_center=center.set,
            scroll_wheel_zoom=True,

        )
        solara.Text(f"Zoom: {zoom.value}")
        solara.Text(f"Center: {center.value}")
