from .models import Category, Tour, News, Ticket, Tag, User, Comment, Rating, Booking, Payment
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/static/%s" % obj.image.name


    class Meta:
        model = Tour
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'created_date', 'updated_date', 'image']


class NewsSerializerDetail(NewsSerializer):
    liked = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):  # lấy hình them /static/ vao duong dan
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/static/%s" % obj.image.name
    def get_liked(self, news):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return news.like_set.filter(liked=True, user=request.user).exists()
    class Meta:
        model = NewsSerializer.Meta.model
        fields = NewsSerializer.Meta.fields + ['liked']


class TicketSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):  # lấy hình them /static/ vao duong dan
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/static/%s" % obj.image.name

    class Meta:
        model = Ticket
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='avatar')

    def get_avatar(self, obj):  # lấy hình them /static/ vao duong dan
        request = self.context.get('request')
        if obj.avatar:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.avatar.name)
            return "/static/%s" % obj.avatar.name

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user

    class Meta: #chỉ tạo không hiện mk
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'avatar', 'password']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'tour', 'news']
        # fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'user']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['adult_quantity', 'child_quantity', 'total_price']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'