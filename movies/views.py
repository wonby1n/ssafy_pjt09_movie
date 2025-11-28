from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.http import JsonResponse

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request):
    # AJAX 요청으로 보낸 genre_id를 받음
    genre_id = request.GET.get('genre_id')
    
    # genre_id가 있으면 해당 장르 포함 영화 필터링, 없으면 전체 조회
    if genre_id:
        movies = Movie.objects.filter(genres__id=genre_id)
    else:
        movies = Movie.objects.all()
    
    # JSON으로 응답하기 위해 리스트 딕셔너리 형태로 변환
    movies_data = []
    for movie in movies:
        movies_data.append({
            'title': movie.title,
            'overview': movie.overview,
            'poster_path': movie.poster_path,
            'vote_average': movie.vote_average,
        })
        
    return JsonResponse({'movies': movies_data})


@require_safe
def recommended(request):
    pass
