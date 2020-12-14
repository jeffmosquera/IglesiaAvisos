from bson.objectid import ObjectId

from Database.MongoDB import MongoDB
from Utils.Datetime import Datetime
from Utils.JsonSerializer import JsonSerializer

db = MongoDB().db


class AdministradorModel:

    @staticmethod
    def conseguir_todo():
        query = db.administradores.find({"activo": True})
        query = list(query)
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def conseguir_por_id(_id):
        query = db.administradores.find_one(
            {"_id": ObjectId(_id), "activo": True})
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def buscar_por_correo(correo):
        query = db.administradores.find_one({'correo': correo})
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def guardar(data):
        data["activo"] = True
        data["creado"] = Datetime.get_current_datetime()
        data["actualizado"] = Datetime.get_current_datetime()
        inserted_id = db.administradores.insert_one(data).inserted_id
        return inserted_id

    @staticmethod
    def actualizar(_id, data):
        data["actualizado"] = Datetime.get_current_datetime()
        db.administradores.update_one(
            {"_id": ObjectId(_id)},
            {"$set": data}
        )

    @staticmethod
    def borrar(_id):
        data = {
            "activo": False,
            "creado": Datetime.get_current_datetime(),
            "actualizado": Datetime.get_current_datetime()
        }
        db.administradores.update_one(
            {"_id": ObjectId(_id)},
            {"$set": data}
        )
