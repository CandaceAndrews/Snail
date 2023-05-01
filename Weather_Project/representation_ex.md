## Serializer Representation

```python
class CapturedSpecialAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    special_animal = SpecialAnimalSerializer()
    # image = serializers.SerializerMethodField()

    class Meta:
        model = CapturedSpecialAnimal
        fields = (
            'id',
            'owner',
            'special_animal',
            # 'image'

        )

    # def get_image(self, obj):
    #     return obj.special_animal.image.url if obj.special_animal.image else None

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['animal_name'] = representation['special_animal']['animal']['name']
    #     representation['variation_type'] = representation['special_animal']['animal']['variation_type']
    #     del representation['special_animal']
    #     return representation
```