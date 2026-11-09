import orjson
import json
import os

global cards
cards = json.load(open("cards.json", "r+"))

def saveCard(name: str, contents: str, answer: str):
    cards["cards"].append({"id": str(len(cards["cards"])), "name": name, "contents": contents, "answer": answer})
    os.truncate("cards.json", 0)
    json.dump(cards, open("cards.json", "w"), separators=(",", ":"), indent=4)
    
def deleteCard(cardID: int):
    try:
        cards["cards"].pop(cardID)
    except IndexError:
        print("ERR: attempting to delete non-existent card")
    os.truncate("cards.json", 0)
    json.dump(cards, open("cards.json", "w"), separators=(",", ":"), indent=4)

def clearCards():
    for cardNum in range(len(cards["cards"])):
        deleteCard(0)

