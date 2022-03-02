from pypresence import Presence
import time

client_id = '948366267725795328'
RPC = Presence(client_id)
RPC.connect()

RPC.update(state="https://war.ukraine.ua/", details="#StopRussianAggression", large_image="flag_of_ukraine_svg", large_text="Ukranian Flag", buttons=[{"label": "#StandWithUkraine", "url": "https://war.ukraine.ua/stand-with-ukraine/"}, {"label": "Why?", "url": "https://war.ukraine.ua/why/"}])

while True:
    time.sleep(15)
