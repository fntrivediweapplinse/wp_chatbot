from django.urls import path
from .views import webhook, test_db

urlpatterns = [
    path("webhook/", webhook.dialogflow_webhook, name="dialogflow_webhook"),
    path("checkdb/",test_db.check_db)
]