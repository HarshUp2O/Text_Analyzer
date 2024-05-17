#I created this file to write business logic

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render
from django.http import HttpResponse
    
def analyze(request):
    djtext = request.POST.get('text', 'default') #Get the text
    
    #Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #checkbox logics
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
                
        analysis = {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        analysis = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed += char
        analysis = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        analysis = {'purpose': 'Extra Spaces Remover', 'analyzed_text': analyzed}
        djtext=analyzed

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any option to see your analyzed text")

    return render(request, 'analyze.html', analysis)