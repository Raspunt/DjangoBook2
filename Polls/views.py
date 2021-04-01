
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .  import models 
from . forms import * 


def MainPage(request):
    genreId = request.GET.get('genreId')
    sq = request.GET.get('sq')
    pageF = request.GET.get('page')

    books = models.Book.objects.all()

    bookPagenator = Paginator(books,6)
    page = bookPagenator.get_page(pageF)

    if genreId != '0' and genreId != None :
        books = models.Book.objects.filter(genreTree = genreId)
    
    else :
        books = models.Book.objects.all()

    if sq != '' and sq != None :
        books = models.Book.objects.filter(title__contains = sq)
    
    numb  = []
    for i in  range(bookPagenator.num_pages) :
        numb.append(i + 1)

    

    data = {
        'numb':numb ,
        'authors':models.Author.objects.all(),
        'genres':models.Genre.objects.all(),
        'books':books,
        'page':page

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

    lis = []

    for i in range(book.rating.stars):
        lis.append(i)

    print( 5 - len(lis))

    unCheckStar = []

    for i in range( 5 - len(lis)):
        unCheckStar.append(i)




    
    return render(request,"Polls/BookDetail.html",
    {
        'book':book,
        'CheckStars':lis,
        'UnCheckStars':unCheckStar,
        'CommentText':SummerNoteForComment
    })




def AuthorsAll(request):
    authors = models.Author.objects.all()
    return render(request,"Polls/AllAuthors.html",
    {
        'authors':authors 
    })


def AuthorDetail(request,AuthorSlug):
    author = models.Author.objects.get(slug = AuthorSlug)
    books = models.Book.objects.filter(Author = author)

    return render(request,"Polls/AuthorDetail.html",
    {
        'author':author,
        'books':books
    })





