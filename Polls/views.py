from django.shortcuts import render, redirect
from .  import models 

def MainPage(request):
    genreId = request.GET.get('genreId')
    sq = request.GET.get('sq')

    books = models.Book.objects.all()

    if genreId != '0' and genreId != None :
        books = models.Book.objects.filter(genreTree = genreId)
    else :
        books = models.Book.objects.all()

    if sq != '' and sq != None :
        books = models.Book.objects.filter(title__contains = sq)

    data = {
        'authors':models.Author.objects.all(),
        'genres':models.Genre.objects.all(),
        'books':books

    }
    return render(request,"Polls/index.html",data)



def BookDetail(request,BookSlug):

    book = models.Book.objects.get(slug = BookSlug)


    if request.method == 'POST':
        print(request.user)
        if  not request.user.is_authenticated:
            print(request.user.is_authenticated)
            return redirect('/login')
        else :
            Username = request.user
            commentText = request.POST.get('commentText')

            newComment = models.Comments(name = Username, text = commentText)
            newComment.save()
            book.comments.add(newComment)
            
            return redirect(f'/Book/{BookSlug}')

            
            


    
    return render(request,"Polls/BookDetail.html",
    {
        'book':book
    })




