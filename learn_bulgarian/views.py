import timedelta
from django.shortcuts import render, redirect
from .models import Word, Lesson
from django.contrib.auth.decorators import login_required
from .models import FlashCard
from datetime import date

def home(request):
    return render(request, 'learn_bulgarian/home.html')

def dictionary(request):
    words = Word.objects.all()
    query = request.GET.get('q')
    if query:
        words = words.filter(bulgarian__icontains=query) | words.filter(translation__icontains=query)
    return render(request, 'learn_bulgarian/dictionary.html', {'words': words})

def lessons_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'learn_bulgarian/lessons.html', {'lessons': lessons})


@login_required
def flashcards(request):
    today = date.today()
    cards = FlashCard.objects.filter(
        user=request.user,
        next_review__lte=today
    ).order_by('next_review')[:5]

    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        quality = int(request.POST.get('quality'))
        card = FlashCard.objects.get(id=card_id)

        # Алгоритм SuperMemo 2
        if quality >= 3:
            if card.repetition == 0:
                card.next_review = today + timedelta(days=1)
            elif card.repetition == 1:
                card.next_review = today + timedelta(days=6)
            else:
                card.next_review = today + timedelta(days=round(card.ease_factor))
            card.ease_factor = max(1.3, card.ease_factor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        else:
            card.repetition = 0
            card.next_review = today + timedelta(days=1)

        card.repetition += 1
        card.save()
        return redirect('flashcards')

    return render(request, 'learn_bulgarian/flashcards.html', {'cards': cards})


    progress, created = UserProgress.objects.get_or_create(user=request.user)
    progress_percent = progress.get_progress()

    return render(request, 'learn_bulgarian/flashcards.html', {
        'cards': cards,
        'progress': progress_percent
    })