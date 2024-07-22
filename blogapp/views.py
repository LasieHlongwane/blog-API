from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Post
from . serializers import PostSerializer

@api_view(['GET'])
def index(request):

    return Response({"success":"the setup was successful"})

@api_view(['GET'])
def GetAllPost(request):
    get_posts =Post.objects.all()
    seri = PostSerializer(get_posts, many=True)
    return Response(seri.data ) 

@api_view(['GET','POST'])
def CreatePost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The post was successfully created son"}, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@api_view({'DELETE'})
def DeletePost(request):
    post_id = request.data.get('post_id')
    try:
       post = Post.objects.get(id-post_id)
       post.delete()
       return Response({"success":"The post is deleted"},status=200)
    except:
       return Response({"error": "the post dont exist"}, status=404)
    
@api_view({'PUT'})
def UpdatePost(request):
    post_id = request.data.get('post_id')
    getnewtitle = request.data.get('new_title')
    getnewcontent = request.data.get('new_content')
    try:
        post = Post.objects.get(id-post_id)
         
        if getnewtitle:
            post.title = getnewtitle
        if getnewcontent:
            post.content = getnewcontent

        post.save()
        return Response({"success": "The post is successful"}, status=200)
    except Post.DoesNotExist:
        return Response({"Error": "The post dont exist"}, status=404)

