
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated # for authentication
from rest_framework import serializers, status, permissions
from rest_framework.views import APIView
from . models import Contact,Agent, Home, Image_files
from .serializers import Contact_serializer, Agent_serializer, Home_serializer,Home_details_serializer,Image_files_serializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView


from django.db.models import Q
class Search(APIView):
        

        def post(self, request, format=None):
            data = self.request.data
            str = data['str']
            q = (Q(description__icontains=str)) | (Q(title__icontains=str)) | (Q(slug__icontains=str))
            queryset = Home.objects.filter(is_published=True)
            queryset = queryset.filter(q)
            serializer = Home_serializer(queryset, many=True)
            return Response(serializer.data)


from ipware import get_client_ip
import json,urllib
class LocationAPI(APIView):
    def get(self,request,format=None):
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
            client_ip = "0.0.0.0"
        else:
            if is_routable:
                ip_type = 'public'
            else:
                ip_type = 'private'

        ip_address = "103.134.127.3"
        url = "https://api.ipfind.com/?ip="+ip_address
        respon = urllib.request.urlopen(url)
        data1 = json.loads(respon.read())
        data1 ['client_ip']=client_ip
        data1['ip_type']=ip_type
        return Response(data1)



class HomeListApiView(ListAPIView):
    # permission_classes = (permissions.AllowAny)
    serializer_class = Home_serializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    # lookup_field = 'slug'

class HomeDetailApiView(RetrieveAPIView):
    # permission_classes = (permissions.AllowAny)
    serializer_class = Home_details_serializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'

class ImageView(APIView):
    def get(self,request,pk,format=None):
        home = Home.objects.get(pk=pk)
       
        images = home.images.all() # images is related name of Image_files's home
        serializer = Image_files_serializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class ContactApiView(APIView):
    
    def get(self,request, format=None):
        contact = Contact.objects.all()
        serializer = Contact_serializer(contact, many=True)
        return Response(serializer.data)
    def post(self,request, format=None):
        serializer = Contact_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## with fbv
# class AgentListView(APIView):
#     def get(self, request, format=None):
#         agent = Agent.objects.all()
#         serializer = Agent_serializer(agent, many=True)
#         return Response(serializer.data)

# with cbv
class AgentListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = [permissions.IsAdminUser]
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    pagination_class= None


class AgentTopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = [permissions.IsAdminUser]
    queryset = Agent.objects.filter(top_seller = True)
    serializer_class = Agent_serializer
    pagination_class= None

class AgentDetailView(RetrieveAPIView): # like detail
    
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    pagination_class= None
                                                                                                                         

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated]) # allow for authenticated. another part on settings
# @permission_classes([AllowAny]) #allow for anyone
def index(request):
    if request.method == 'POST':
        name=request.data['name']
        age=request.data['age']
        print(name,age)
        return Response ({"name":name, "age":age})
    context = {
        'name':'Nayem Islam',
        'universuty': 'CU'
    }
    return Response(context)




def registationApi(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        password1 = request.data['password1']
        password2 = request.data['password2']
        first_name = request.data['first_name']
        last_name = request.data['last_name']

        if User.objects.filter(username=username).exists():
            return Response({"error": "An user already exists with this username!"})
        
        if password1 != password2:
            return Response({"error":"Both password didn't mathed!"})    
        user= User()
        user.username = username
        user.password = password1
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.is_active = True
        user.set_password(raw_password = password1)

        user.save()

        return Response({"success": "An user successfully creates an account"})




