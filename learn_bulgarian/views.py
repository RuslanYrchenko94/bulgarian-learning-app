from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Word, Lesson
from .forms import DictionarySearchForm


class DictionaryView(ListView):
    """
    View for displaying and searching words in dictionary.
    Supports pagination and search functionality.
    """
    model = Word
    template_name = 'dictionary.html'
    context_object_name = 'words'
    paginate_by = 20  # Number of words per page

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            return queryset.filter(
                models.Q(bulgarian__icontains=search_query) |
                models.Q(translation__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = DictionarySearchForm(self.request.GET or None)
        return context


class LessonListView(ListView):
    """View for displaying list of all available lessons"""
    model = Lesson
    template_name = 'lessons_list.html'
    context_object_name = 'lessons'
    ordering = ['level']


class LessonDetailView(DetailView):
    """View for displaying single lesson details"""
    model = Lesson
    template_name = 'lesson_detail.html'
    context_object_name = 'lesson'


def home(request):
    """Home page view with basic statistics and quick actions"""
    total_words = Word.objects.count()
    total_lessons = Lesson.objects.count()

    context = {
        'total_words': total_words,
        'total_lessons': total_lessons,
    }
    return render(request, 'home.html', context)