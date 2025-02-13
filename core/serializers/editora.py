from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora

class EditoraSerializer(ModelSerializer):
    def validate_email(self, email):
        return email.lower()
        
    class Meta:
        model = Editora
        fields = "__all__"