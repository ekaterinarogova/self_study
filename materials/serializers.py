from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Section, Materials, Tests


class MaterialsSerializers(serializers.ModelSerializer):
    """Serializer for :model:`materials.Materials`"""
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Materials
        fields = '__all__'


class SectionDetailViewSerializers(serializers.ModelSerializer):
    """Serializer for :model:`materials.Section` for detail view"""
    materials = MaterialsSerializers(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__'


class SectionSerializers(serializers.ModelSerializer):
    """Serializer for :model:`materials.Section`"""
    class Meta:
        model = Section
        fields = "__all__"


class TestsSerializers(serializers.ModelSerializer):
    """Serializer for :model:`materials.Tests` for all operations"""
    materials = SlugRelatedField(slug_field='title', queryset=Materials.objects.all())

    class Meta:
        model = Tests
        fields = '__all__'


class TestsForUserSerializers(serializers.ModelSerializer):
    """Serializer for :model:`materials.Tests` for users, that are not staff"""
    class Meta:
        model = Tests
        fields = ('question', 'possible_answers')
