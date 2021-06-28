def getANSTaggedStory(dataStory):
    ans = {
        "additional_properties": {
            "clipboard": {},
            "has_published_copy": True
        },
        "address": {},
        "canonical_website": "elcomercio",
        "content_elements": [
            {
                "_id": "EWQVXS6KVRCDLEQYWJMQ7N457U",
                "additional_properties": {
                    "_id": 1623970489223,
                    "comments": [],
                    "inline_comments": []
                },
                "content": "El fenómeno ha sido documentado en la región rural de Gippsland, donde la tela de araña llegó a cubrir más de un kilómetro de largo cerca a una de las vías principales, según el diario La Vanguardia de España. No es la primera vez que se registra un fenómeno así, aunque ha sorprendido el tamaño del mismo y la coordinación de los insectos para haber realizado un gran manto en lugar de varios pequeños. (Foto: Facebook de Carolyn Crossley vía Reuters)",
                "type": "text"
            },
            {
                "_id": "HZG6ENRUZBAW3NTARAIIBBCHZE",
                "referent": {
                    "id": "HZG6ENRUZBAW3NTARAIIBBCHZE",
                    "provider": "",
                    "referent_properties": {
                        "additional_properties": {
                            "_id": "73RYP4KUHFFCXNV7ZBSDA7GEYI",
                            "comments": []
                        }
                    },
                    "type": "gallery"
                },
                "type": "reference"
            }
        ],
        "content_restrictions": {
            "content_code": "free"
        },
        "created_date": "2021-06-17T22:43:27.751Z",
        "credits": {
            "by": [
                {
                    "referent": {
                        "id": "walter",
                        "provider": "",
                        "referent_properties": {},
                        "type": "author"
                    },
                    "type": "reference"
                }
            ]
        },
        "description": {
            "basic": ""
        },
        "display_date": "2021-06-17T22:46:57.652Z",
        "distributor": {
            "category": "staff",
            "name": "elcomercio",
            "subcategory": ""
        },
        "first_publish_date": "2021-06-17T22:46:57.652Z",
        "headlines": {
            "basic": "¿Por qué una enorme tela de araña cubrió los campos de un pueblo en Australia? | FOTOS",
            "meta_title": "¿Por qué una enorme tela de araña cubrió los campos de un pueblo en Australia? | FOTOS",
            "mobile": "",
            "native": "",
            "print": "",
            "tablet": "",
            "web": ""
        },
        "label": {},
        "language": "",
        "last_updated_date": "2021-06-17T22:56:07.369Z",
        "owner": {
            "id": "sandbox.elcomercio",
            "sponsored": False
        },
        "planning": {
            "internal_note": "",
            "story_length": {
                "character_count_actual": 452,
                "character_encoding": "UTF-16",
                "inch_count_actual": 1,
                "line_count_actual": 3,
                "word_count_actual": 81
            }
        },
        "promo_items": {
            "basic_gallery": {
                "_id": "UARPGAR5ENH6VHFVCN3PJPALD4",
                "referent": {
                    "id": "UARPGAR5ENH6VHFVCN3PJPALD4",
                    "provider": "",
                    "referent_properties": {},
                    "type": "gallery"
                },
                "type": "reference"
            }
        },
        "publish_date": "2021-06-17T22:56:07.146Z",
        "related_content": {
            "basic": [],
            "redirect": []
        },
        "revision": {
            "user_id": "walter.ybarra@fractalservicios.pe"
        },
        "source": {
            "name": "elcomercio",
            "source_type": "staff",
            "system": "composer"
        },
        "subheadlines": {
            "basic": "Los residentes del estado de Victoria registraron el peculiar manto que ha cubierto amplias zonas de la región australiana. El fenómeno respondería a una técnica de supervivencia de los arácnidos ante las lluvias torrenciales registradas en el país oceánico"
        },
        "subtype": "gallery_vertical",
        "taxonomy": {
            "additional_properties": {
                "parent_site_primaries": []
            },
            "tags": dataStory["tags"]
        },
        "type": "story",
        "version": "0.10.7",
        "workflow": {
            "status_code": 1
        }
    }

    return ans

def getANSStory(dataStory):
    ans = {"additional_properties": {
                "clipboard": {},
                "has_published_copy": False
            },
            "address": {},
            "canonical_website": "elcomercio",
            "content_elements": [
                {
                    "additional_properties": {
                        "comments": [],
                        "inline_comments": []
                    },
                    "content": "<br/>",
                    "type": "text"
                }
            ],
            "content_restrictions": {
                "content_code": "gratis"
            },
            "created_date": dataStory["creationDate"].strftime("%Y-%m-%dT%H:%M:%SZ"),
            "display_date": dataStory["creationDate"].strftime("%Y-%m-%dT%H:%M:%SZ"),
            "credits": {
                "by": [
                    {
                        'referent': {
                        'id': dataStory["story_author_id"],
                        'provider': '',
                        'referent_properties': {
                            
                        },
                        'type': 'author'
                        },
                        'type': 'reference'
                    }
                    ]
            },
            "description": {
                "basic": ""
            },
            "distributor": {
                "category": "staff",
                "name": "elcomercio",
                "subcategory": ""
            },
            "headlines": {
                "basic": dataStory["title"],
                "meta_title": "",
                "mobile": "",
                "native": "",
                "print": "",
                "tablet": "",
                "web": ""
            },
            "label": {},
            "language": "",
            "last_updated_date": dataStory["creationDate"].strftime("%Y-%m-%dT%H:%M:%SZ"),
            "owner": {
                "id": dataStory["story_owner"],
                "sponsored": False
            },
            "planning": {
                "internal_note": "",
                "story_length": {
                    "character_count_actual": 0,
                    "character_encoding": "UTF-16",
                    "inch_count_actual": 0,
                    "line_count_actual": 0,
                    "word_count_actual": 0
                }
            },
            "related_content": {
                "basic": [],
                "redirect": []
            },
            "revision": {
                "user_id": "luis.bustamante@fractal.com.pe"
            },
            "source": {
                "name": "elcomercio",
                "source_type": "staff",
                "system": "composer"
            },
            "subheadlines": {
                "basic": ""
            },
            "subtype": "gallery_slider",
            "taxonomy": {
                "additional_properties": {
                    "parent_site_primaries": []
                },
                "tags": dataStory["tags"]
            },
            "type": "story",
            "version": "0.10.7",
            "workflow": {
                "status_code": 1
            }
          }
    
    return ans

def createDocument(dataStory, creationDate):
    ans = {
            'additional_properties': {
                'clipboard': {
                
                },
                'has_published_copy': True
            },
            'address': {
                
            },
            'canonical_website': 'trome',
            'content_elements': [
                {
                    'additional_properties': {
                        'comments': [
                        
                        ],
                        'inline_comments': [
                        
                        ]
                    },
                    'content': dataStory["content"],
                    'type': 'text'
                }, 
                video_ans, 
                {
                    "additional_properties": {
                        "comments": [],
                        "inline_comments": []
                    },
                    "content": "<u><b>TE PUEDE INTERESAR</b></u>",
                    "level": 2,
                    "type": "header"
                },
                getANSRelated(related_ans)
            ],
            'content_restrictions': {
                'content_code': 'metered'
            },
            'created_date': creationDate.strftime("%Y-%m-%dT%H:%M:%SZ"),
            'credits': {
                'by': [
                {
                    'referent': {
                    'id': story_author_id,
                    'provider': '',
                    'referent_properties': {
                        
                    },
                    'type': 'author'
                    },
                    'type': 'reference'
                }
                ]
            },
            'description': {
                'basic': ''
            },
            'display_date': creationDate.strftime("%Y-%m-%dT%H:%M:%SZ"),
            'distributor': {
                'category': 'staff',
                'name': 'elcomercio',
                'subcategory': ''
            },
            'geo': {
                
            },
            'headlines': {
                'basic': dataStory["title"],
                'meta_title': dataStory["title"],
                'mobile': '',
                'native': '',
                'print': '',
                'tablet': '',
                'web': ''
            },
            'label': {
                
            },
            'language': '',
            'owner': {
                'id': story_owner,
                'sponsored': False
            },
            'planning': {
                'internal_note': '',
                'story_length': {
                'character_count_actual': 0,
                'character_encoding': 'UTF-16',
                'inch_count_actual': 0,
                'line_count_actual': 0,
                'word_count_actual': 0
                }
            },
            'promo_items': {
                'basic': {
                '_id': dataStory["promoItem"],
                'referent': {
                    'id': dataStory["promoItem"],
                    'provider': '',
                    'referent_properties': {
                    
                    },
                    'type': 'image'
                },
                'type': 'reference'
                }
            },
            # 'related_content': {
            #     'basic': related_stories,
            #     'redirect': [
                
            #     ]
            # },
            'revision': {
                'user_id': 'luis.bustamante@fractal.com.pe'
            },
            'source': {
                'name': 'elcomercio',
                'source_type': 'staff',
                'system': 'composer'
            },
            'subheadlines': {
                'basic': 'Descubre qué es lo que te deparan los astros con el acertado horóscopo Trome'
            },
            'subtype': 'horoscopo',
            'taxonomy': {
                'tags': [
                {
                    'description': 'Horóscopo',
                    'slug': 'horoscopo',
                    'text': 'Horóscopo'
                }
                ]
            },
            'type': 'story',
            'version': '0.10.7',
            'workflow': {
                'status_code': 1
            }
          }

    draftUri = story_api + "/draft/v1/story"
    draftResponse = requests.request("POST", draftUri, headers=auth_header, data=json.dumps(ans))
    document= json.loads(draftResponse.text)
    return document

def circulateStory(document_id):
    circulation = {
                    'document_id': document_id,
                    'website_id': 'trome',
                    'website_primary_section': {
                        'type': 'reference',
                        'referent': {
                            'type': 'section',
                            'id': '/horoscopo',
                            'provider': 'api.sandbox.elcomercio.arcpublishing.com/site/v3/website',
                            'website': 'trome'
                        }
                    },
                    'website_sections': [
                        {
                            'type': 'reference',
                            'referent': {
                                'type': 'section',
                                'id': '/horoscopo',
                                'provider': 'api.sandbox.elcomercio.arcpublishing.com/site/v3/website',
                                'website': 'trome'
                            }
                        }
                    ]
                  }

    circulateUri = story_api + "/draft/v1/story/" + document_id + "/circulation/trome"
    circulateResponse = requests.request("PUT", circulateUri, headers=auth_header, data=json.dumps(circulation))
    circulate = json.loads(circulateResponse.text)
    return circulate
    
def publishStory(document_id):
    publishUri = story_api + "/draft/v1/story/" + document_id + "/revision/published"
    publishResponse = requests.request("POST", publishUri, headers=auth_header)
    publish = json.loads(publishResponse.text)
    return publish