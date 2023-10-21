import customtkinter
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup as bs
from tkinter import *

app = customtkinter.CTk()
app.title("val")
app.geometry("650x320")
app.minsize(650, 350)
app.maxsize(650, 350)


def button_click_event():
    nick = textbox_nick.get('1.0', END).strip()
    numbers = textbox_numbers.get('1.0', END).strip()
    process_nickname(nick+"#"+numbers)


def process_nickname(nickname):
    site = f'https://tracker.gg/valorant/profile/riot/{nickname}/overview?season=all'.replace(' ', '%20').replace('#', '%23')

    r = requests.get(site)
    try:
        soup = bs(r.text, 'html.parser')

        label_nickname.configure(text=f"nickname : {nickname} ")

        div_el = soup.find(class_='rating-summary__content rating-summary__content--secondary')

        bottom_element = div_el.find(class_='value')
        bottom_value = bottom_element.text if bottom_element else None
        label_peak_rank.configure(text=f"Peak rating : { bottom_value}")

        rating = soup.find('span', class_='stat__value')
        rating_title = rating.text if rating else None
        label_rank.configure(text=f"Rang :{rating_title}")

        div_elements = soup.find_all(class_='stat align-left giant expandable')

        kd_ratio_element = div_elements[1].find(class_='value')
        kd_ratio_value = kd_ratio_element.text if kd_ratio_element else None
        label_ratio.configure(text=f"K/D Ratio : {kd_ratio_value}")

        matches = soup.find('span', class_='matches')
        matches_value = matches.text if matches else None
        label_matches.configure(text=f"Matches : {matches_value}")

        play_time = soup.find('span', class_='playtime')
        play_time_value = play_time.text if play_time else None
        label_playtime.configure(text=f"Play time : {play_time_value}")

        div_elements = soup.find_all(class_='st__item st-content__item-value st__item--sticky st__item--wide')

        if div_elements:
            for i, div_elem in enumerate(div_elements):
                agent_element = div_elem.find(class_='value')
                game_element = div_elem.find(class_='label')

                if agent_element and game_element:
                    agent = agent_element.text.strip()
                    game = game_element.text.strip()

                    if i == 0:
                        label_hero1.configure(text=f"Agent: {agent}\nGame: {game}")
                    elif i == 1:
                        label_hero2.configure(text=f"Agent: {agent}\nGame: {game}")
                    elif i == 2:
                        label_hero3.configure(text=f"Agent: {agent}\nGame: {game}")
                else:
                    messagebox.showinfo("Error", "Not found agents")
        else:
            messagebox.showinfo("Error", "Not found agents")

    except AttributeError:
        messagebox.showinfo("Error", "This player was not found or you typed the nickname incorrectly")
    except ConnectionError:
        messagebox.showinfo("Error", "Error connect")


frame1 = customtkinter.CTkFrame(app)
frame2 = customtkinter.CTkFrame(app)
frame3 = customtkinter.CTkFrame(app)

textbox_nick = customtkinter.CTkTextbox(app, height=20, width=150)
textbox_numbers = customtkinter.CTkTextbox(app, height=20, width=150)

button = customtkinter.CTkButton(app, text="Find a player", command=button_click_event)

label_info = customtkinter.CTkLabel(app, text="Info")
label_nick = customtkinter.CTkLabel(app, text="Nickname")
label_numbers = customtkinter.CTkLabel(app, text="Numbers")
label_nickname = customtkinter.CTkLabel(frame1, text="NIK :                        ")
label_peak_rank = customtkinter.CTkLabel(frame1, text="Peak rating :               ")
label_rank = customtkinter.CTkLabel(frame1, text="Rang :                           ")
label_ratio = customtkinter.CTkLabel(frame2, text="K/D Ratio :                     ")
label_matches = customtkinter.CTkLabel(frame2, text="Matches :                     ")
label_playtime = customtkinter.CTkLabel(frame2, text="Play time :                  ")

label_hero1 = customtkinter.CTkLabel(frame3, text="Agent:                          \nGame:                           ")
label_hero2 = customtkinter.CTkLabel(frame3, text="Agent:                          \nGame:                           ")
label_hero3 = customtkinter.CTkLabel(frame3, text="Agent:                          \nGame:                           ")

frame1.grid(row=2, column=0, padx=30, pady=30)
frame2.grid(row=2, column=1, padx=30, pady=30)
frame3.grid(row=2, column=2, padx=30, pady=30)

textbox_nick.grid(row=1, column=0, padx=10, pady=10)
textbox_numbers.grid(row=1, column=1, padx=10, pady=10)

button.grid(row=1, column=2, padx=10, pady=10)

label_nick.grid(row=0, column=0, padx=10, pady=10)
label_numbers.grid(row=0, column=1, padx=10, pady=10)
label_info.grid(row=0, column=2, padx=10, pady=10)
label_nickname.grid(padx=10, pady=10)
label_peak_rank.grid(padx=10, pady=10)
label_rank.grid(padx=10, pady=10)
label_playtime.grid(padx=10, pady=10)
label_ratio.grid(padx=10, pady=10)
label_matches.grid(padx=10, pady=10)

label_hero1.grid(padx=10, pady=10)
label_hero2.grid(padx=10, pady=10)
label_hero3.grid(padx=10, pady=10)

app.mainloop()
