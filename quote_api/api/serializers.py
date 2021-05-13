from rest_framework import serializers

from quote_api.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    """Serialzes Quote Model"""

    class Meta:
        model = Quote
        fields = '__all__'
