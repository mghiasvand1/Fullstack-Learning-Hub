import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionModelTests(TestCase):

    def testWasPublishedRecentlyWithFutureQuestion(self):
        # was_published_recently() returns False for questions whose pub_date
        # is in the future.
        time = timezone.now() + datetime.timedelta(days = 30)
        futureQuestion = Question(pubDate = time)
        self.assertIs(futureQuestion.wasPublishedRecently(), False)

    def testWasPublishedRecentlyWithOldQuestion(self):
        # was_published_recently() returns False for questions whose pub_date
        # is older than 1 day.
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        oldQuestion = Question(pubDate = time)
        self.assertIs(oldQuestion.wasPublishedRecently(), False)

    def testWasPublishedRecentlyWithRecentQuestion(self):
        # was_published_recently() returns True for questions whose pub_date
        # is within the last day.
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recentQuestion = Question(pubDate = time)
        self.assertIs(recentQuestion.wasPublishedRecently(), True)

def createQuestion(questionText, days):
    # Create a question with the given `question_text` and published the
    # given number of `days` offset to now (negative for questions published
    # in the past, positive for questions that have yet to be published).
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(questionText = questionText, pubDate = time)

class QuestionIndexViewTests(TestCase):

    def testNoQuestions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available .')
        self.assertQuerysetEqual(response.context['latestQuestionList'], [])

    def testPastQuestion(self):
        question = createQuestion(questionText = 'Past question .', days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latestQuestionList'], [question],)

    def testFutureQuestion(self):
        question = createQuestion(questionText = 'Future question .', days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available .')
        self.assertQuerysetEqual(response.context['latestQuestionList'], [])

    def testFutureQuestionAndPastQuestion(self):
        # Even if both past and future questions exist, only past questions
        # are displayed.
        question = createQuestion(questionText = 'Past question .', days = -30)
        createQuestion(questionText = 'Future question .', days = 30)
        self.assertContains(response, 'No polls are available .')
        self.assertQuerysetEqual(response.context['latestQuestionList'], [question],)

    def testTwoPastQuestions(self):
        question1 = createQuestion(questionText = 'Past question 1.', days = -30)
        question2 = createQuestion(questionText = 'Past question 2.', days = -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latestQuestionList'], [question2, question1],)

class QuestionDetailViewTests(TestCase):

    def testFutureQuestion(self):
        # The detail view of a question with a pub_date in the future
        # returns a 404 not found.
        futureQuestion = createQuestion(questionText = 'Future question .', days = 5)
        url = reverse('polls:detail', args = (futureQuestion.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def testPastQuestion(self):
        # The detail view of a question with a pub_date in the past
        # displays the question's text.
        pastQuestion = createQuestion(questionText = 'Past question .', days = -5)
        url = reverse('polls:detail', args = (pastQuestion.id,))
        response = self.client.get(url)
        self.assertContains(response, pastQuestion.questionText)