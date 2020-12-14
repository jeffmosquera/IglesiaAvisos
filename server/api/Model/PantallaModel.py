from bson.objectid import ObjectId
import pymongo
from Database.MongoDB import MongoDB
from Utils.Datetime import Datetime
from Utils.JsonSerializer import JsonSerializer

db = MongoDB().db


class PantallaModel:

    @staticmethod
    def conseguir_por_id(_id):
        query = db.pantalla.find_one(
            {"_id": ObjectId(_id), "activo": True})
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def actualizar(_id, data):
        data["actualizado"] = Datetime.get_current_datetime()
        db.pantalla.update_one(
            {"_id": ObjectId(_id)},
            {"$set": data}
        )
