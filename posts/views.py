

# Create your views here.
from django.views.generic import ListView,TemplateView
from .models import Post

class post_view(ListView):
    model=Post
    template_name="messages.html"
    context_object_name="all_posts"

class home_view(TemplateView):
    template_name="home.html"