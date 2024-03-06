from tkinter import *
import requests

# Function to fetch Kanye West quote from the API
def get_quote():
    request = requests.get("https://api.kanye.rest")
    request.raise_for_status()
    data = request.json()["quote"]
    canvas.itemconfig(quote_text, text=data)

# Creating the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Creating a canvas for displaying the quote
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Adding a button to fetch a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
