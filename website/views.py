from django.shortcuts import render
from django.core.mail import send_mail



# Create your views here.
def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method=='POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		
		send_mail(

			message_name,# subject
			message,# message
			message_email,# from email
			['sahan@gmail.com'],# To Email


			)



		return render(request, 'contact.html', {'message_name': message_name})
	
	else:
		return render(request, 'contact.html', {})



def about(request):
	return render(request, 'about.html', {})

def price(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {}) 

def appointment(request):
	if request.method=='POST':

		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']


		return render(request, 'appointment.html', {

				'your_name': your_name,
				'your_phone': your_phone,
				'your_email': your_email,
				'your_address': your_address,
				'your_schedule': your_schedule,
				'your_date': your_date,
				'your_message': your_message

				})


	else:
		return render(request, 'home.html', {})
