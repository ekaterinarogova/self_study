from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Section, Materials, Tests


class MaterialsSerializers(serializers.ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Materials
        fields = '__all__'


class SectionDetailViewSerializers(serializers.ModelSerializer):
    materials = MaterialsSerializers(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__'


class SectionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = "__all__"


class TestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = '__all__'


class TestsForUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = ('question', 'possible_answers')
