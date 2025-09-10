from rest_framework import serializers

from .models import Book, GENDERS


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)
    
    class Meta:
        model = Book
        fields = ["id", "isbn", "title", "publish_date", "gender", "price", "author", "author_name"]

        id = serializers.IntegerField(read_only=True)

        def validate(self, attrs):
            isbn = attrs.get("isbn")
            author = attrs.get("author")

            book_id = self.instance.id if self.instance else None

            if (
                Book.objects.filter(isbn=isbn, author=author)
                .exclude(id=book_id)
                .exists()
            ):
                raise serializers.ValidationError(
                    "This author already has a book with this ISBN."
                )
            return attrs

        def validate_title(self, value):
            if len(value) <= 0 or len(value) > 150:
                raise serializers.ValidationError(
                    "The field title must be between 1 and 150 chars"
                )
            return value

        def validate_isbn(self, value):
            if len(value) <= 0 or len(value) > 20:
                raise serializers.ValidationError(
                    "The field isbn must be between 1 and 20 chars"
                )
            return value

        def validate_gender(self, value):
            valid_genders = [gender[0] for gender in GENDERS]

            if value not in valid_genders:
                raise serializers.ValidationError(
                    f"Nationality must be on of: {', '.join(valid_genders)}"
                )
            return value

        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError("Price must be greater than zero!")
            return value

        def validate_author(self, value):
            if value is None:
                raise serializers.ValidationError("Author is required.")
            return value
