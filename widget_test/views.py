from django.shortcuts import render

def get_bot_widget(request):
    data = {'content': 'Testing after a long time'}
    
    return render(request, 'bot_widget.html',data)


def get_rasa_webchat(request):
    return render(request, 'rasa_webchat.html')


def get_botcopy_widget(request):
    return render(request, 'botcopy_bot.html')