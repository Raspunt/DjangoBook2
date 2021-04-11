
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.models import User
from Polls.TelegaFiles.telegaAlert import TelegaBot
import asyncio
import logging
logging.getLogger("asyncio").setLevel(logging.WARNING)

from .  import models 
from . forms import * 


# tel = TelegaBot()
# tel.start()



def MainPage(request):
    genreId = request.GET.get('genreId')
    sq = request.GET.get('sq')
    pageF = request.GET.get('page')

   

    books = models.Book.objects.all()

    #  начало поиска и фильтрации

    if genreId != '0' and genreId != None :
        books = models.Book.objects.filter(genreTree = genreId)

    else :
        books = models.Book.objects.all()

    if sq != '' and sq != None :
        books = models.Book.objects.filter(title__contains = sq)
    

    # Конец

    bookPagenator = Paginator(books,6)
    page = bookPagenator.get_page(pageF)

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
        if  not request.user.is_authenticated:   #  if user not authenticated
            return redirect('/login')
        else :
            Username = request.user
            commentText = request.POST.get('commentText')

            if Username != None and commentText != None :
                newComment = models.Comments(name = Username, text = commentText)
                newComment.save()
                book.comments.add(newComment)
     
    lis = []
    for i in range(book.Rewiew.stars):
        lis.append(i)

    unCheckStar = []
    for i in range( 5 - len(lis)):
        unCheckStar.append(i)

    if not request.user in book.like.all(): 
        alreadyLiked = "Лайк уже поставлен"
    else :
        alreadyLiked = ''



    return render(request,"Polls/BookDetail.html",
    {
        'alreadyLiked':alreadyLiked,
        'book':book,
        'CheckStars':lis,
        'UnCheckStars':unCheckStar,
        'CommentText':SummerNoteForComment
    })





def LikeButton(request,BookSlug):

    book = models.Book.objects.get(slug = BookSlug)
    alreadyLiked = "Нету нечего"
    is_liked = request.POST.get('like')

    
    print('пост сработал')
    print("проверка пользователей " + str(book.like.all()))

    if not request.user in book.like.all(): 
        if is_liked == '1':
            book.like.add(request.user)
            print('лайка нашлась')
        else :
            print('нет лайки ;(')
    else :
        alreadyLiked = "likeC"
        print("уже лайка есть")

    countLike = book.like.count()
    return JsonResponse({"data":alreadyLiked,"countLike":countLike})





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






