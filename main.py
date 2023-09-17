from tkinter import *

import requests
 
def get_quote():
    response = requests.get(
        url = "https://api.kanye.rest"
    )

    response.raise_for_status()

    data = response.json()
    kanye_quote = data["quote"]
    canvas.itemconfig(quote_text, text = kanye_quote)
    
BACKGROUND_COLOR = "#82A0D8"

# App UI
window = Tk()
window.title("Kanye Thinks ...")
window.config(
    padx = 50,
    pady = 50,
    bg = BACKGROUND_COLOR
)

canvas = Canvas(
    width = 366,
    height = 389,
    background= BACKGROUND_COLOR,
    highlightthickness = 0
)

quote_image = "./thinking_clouds.png"
quote_clouds = PhotoImage(file = quote_image)

cloud_background = canvas.create_image(
    183,
    194,
    image = quote_clouds
)

quote_text = canvas.create_text(
    183,
    150,
    text = "What Kanye is thinking ...",
    fill = "white",
    font = ("Ariel", 16, "italic")
)

canvas.grid(
    column = 0,
    row = 0
)

# Button
kanye_image = "./kanye.png"
kanye_image_button = PhotoImage(file = kanye_image)
kanye_button = Button(
    image = kanye_image_button,
    highlightthickness = 0,
    command = get_quote,
    background = BACKGROUND_COLOR 
)

kanye_button.grid(
    column = 0,
    row = 1
)

window.mainloop()