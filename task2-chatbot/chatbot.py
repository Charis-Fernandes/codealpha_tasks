import customtkinter as ctk
from tkinter import END
from PIL import Image, ImageTk, ImageOps, ImageDraw
import string

app = ctk.CTk()
app.title("Chatbot")

app.configure(bg="black")

def create_circular_image(image_path, size=(50, 50)):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.Resampling.LANCZOS) 
        mask = Image.new('L', size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, size[0], size[1]), fill=255)
        img.putalpha(mask)
        img = ImageOps.fit(img, size, centering=(0.5, 0.5))
        return ImageTk.PhotoImage(img)

user_image = create_circular_image("image_2024-08-15_223400564-transformed (1).png")  
bot_image = create_circular_image("pngtree-a-symbol-of-the-alpha-in-the-form-of-mutual-cut-image_302423.jpg")   

def exit_fullscreen(event=None):
    app.overrideredirect(False)
    app.state("normal")

def send_message(event=None):
    user_message = entry.get()
    if user_message.strip() != "":
        display_message("You", user_message, user_image)
        entry.delete(0, END)

        user_message_cleaned = user_message.translate(str.maketrans('', '', string.punctuation)).lower()
        
        bot_response = generate_bot_response(user_message_cleaned)
        display_message("Bot", bot_response, bot_image)

def generate_bot_response(user_message):
    responses = {
        "hi": "Hello!",
        "how are you": "I'm always good!",
        "bye": "Goodbye!",
        "who are you": "I'm a bot made for CodeAlpha!",
        "sup": "What's up?",
        "make a wish": "I wish to serve you!",
        "happy birthday": "Thanks!",
        "today's my birthday": "Happy Birthday!",
        "how old are you?": "I was born yesterday",
        "website?":"It's Casca.in"
    }

    cleaned_responses = {k.translate(str.maketrans('', '', string.punctuation)).lower(): v for k, v in responses.items()}

    return cleaned_responses.get(user_message, "Sorry, I don't understand that.")

def display_message(sender, message, profile_image):
    message_frame = ctk.CTkFrame(chatbox, fg_color="grey")
    message_frame.pack(anchor="w", fill="x", pady=5, padx=10)  # Adjust padding here

    profile_label = ctk.CTkLabel(message_frame, image=profile_image, text="")
    profile_label.pack(side="left", padx=5)

    message_label = ctk.CTkLabel(message_frame, text=f"{sender}: {message}", fg_color="white", text_color="black", anchor="w")
    message_label.pack(side="left", fill="x", padx=5)

frame = ctk.CTkFrame(app, fg_color="grey")
frame.pack(fill="both", expand=True, padx=10, pady=10)

chatbox = ctk.CTkCanvas(frame, bg="grey")
chatbox.pack(fill="both", expand=True, padx=10, pady=10)

input_frame = ctk.CTkFrame(app, fg_color="grey")
input_frame.pack(fill="x", side="bottom", padx=10, pady=10)

entry = ctk.CTkEntry(input_frame, height=30)
entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

entry.bind("<Return>", send_message)

send_button = ctk.CTkButton(input_frame, text="Send", command=send_message)
send_button.pack(side="right", padx=10, pady=10)

app.bind("<Escape>", exit_fullscreen)

app.mainloop()
