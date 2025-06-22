from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

# def index(request):
    # latestQuestionList = Question.objects.order_by('-pubDate')[:5]
    # # Means get the first five objects order by their pub date ( descending ) . ( and pub date without - means asscending . ) 
    # context = {
        # 'latestQuestionList' : latestQuestionList,
    # }
    # return render(request, 'polls/index.html', context)

# def detail(request, questionId):
    # question = get_object_or_404(Question, pk = questionId)
    # context = {
        # 'question' : question,
    # }
    # return render(request, 'polls/detail.html', context)

# def results(request, questionId):
    # question = get_object_or_404(Question, pk = questionId)
    # return render(request, 'polls/results.html', {'question' : question,})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'
    
    def get_queryset(self):
        # Return the last five published questions (not including those set to be
        # published in the future).
        return Question.objects.filter(pubDate__lte = timezone.now()).order_by('-pubDate')[:5]
        # '__lte =' means less or equal than and '__gte =' means greater or equal than 

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        # Excludes any questions that aren't published yet.
        return Question.objects.filter(pubDate__lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, questionId):
    # We need to avoid race conditions using F()
    question = get_object_or_404(Question, pk = questionId)
    try:
        selectedChoice = question.choiceSet.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {
            'question' : question,
            'errorMessage' : 'You did not select a choice .',
        }
        return render(request, 'polls/detail.html', context)
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
        
