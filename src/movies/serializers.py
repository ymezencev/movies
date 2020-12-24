from rest_framework import serializers
from movies.models import Movie, Review, Rating, Actor


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментрариев, только parents"""
    def to_representation(self, instance):
        instance = instance.filter(parent=None)
        return super().to_representation(instance)


class RecursiveSerializer(serializers.Serializer):
    """Рекурсиынй вывод children элементов"""
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance,
                                                  context=self.context)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ('name', 'text', 'children')


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = '__all__'


class ActorsListSerializer(serializers.ModelSerializer):
    """Вывод списка актёров"""

    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class ActorsDetailSerializer(serializers.ModelSerializer):
    """Вывод информации об актёре"""

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'tagline', 'category', 'rating_user',
                  'middle_star')


class MovieDetailSerializer(serializers.ModelSerializer):
    """Данные о фильме"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = ActorsDetailSerializer(read_only=True, many=True)
    actors = ActorsDetailSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True,
                                          many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ('draft', )


class SetMovieRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга фильма"""

    class Meta:
        model = Rating
        fields = ('star', 'movie')

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star', None)},

        )
        return rating
