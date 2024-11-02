from django.http import HttpResponse
from django.shortcuts import render
import string
from textblob import TextBlob

def index(request):
    return render(request, 'index.html')

def analyze(request):
    punctuations = string.punctuation
    orgText = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    nocaps = request.GET.get('nocaps', 'off')
    newlinerem = request.GET.get('newlinerem', 'off')
    newspacerem = request.GET.get('newspacerem', 'off')
    charcount = request.GET.get('charcount', 'off')
    wordcount = request.GET.get('wordcount', 'off')
    sentiment = request.GET.get('sentiment', 'off')

    AnalyzedText = orgText
    purpose_list = []

    # Remove punctuation
    if removepunc == 'on':
        AnalyzedText = ''.join([char for char in AnalyzedText if char not in punctuations])
        purpose_list.append('Removed Punctuations')

    # Convert to uppercase
    if fullcaps == 'on':
        AnalyzedText = AnalyzedText.upper()
        purpose_list.append('Converted to UpperCase')

    # Convert to lowercase
    if nocaps == 'on':
        AnalyzedText = AnalyzedText.lower()
        purpose_list.append('Converted to LowerCase')

    # Remove newlines
    if newlinerem == 'on':
        AnalyzedText = AnalyzedText.replace('\n', '').replace('\r', '')
        purpose_list.append('New lines removed')

    # Remove extra spaces
    if newspacerem == 'on':
        AnalyzedText = AnalyzedText.replace(' ', '')
        purpose_list.append('Extra spaces removed')

    # Character count (both with and without spaces)
    if charcount == 'on':
        count_withSpace = len(orgText)
        count_withNoSpace = len(orgText.replace(' ', ''))
        purpose_list.append(f'Total characters with spaces: {count_withSpace}')
        purpose_list.append(f'Total characters without spaces: {count_withNoSpace}')

    if wordcount == 'on':
        Totalwords = len(orgText.split())
        purpose_list.append(f'Total words are : {Totalwords}')


    if sentiment == 'on':
        blob = TextBlob(orgText)
        sentiment = blob.sentiment.polarity
        purpose_list.append(f'Sentiment of text is : {sentiment}')

    

    
    # If no operation was selected
    if not purpose_list:
        purpose_list.append("No operations selected")

    result = {'purpose': purpose_list, 'result': AnalyzedText}  # Pass the list, not a string

    return render(request, 'analyze.html', result)

