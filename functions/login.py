import json

def question ():
    return {
    "fulfillmentMessages": [{
        "payload": {
            "richContent": [
                [
                    {
                        "type": "chips",
                        "options": [
                            {
                                "text": "Anmelden",
                            },
                            {
                                "text": "Registrieren",
                            }
                        ]
                    }
                ]
            ]

        }
    }]
    }