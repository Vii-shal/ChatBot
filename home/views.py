from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"


# Create your views here.
def chat(request):                                    #chat view
    # return HttpResponse("This Work")+
    return render(request, "index.html")

def about(request):                                    #chat view
    # return HttpResponse("This Work")
    return render(request, "about.html")

def chatAPI(request):                                 #API , returns json response       
    if request.method == "POST":
        prompt = request.POST["prompt"] 
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response)
        return JsonResponse(response)
    return HttpResponse("Bad Request")

