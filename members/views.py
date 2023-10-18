from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from firebase_admin import messaging
from django.http import JsonResponse



def home(request):

  return render(request, 'members/home.html')

def members(request):
  template = loader.get_template('members/all_members.html')
  return HttpResponse(template.render()) 

def send_push_notification(request):
    try:
        # Retrieve the user's FCM registration token from your database
        #user = Member.objects.get(id=id)
        registration_token = "crN-oOkjSnW8c_yrJr1iF6:APA91bEF8fxI5n62ov50gfYYWmEreB21NGvH4lH396EUezFH90vEoOAUIJT55SvohrbrqM3JLeByDjhpo-v_n38jqdpopohNZ1k8TR62EZ8nfiTgVB4eZVTtsZOj7VzAPktHHiYaDkzh"

        # Construct a message
        message = messaging.Message(
            notification=messaging.Notification(
			title='Fiat-Doblo 2023',  # Notification title
			body='Votre text ici avec l url avec url avec url'  # Notification body
			),
			data={
			'click_action': 'FLUTTER_NOTIFICATION_CLICK',  # Required for Android to handle click action
			'url': 'https://hafiddjango.pythonanywhere.com/fr/product/1/peugeot-308-1267/',  # The clickable URL you want to open
			},
			
            token=registration_token
        )

        # Send the message
        response = messaging.send(message)
        print('Successfully sent message:', response)

        return JsonResponse({'message': 'Notification sent successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)