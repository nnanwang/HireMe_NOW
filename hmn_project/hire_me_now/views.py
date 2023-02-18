from django.shortcuts import render
import openai

# Create Homepage
def home(request):
    # We want to render a webpage, request, template_name => page name, context => return
    if request.method == "POST":
        question = request.POST['question']
        return render(request=request, template_name='screen/home.html', context={"question":question})
    
    return render(request=request, template_name='screen/home.html', context={})
    
