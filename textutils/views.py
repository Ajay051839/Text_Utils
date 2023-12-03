# i have created this file--ajay
# for rendering templates it is important to add in settings.py DIR=['templates']

from django.http import HttpResponse
from django.shortcuts import render  # for rendering HTML file or template

def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcap = request.GET.get('fullcap', 'off')
    removenextline = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Initialize variables
    analysed = djtext
    temp = analysed
    char_count = len(temp)

    # Remove Punctuations
    if removepunc == "on":
        analysed = ''.join(char for char in analysed if char not in punctuations)

    # Convert to UPPERCASE
    if fullcap == "on":
        analysed = analysed.upper()

    # Remove New Line
    if removenextline == "on":
        analysed = analysed.replace('\n', '')

    # Remove Extra Space
    if spaceremover == "on":
        analysed = ' '.join(analysed.split())

    # Count Characters
    if charcount == "on":
        char_count = len(analysed)

    operations = []

    if removepunc == "on":
        operations.append('Remove Punctuations')

    if fullcap == "on":
        operations.append('Uppercase')

    if removenextline == "on":
        operations.append('Remove New Line')

    if spaceremover == "on":
        operations.append('Remove Extra Space')

    if charcount == "on":
        operations.append('Count Characters')

    params = {'purpose': ', '.join(operations),
              'analysed_text': analysed, 'count': char_count}
    return render(request, 'analyse.html', params)

def ex1(request):
    s = '''<h1>Navigate from here</h1><br/>
    <a href="www.youtube.com">Go to YouTube</a><br/>
    <a href="www.codewithharry.com">Django by Harry bhai</a><br/>
    <a href="www.rediffmail.com">Go to Rediff</a><br/>
    <a href="www.google.com">Google anything!</a><br/>'''
    return HttpResponse(s)

