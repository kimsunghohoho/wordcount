from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    full_text = request.GET['fulltext']

    word_list=full_text.split()
    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    
    return render(request, 'result.html', {'fulltext' : full_text, 'total' : len(word_list), 'dictionary': word_dic.items()})