from rest_framework import serializers

from applications.category.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        rap = super().to_representation(instance)
        if not instance.parent:
            rap.pop('parent')
        return rap
