from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def dialogflow_webhook(request):
    """
    Handles Dialogflow webhook requests.
    """
    try:
        print(f"Received {request.method} request")

        if not request.body:
            print("❌ Empty request body")
            return JsonResponse({"error": "Empty request body"}, status=400)

        raw_data = request.body.decode("utf-8")
        print("🔹 Raw Request Body:", raw_data)

        req = json.loads(raw_data)
        print("✅ Parsed JSON:", req)

        intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

        if intent_name == "Default Fallback Intent":
            response_data = {
                "fulfillmentMessages": [
                    {
                        "payload": {
                            "richContent": [
                                [
                                    {
                                        "type": "description",
                                        "title": "Need Help?",
                                        "text": [
                                            "Click the link below to contact us:",
                                            "[Visit Our Website](https://commons-candle-end-trim.trycloudflare.com/)"
                                        ]
                                    }
                                ]
                            ]
                        }
                    }
                ]
            }


            return JsonResponse(response_data) 

        return JsonResponse({"message": "Intent not handled"}, status=200)

    except json.JSONDecodeError:
        print("❌ JSON Decode Error")
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    except Exception as e: 
        print(f"❌ An error occurred: {e}")
        return JsonResponse({"error": f"An error occurred: {e}"}, status=500)