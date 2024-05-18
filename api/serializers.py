from rest_framework import serializers
from application import models
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer): # will serialize Profile model objects to json object
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer): # will convert Review model objects to json object
    class Meta:
        model = models.Review
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer): # will convert Tag Model objects to json object
    class Meta:
        model = models.Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer): # will serialize the Project model objects to json object
    owner = ProfileSerializer(many=False) # owner object of ProjectSerializer will get serialized owner object
    tags = TagSerializer(many=True) # tags object of ProjectSerializer will get serialized tags objects
    reviews = serializers.SerializerMethodField() # to create a method for reviews that will give serialized object
    class Meta:
        model = models.Project
        fields = '__all__'

    def get_reviews(self, obj): # method to serialize reviews object
        reviews = obj.review_set.all() # query all the reviews objects
        serializer = ReviewSerializer(reviews, many=True) # serialize the review objects to json objects
        return serializer.data # return the serialized data