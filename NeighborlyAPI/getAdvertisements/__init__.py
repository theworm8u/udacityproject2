import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://udacitydavidcosmosdbp2:vbHyqfNrMRl0Fgn06i7MPTMVAerUZ7p9gg3Ocxn6VMcVZVBCIfpM2xeRKllz9E1BhFwxM3wfBdt2HQs2tjuJ0A==@udacitydavidcosmosdbp2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@udacitydavidcosmosdbp2@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['udacitydavidproj2mongodb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

