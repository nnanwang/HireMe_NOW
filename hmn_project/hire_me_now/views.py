from django.shortcuts import render
import openai
from hire_me_now.secret.OpenaiAPIKey import get_key

# Create Homepage
def home(request):
    # We want to render a webpage, request, template_name => page name, context => return
    if request.method == "POST":
        question = request.POST['question']
        print(question)
        # Set API Key
        openai.api_key = get_key()
        # Create OpenAI Instance
        openai.Model.list()
        # Make a Completion
        response = openai.Completion.create(
            model="text-davinci-003", # free, no more than 8000 tokens
            prompt=question,
            temperature=0, # how arbitrary you want your model do.
            max_tokens=3000, # max length response
            frequency_penalty=0.0, # range [-2.0, 2.0], penalize new tokens based on their existing frequency in the text so far
            presence_penalty=0.0, # range [-2.0, 2.0], penalize new tokens based on whether they appear in the text so far
            logprobs=1, # top * possible result, limited up to 5
            logit_bias={}, # Modify the likelihood of specified tokens appearing in the completion. {"Token": presentage range [-100, 100]}
        )

        # Parse the response
        response = response["choices"][0]["text"].strip()
        
        return render(request=request, template_name='screen/home.html', context={"question":question, "response": response})
    
    return render(request=request, template_name='screen/home.html', context={})

def multiresponse(request):


    return
    
