#i have created this file - Ayush
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1>Hello, This is home page</h1>")
    bio = {'name':'Ayush','place':'Lucknow'}
    return render(request, 'index.html',bio)

def about(request):
    return HttpResponse("<h1>About Ayush</h1>")

def query_retrvl(request):
    return render(request, 'Query_Prmtr_retrievel.html')



def top5(request):
            # get the text
    djtext = request.GET.get('text','default')
    print(djtext)
            # analyze the text
    return HttpResponse('''
                        <h1>My top 5 websites : </h1>
                        <p>These are my top 5 most visited websites : </p>
                        <ol>
                            <li><a href = "https://www.youtube.com">Youtube</a>
                            <li><a href = "https://www.leetcode.com">Leetcode</a>
                            <li><a href = "https://www.Instagram.com">Instagram</a>
                            <li><a href = "https://www.chatgpt.com">ChatGPT</a>
                            <li><a href = "https://www.mail.google.com">Gmail</a>
                        </ol>

                        ''')

    
