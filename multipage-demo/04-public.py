import solara
from solara.alias import rv

# create class
class Person:
    name = "John"
    age = 0

# create objects of class
personModel = Person()
clicks = solara.reactive(0)
# person = solara.reactive(personModel)
color = 'blue'

@solara.component
def MarkdownEditor():
    # markdown_text, set_markdown_text = solara.use_state(markdown_initial)
    with solara.ColumnsResponsive(12, medium=6):
        with solara.Sidebar():
            with solara.Row():
                def increment():
                    clicks.value += 1
                    personModel.age += 1
                    personModel.name += '1'
                solara.Button(label=f"Clicked: {clicks}", on_click=increment, color=color)
        with solara.Column():
            with solara.Padding(2):
                solara.Markdown(f"# Input text {personModel.__dict__}")
        with solara.Column():
            with solara.Padding(2):
                solara.Markdown(f"# Click the sidenav button and click the button to update the object")

        print("markdown_initial", clicks)

# # create an alias of the Markdown Editor component so Solara can find it
Page = MarkdownEditor