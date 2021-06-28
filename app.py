import os
import requests
import json
from storyutils import *
from datetime import datetime, timedelta, date
from collections import OrderedDict
from flask import Flask, jsonify, request
app = Flask(__name__)


story_api = os.environ['EC_STORY_API']
story_api_token = os.environ['EC_API_TOKEN']
story_author_id = os.environ['STORY_AUTHOR_ID']
story_owner = os.environ['STORY_OWNER']

auth_header = {"Authorization": "Bearer " + story_api_token}

elements = []

elements.append(["Test de publica", "DISTRITOS CALLAO CALLAO CERCADO"])

@app.route("/elections")
def elections():
    now = datetime.now()
    dateStory = now-timedelta(days=30)
    draftUri = story_api + "/draft/v1/story"

    dataStory = {"creationDate": dateStory, "story_author_id": story_author_id, "story_owner": story_owner}
    i = 0
    # for region in elements:
    #     for element in region:
    #         dataStory["title"] = element
    #         ans = getANSElectionsStory(dataStory)
    #         draftResponse = requests.request("POST", draftUri, headers=auth_header, data=json.dumps(ans))
    #         document= json.loads(draftResponse.text)

    #         print(element + ": " + document["id"])
    #     i += 1
    ans = getANSTaggedStory(dataStory)
    draftResponse = requests.request("POST", draftUri, headers=auth_header, data=json.dumps(ans))
    document= json.loads(draftResponse.text)

    print("=> " + document["id"])

    return "Finish"

@app.route("/test")
def test():
    stories = [{"title": "Titular de Peru21", "tags": [
                {
                    "description": "Tag nuevo 1",
                    "slug": "tag-nuevo-1",
                    "text": "Tag nuevo 1"
                },
                {
                    "description": "Prueba de Walter",
                    "slug": "prueba-de-walter",
                    "text": "PRueba de Walter"
                },
            ]}, 
               {"title": "Prueba de historia Trome", "tags": [
                {
                    "description": "Año Nuevo",
                    "slug": "ano-nuevo",
                    "text": "Año Nuevo"
                },
                {
                    "description": "Sergio Castellón",
                    "slug": "sergio-castellon",
                    "text": "Sergio Castellón"
                },
            ]}
              ]



    now = datetime.now()
    dateStory = now-timedelta(days=30)
    draftUri = story_api + "/draft/v1/story"

    dataStory = {"creationDate": dateStory, "story_author_id": story_author_id, "story_owner": story_owner}
    for element in stories:
        dataStory["title"] = element["title"]
        dataStory["tags"] = element["tags"]
        ans = getANSStory(dataStory)
        draftResponse = requests.request("POST", draftUri, headers=auth_header, data=json.dumps(ans))
        document= json.loads(draftResponse.text)

        print(element["title"] + ": " + document["id"])

    return "Finish 2"