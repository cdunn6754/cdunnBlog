from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.shortcuts     import redirect

from blog.models import Blog, BlogUser
from blog.forms  import UserForm, BlogUserForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'blog/blog_index.html'

class AboutMeView(TemplateView):
    template_name = 'blog/about_me.html'

class TestBlogView(TemplateView):
    template_name = 'blog/test_blog.html'

def createUser(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        blog_user_form = BlogUserForm(request.POST)

        if user_form.is_valid() and blog_user_form.is_valid():
            user = user_form.save()
            # hash password
            user.set_password(user.password)
            user.save()

            blogUser = blog_user_form.save(commit=False)
            blogUser.user = user
            blogUser.save()
            return redirect("blog:index")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        blog_user_form = BlogUserForm()
    return render(
        request,
        "blog/bloguser_create_form.html",
        {
            'user_form' : user_form,
            'blog_user_form': blog_user_form
        }
        )
