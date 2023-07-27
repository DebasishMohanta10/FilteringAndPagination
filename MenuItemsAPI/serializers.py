from rest_framework import serializers
from .models import MenuItem,Category
import bleach

class CategorySerializer(serializers.ModelSerializer):
    menuitems_count = serializers.SerializerMethodField(method_name='menuitems')
    class Meta:
        model = Category
        fields=['id','name','description',"menuitems_count"]
    
    def menuitems(self,obj):
        return len(obj.menuitems.all())

class MenuItemSerializer(serializers.ModelSerializer):
    inStock = serializers.IntegerField(source="inventory")
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ["id","name","price","inStock","category","category_id"]
    
    def validate(self,attrs):
        attrs['name'] = bleach.clean(attrs['name'])
        if attrs['price'] < 2:
            raise serializers.ValidationError("Price should be greater than or equal to $2.")
        if attrs['inventory'] < 0:
            raise serializers.ValidationError("Stock should be Greater than 0.")    
        return super().validate(attrs)


    
    

