
class FacebookRegistration(APIView):
    """
    Facebook user registration is done here
    """

    serializer_class = FbRegisterSerializer
    permission_classes = (AllowAny,)
    model = User

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request):

        serializer = self.serializer_class(data=request.data,)
        if serializer.is_valid():
            try:
                user = User.objects.get(facebook_id=request.data['facebook_id'])
            except:
                try:
                    user = User.objects.get(email=serializer.validated_data.get('contact_no'))
                    for k, v in serializer.validated_data.iteritems():
                        setattr(user,k,v)
                    user.save()
                except:
                    user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,
                        'image': user.image_url, 
                       'name' : user.name,
                       'email': user.email,
                       },
                        status=status.HTTP_201_CREATED)

        else:
            return Response({'error': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

