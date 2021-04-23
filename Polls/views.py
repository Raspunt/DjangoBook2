
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.models import User
from Polls.TelegaFiles.telegaAlert import TelegaBot
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic.edit import CreateView, UpdateView

from users.models import UserProfile
from . models import *
from . forms import *








def MainPage(request):
    genreId = request.GET.get('genreId')
    sq = request.GET.get('sq')
    pageF = request.GET.get('page')



    books = Book.objects.all()

    #  начало поиска и фильтрации

    if genreId != '0' and genreId != None :
        books = Book.objects.filter(genreTree = genreId)

    else :
        books = Book.objects.all()

    if sq != '' and sq != None :
        books = Book.objects.filter(title__contains = sq)


    # Конец

    bookPagenator = Paginator(books,6)
    page = bookPagenator.get_page(pageF)

    numb  = []
    for i in  range(bookPagenator.num_pages) :
        numb.append(i + 1)


    data = {
        'numb':numb ,
        'authors':Author.objects.all(),
        'genres':Genre.objects.all(),
        'books':books,
        'page':page

    }
    return render(request,"Polls/index.html",data)



def BookDetail(request,BookSlug):

    commentText = request.POST.get('commentText')
    if not request.user.is_authenticated:
        return redirect('/login')    
    else:
        Username = User.objects.get(username=request.user)


    try :
    
        userPr = UserProfile.objects.get(name=Username)  
              
    except ObjectDoesNotExist as e :

        print("Нету профиля " + str(e))
        userPr = UserProfile.objects.create(name = request.user)

    


    book = Book.objects.get(slug = BookSlug)
    if request.method == 'POST':
        if  not request.user.is_authenticated:   #  if user not authenticated
            return redirect('/login')
        else :
            

            


            if Username != None and commentText != None :
                newComment = Comments(name = userPr, text = commentText , user_id=Username)
                newComment.save()
                book.comments.add(newComment)
                models.Comments.name




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
        'userPr':userPr,
        'alreadyLiked':alreadyLiked,
        'book':book,
        'CheckStars':lis,
        'UnCheckStars':unCheckStar,

    })





def LikeButton(request,BookSlug):

    book = Book.objects.get(slug = BookSlug)
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







def AuthorDetail(request,AuthorSlug):
    author = Author.objects.get(slug = AuthorSlug)
    books = Book.objects.filter(Author = author)

    return render(request,"Polls/AuthorDetail.html",
    {
        'author':author,
        'books':books
    })



def CrudActions(request):
    
    books = Book.objects.all()


    

    if request.user.is_superuser == False:
        return redirect('/')




    return render(request ,"Polls/CrudActions/CrudActions.html",
    {
        "books":books,
    })


#  Book Crud

class CreateBookView(CreateView):
    model = Book
    form_class = CrudFrom
    template_name = "Polls/CrudActions/CreateBook.html"
    success_url = '/CrudActions'
    

class UpdateBook(UpdateView):

    model = Book
    fields = '__all__'
    template_name = "Polls/CrudActions/EditBook.html"
    success_url = '/CrudActions'



def DeleteBook(request,slugBook):

    if request.user.is_superuser == False:
        return redirect('/')


    book = Book.objects.get(slug = slugBook)
    book.delete()

    return redirect('/CrudActions')



#  Author Crud


class CreateAuthorView(CreateView):
    model = Author
    fields = '__all__'
    template_name = "Polls/CrudActions/CreateAuthor.html"
    success_url = '/CrudActions'


class UpdateAuthorView(CreateView):
    model = Author
    fields = '__all__'
    template_name = "Polls/CrudActions/UpdateAuthor.html"
    success_url = '/CrudActions'

def DeleteAuthor(request,slugAuthor):

    if request.user.is_superuser == False:
        return redirect('/')

    author = Author.objects.get(slug = slugAuthor)
    author.delete()

    return redirect('/CrudActions')

