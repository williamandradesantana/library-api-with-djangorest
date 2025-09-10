from rest_framework import serializers, validators

from .models import Author, NATIONALITIES


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "date_of_birth", "nationality"]

    id = serializers.IntegerField(read_only=True)

    def validate_name(self, value):
        if len(value) > 100 or len(value) <= 0:
            raise serializers.ValidationError(
                "The field name must be between 1 and 100 chars"
            )
        return value

    def validate_nationality(self, value):
        valid_nationalities = [n[0] for n in NATIONALITIES]

        if value not in valid_nationalities:
            raise serializers.ValidationError(
                f"Nationality must be on of: {', '.join(valid_nationalities)}"
            )
        return value
