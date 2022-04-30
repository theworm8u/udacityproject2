import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://udacitydavidcosmosdbp2:vbHyqfNrMRl0Fgn06i7MPTMVAerUZ7p9gg3Ocxn6VMcVZVBCIfpM2xeRKllz9E1BhFwxM3wfBdt2HQs2tjuJ0A==@udacitydavidcosmosdbp2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@udacitydavidcosmosdbp2@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['udacitydavidproj2mongodb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )