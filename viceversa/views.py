from django.shortcuts import render

 
def home(request):
    return render(request, 'home.html')
    
   
def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    quantity = len(user_text.split())
    return render(request, 'reversed.html', {'usertext': user_text,'reversedtext': reversed_text, 'count': quantity} )
    