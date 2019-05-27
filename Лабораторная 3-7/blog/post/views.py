from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from . forms import UserReg
from .models import Post

def home(request):
	post = Post.objects.filter()
	return render(request, 'post/index.html', {"posts": post})

def articles(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post/articles.html', {"post": post})

def login(request):
	return render(request, 'post/login.html')

def registration(request):
	if request.method == "POST":
		form = UserReg(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username} успешно зарегистрирован!')
			return redirect('login')
	else:
		form = UserReg()
	return render(request, 'post/registration.html', {'form': form})

def edit(request):
	if not request.user.is_anonymous:
		if request.method == "POST":

			form = {
			'text': request.POST["text"],
			'title': request.POST["title"]
			}

			if form["text"] and form["title"]:
				title = form["title"]
				if Post.objects.filter(title=title).exists():
					form['errors'] = u"Запись с таким заголовком уже существует!"
					return render(request, 'post/edit.html', {'form': form})
				else:
					Post.objects.create(text=form["text"], title=form["title"], author=request.user)
					post = Post.objects.get(title=form['title'])
					return redirect('articles', pk=post.id)
			else:
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'post/edit.html', {'form': form})
		else:
			return render(request, 'post/edit.html', {})
	else:
		raise Http404

