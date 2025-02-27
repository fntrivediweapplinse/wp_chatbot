from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def check_db(request):
    from ..models import TblPortfolio

    data = list(TblPortfolio.objects.filter().values())
    
    value = "𝐇𝐞𝐥𝐥𝐨"

    response_data = {
        "fulfillmentMessages": [
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "description",
                                "title": "Welcome!",
                                "text": [
                                    "**Click** the button below to visit our website:",
                                    "<a href='https://example.com' target='_blank'><button>Visit Site</button></a>"
                                ]
                            }
                        ]
                    ]
                }
            }
        ]
    }



    return JsonResponse(response_data)