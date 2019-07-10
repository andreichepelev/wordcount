from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')
def contacts(request):
    return HttpResponse('@pirunpoika')
def about(request):
    return render(request, 'about.html')
def count(request):
    fulltext_on_count = request.GET['fulltext']
    wordlist = fulltext_on_count.split()

    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            #increment
            word_dict[word] += 1
        else:
            #add first
            word_dict[word] = 1

    sortedworddict = sorted(word_dict.items(), \
    key = operator.itemgetter(1), \
    reverse = True)

    return render(request, 'count.html', \
    {'fulltext_on_count':fulltext_on_count, \
    'wordcount':len(wordlist), \
    'sortedworddict':sortedworddict})
