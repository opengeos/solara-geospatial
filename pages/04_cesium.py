import os
import mapwidget.cesium as mapwidget

import solara

altitude = solara.reactive(400)
center = solara.reactive((37.655, -122.4175))

if os.environ.get('CESIUM_TOKEN') is None:
    token = 'YOUR-CESIUM-TOKEN'
else:
    token = os.environ.get('CESIUM_TOKEN')


@solara.component
def Page():
    with solara.Column(style={"min-width": "500px", "height": "500px"}):
        # solara components support reactive variables
        solara.SliderInt(label="Zoom level", value=altitude, min=1, max=1000)
        # using 3rd party widget library require wiring up the events manually
        # using zoom.value and zoom.set
        mapwidget.Map.element(  # type: ignore
            center=center.value, altitude=altitude.value, height='600px', width="100%"
        )
