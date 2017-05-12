from rest_framework import serializers
from .models import Book
from modules.authors.serializers import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    #comentarios = CommentSerializer(read_only = True, many=True) #tiene que ser en nombre de la llave foranea en el modelo
    autor = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ("id", "nombre", "descripcion", "isbn","autor","fecha_pub","foto")