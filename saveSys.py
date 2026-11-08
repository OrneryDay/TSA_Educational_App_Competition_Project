import json
import os



def formatCard(name: str, description: str, id = None):
    if id == None:
        id = len(json.load(open("cards.json", "r"))["cards"] - 1)
    return {
        "id": id,
        "name": name,
        "description": description
    }

def saveCard(contents):
    save = json.load(open("cards.json", "r"))
    save["cards"].append(contents)
    json.dump(save, open("cards.json", "w"), indent=4)
    #with open("cards.json", "a") as f:
    #    json.dump(contents, f)
    #    f.write("\n")

def removeFile(itemID: int):
    file = open("cards.json", "r+")
    contents = json.load(file)
    try:
        contents["cards"].pop(itemID)
    except IndexError:
        print("Item not found")
    print(contents["cards"][0]['id'])
    saveCard(contents)
    #if item in contents:
    #    del contents[contents.index(item)]
    #    json.dump(contents, open("cards.json", "w"))
    
"""
import json
import os



def formatCard(name: str, description: str, id = None):
    if id == None:
        id = len(json.load(open("cards.json", "r"))["cards"]) - 1
    return {
        "id": id,
        "name": name,
        "description": description
    }

class savingSys:
    global saveFile
    saveFile = open("cards.json", "r+")


    def JSONCheck(self):
        if saveFile == "" or saveFile == None:
            json.dump({"cards": []}, saveFile)

    def saveCard(self, contents):
        print(type(saveFile), "\n", saveFile)

        JSONSave = json.load(saveFile)
        JSONSave["cards"].append(contents)
        #os.truncate("cards.json", 0)
        #print(f"file contents:{JSONSave["cards"]}\nvariable contents: {saveFile}")
        #json.dump(JSONSave, open("cards.json", "w"), indent=4)

    def removeFile(self, itemID: int):
        file = open("cards.json", "r+")
        contents = json.load(file)
        try:
            contents["cards"].pop(itemID)
        except IndexError:
            print("Item not found")
        savingSys.saveCard(self, contents)
        #if item in contents:
        #    del contents[contents.index(item)]
        #    json.dump(contents, open("cards.json", "w"))
"""
