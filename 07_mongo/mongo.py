#Team YaThatWasABanana --
import pymongo
import os

os.system("sudo mv pkmn.json ../../data/db")
os.system("mongoimport --db YaThatWasABanana --collection pkmn --drop --file ~/data/db/pkmn.json")
SERVER_ADDR = "206.81.13.98"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.YaThatWasABanana
collection = db.pkmn

print(list(collection.find({"pokemon.id": 1})))
