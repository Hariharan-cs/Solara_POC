from solara import *
import reacton.ipyvuetify as rv

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = solara.reactive("Solara makes our team more productive.")
word_limit = solara.reactive(10)


@solara.component
def SentenceValidator():
    # Calculate word_count within the component to ensure re-execution when reactive variables change.
    word_count = len(sentence.value.split())

    solara.SliderInt("Word limit", value=word_limit, min=2, max=20)
    solara.InputText(label="Your sentence", value=sentence, continuous_update=True)

    # Display messages based on the current word count and word limit.
    if word_count >= int(word_limit.value):
        solara.Error(f"With {word_count} words, you passed the word limit of {word_limit.value}.")
    elif word_count >= int(0.8 * word_limit.value):
        solara.Warning(f"With {word_count} words, you are close to the word limit of {word_limit.value}.")
    else:
        solara.Success("Great short writing!")


# The following line is required only when running the code in a Jupyter notebook:


counter = solara.reactive(0)

def increment():
    counter.value += 1

@solara.component
def CounterDisplay():
    solara.Info(f"Counter: {counter.value}")

@solara.component
def IncrementButton():
    with Row():
        Button("Increments", color="#fffff", icon_name="./protecto-logo", on_click=increment)

color = solara.reactive("red")

@solara.component
def SomeAppSpecificComponent():
    solara.Select(label="Color", values=["red", "green", "blue", "orange"], value=color)
    solara.Markdown("### Solara is awesome", style={"color": color.value})
    clicks, set_clicks = solara.use_state(0)
    def my_click_handler(*ignore_args):
        # trigger a new render with a new value for clicks
        set_clicks(clicks+1)
    button = rv.Btn(children=[f"Clicked {clicks} times"])
    rv.use_event(button, 'click', my_click_handler)
    return button

@solara.component
def sidenav(): 
    with solara.Column():
        solara.Title("I'm in the browser tab and the toolbar")
        with solara.Sidebar():
            solara.Markdown("## I am in the sidebar")
            solara.SliderInt(label="Ideal for placing controls")
        solara.Info("I'm in the main content area, put your main content here")
        with solara.Card("Use solara.Columns([1, 2]) to create relatively sized columns"):
            with solara.Columns([1, 2]):
                solara.Success("I'm in the first column")
                solara.Warning("I'm in the second column, I am twice as wide")
                solara.Info("I am like the first column")

        with solara.Card("Use solara.Column() to create a full width column"):
            with solara.Column():
                solara.Success("I'm first in this full with column")
                solara.Warning("I'm second in this full with column")
                solara.Error("I'm third in this full with column")

        with solara.Card("Use solara.ColumnsResponsive(6, large=4) to response to screen size"):
            with solara.ColumnsResponsive(6, large=4):
                for i in range(6):
                    solara.Info("two per column on small screens, three per column on large screens")


# @solara.component
# def Layout(children=[5]):
#     # Note that children being passed here for this example will be a Page() element.
#     route_current, routes_all = solara.use_route()
#     with solara.Column():
#         # put all buttons in a single row
#         with solara.Row():
#             for route in routes_all:
#                 with solara.Link(route):
#                     solara.Button(route.path, color="red" if route_current == route else None)
#         # under the navigation buttons, we add our children (the single Page())
#         solara.Column(children=children)

# @solara.component
# def Page(name: str = "foo"):
#     subpages = ["foo", "bar", "solara", "react-ipywidgets"]
#     solara.Markdown(f"You are at: {name}")
#     # bunch of buttons which navigate to our dynamic route
#     with solara.Row():
#         for subpage in subpages:
#             with solara.Link(subpage):
#                 solara.Button(label=f"Go to: {subpage}")

# @solara.component
# def Home():
#     solara.Markdown("Home")


# @solara.component
# def About():
#     solara.Markdown("About")


# routes = [
#     solara.Route(path="/", component=Home, label="home"),
#     solara.Route(path="about", component=About, label="about"),
# ]

@solara.component
def Page():
    IncrementButton()
    CounterDisplay()
    SentenceValidator()
    SomeAppSpecificComponent()
    # sidenav()
    # # Layout()
    # # Page()
    # Home()
    # About()
