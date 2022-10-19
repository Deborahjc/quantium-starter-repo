from interactive_app import app


def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element(id="header", timeout=20)
    dash_duo.wait_for_element(id="my_graph", timeout=20)
    dash_duo.wait_for_element(id="region", timeout=20)

    


