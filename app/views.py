from django.shortcuts import render
from django.http import HttpResponse

class CreateCollectionView(APIView):
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        return HttpResponse(serializer.errors, status=400)

class TopPostsView(APIView):
    def get(self, request, tenant_id):
        posts = EngagementPost.objects.filter(tenant_id=tenant_id).order_by('-created_at')[:5]
        serializer = EngagementPostSerializer(posts, many=True)
        return HttpResponse(serializer.data)

class TopProductsView(APIView):
    def get(self, request, tenant_id):
        products = EngagementPostProduct.objects.filter(engagement_post__tenant_id=tenant_id).order_by('-created_at')[:5]
        serializer = EngagementPostProductSerializer(products, many=True)
        return HttpResponse(serializer.data)

class EngagementPostCollectionView(APIView):
    def post(self, request):
        serializer = EngagementPostCollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        return HttpResponse(serializer.errors, status=400)

class GetEngagementPostCollectionView(APIView):
    def get(self, request, collection_id):
        collection = Collection.objects.get(id=collection_id)
        posts = EngagementPostCollection.objects.filter(collection=collection)
        serializer = EngagementPostCollectionSerializer(posts, many=True)
        return HttpResponse(serializer.data)




