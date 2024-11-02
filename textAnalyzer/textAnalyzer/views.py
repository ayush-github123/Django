from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def pricing(request):
    return render(request, 'pricing.html')

def analyze(request):
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    djtext = request.POST.get('text', 'default')
    checked = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    nocaps = request.POST.get('nocaps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    newspacerem = request.POST.get('newspacerem', 'off')
    charcount = request.POST.get('charcount', 'off')
    

    AnalyzedText = ''
    
    # Remove punctuation if checked
    if checked == 'on':
        for char in djtext:
            if char not in punctuations:
                AnalyzedText += char
        
        x = {'purpose': 'Removed Punctuations', 'result': AnalyzedText}
        return render(request, 'analyze.html', x)
    
    # Convert to uppercase if fullcaps is checked
    elif fullcaps == 'on':
        for char in djtext:
            if char not in punctuations:
                AnalyzedText += char.upper()

        x = {'purpose': 'Converted to Uppercase', 'result': AnalyzedText}
        return render(request, 'analyze.html', x)
    

    elif nocaps == 'on':
        for char in djtext:
            if char not in punctuations:
                AnalyzedText += char.lower()

        x = {'purpose': 'Converted to Lowercase', 'result': AnalyzedText}
        return render(request, 'analyze.html', x)
    

    elif newlinerem == 'on':
        for char in djtext:
            if char != '\n' and char!='\r':
                AnalyzedText += char

        x = {'purpose': 'Removed New Line', 'result': AnalyzedText}
        return render(request, 'analyze.html', x)
    

    elif newspacerem == 'on':
        for char in djtext:
            if char != ' ':
                AnalyzedText += char

        x = {'purpose': 'Removed Spaces', 'result': AnalyzedText}
        return render(request, 'analyze.html', x)
    

    elif charcount == 'on':
        count=0
        for char in djtext:
            if char != ' ':
                count+=1

        x = {'purpose': 'Total Character Counted', 'result': str(count) +'( Whitespaces not included)'}
        return render(request, 'analyze.html', x)

    # If no options are selected
    else:
        return HttpResponse("Text not analyzed...")
