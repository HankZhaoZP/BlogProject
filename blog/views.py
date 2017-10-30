from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category,Tag
from comment.forms import CommentForm
from django.views.generic import ListView,DeleteView
from django.core.paginator import Paginator
from django.db.models import Q
import markdown
# Create your views here.

# def index(request):
#     post_list=Post.objects.all()
#     return render(request,'blog/index.html',context={'post_list':post_list})

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 1

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.increase_views()
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

# def archives(request,year,month):
#     post_list=Post.objects.filter(create_time__year=year,
#                                   create_time__month=month
#                                   ).order_by('-create_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

class Archives(IndexView):
    def get_queryset(self):
        year=self.kwargs.get('year')
        month=self.kwargs.get('month')
        return super(Archives,self).get_queryset().filter(
            create_time__year=year,create_time__month=month).order_by('-create_time')

# def categorys(request,pk):
#     category_name=get_object_or_404(Category,pk=pk)
#     post_list=Post.objects.filter(category=category_name).order_by('-create_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

class Categorys(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(Categorys,self).get_queryset().filter(category=cate).order_by('-create_time')

def search(request):
    q=request.GET.get('q')
    error_msg=''

    if not q:
        error_msg='请输入关键词'
        return render(request,'blog/index.html',context={'error_msg':error_msg})

    post_list=Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg,
                                               'post_list': post_list})