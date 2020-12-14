from bson.objectid import ObjectId

from Database.MongoDB import MongoDB
from Utils.Datetime import Datetime
from Utils.JsonSerializer import JsonSerializer

db = MongoDB().db


class UsuarioModel:

    @staticmethod
    def conseguir_todo():
        query = db.usuarios.find({"activo": True})
        query = list(query)
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def buscar_por_telefono(telefono):
        query = db.usuarios.find_one({'telefono': telefono, 'activo': True})
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def conseguir_por_id(_id):
        query = db.usuarios.find_one(
            {"_id": ObjectId(_id), "activo": True})
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def guardar(data):
        data["activo"] = True
        data["creado"] = Datetime.get_current_datetime()
        data["actualizado"] = Datetime.get_current_datetime()
        inserted_id = db.usuarios.insert_one(data).inserted_id
        return inserted_id

    @staticmethod
    def actualizar(_id, data):
        data["actualizado"] = Datetime.get_current_datetime()
        db.usuarios.update_one(
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
        db.usuarios.update_one(
            {"_id": ObjectId(_id)},
            {"$set": data}
        )
