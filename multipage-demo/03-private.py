import solara

clicks = solara.reactive(0)


@solara.component
def Page():
    color = "green"
    if clicks.value >= 5:
        color = "red"

    def increment():
        clicks.value += 1
        print("clicks", clicks)  # noqa
    
    solara.Markdown(f"# Click the button one time and go to public window")
    solara.Button(label=f"Clicked: {clicks}", on_click=increment, color=color)
