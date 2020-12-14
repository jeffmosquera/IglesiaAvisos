from bson.objectid import ObjectId
import pymongo
from Database.MongoDB import MongoDB
from Utils.Datetime import Datetime
from Utils.JsonSerializer import JsonSerializer

db = MongoDB().db


class EventoModel:

    @staticmethod
    def conseguir_todo():
        query = db.eventos.find({"activo": True}, sort=[
                                ('creado', pymongo.DESCENDING)])
        query = list(query)
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def conseguir_todo_ordenado_por_datetimeDate():
        query = db.eventos.find({"activo": True}, sort=[
                                ('datetimeDate', pymongo.ASCENDING)])
        query = list(query)
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def conseguir_por_id(_id):
        query = db.eventos.find_one(
            {"_id": ObjectId(_id), "activo": True})
        query = JsonSerializer.serialize(query)
        return query

    @staticmethod
    def guardar(data):
        data["activo"] = True
        data["creado"] = Datetime.get_current_datetime()
        data["actualizado"] = Datetime.get_current_datetime()
        data["datetimeDate"] = Datetime.convert_timestamp_to_datetime(
            data["timestampDate"])
        inserted_id = db.eventos.insert_one(data).inserted_id
        return inserted_id

    @staticmethod
    def actualizar(_id, data):
        data["actualizado"] = Datetime.get_current_datetime()
        if "timestampDate" in data:
            data["datetimeDate"] = Datetime.convert_timestamp_to_datetime(
                data["timestampDate"]+60*60*5)
        if "datetimeDate" in data:
            data["datetimeDate"] = Datetime.convert_timestamp_to_datetime(
                data["timestampDate"])
        db.eventos.update_one(
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
        db.eventos.update_one(
            {"_id": ObjectId(_id)},
            {"$set": data}
        )
