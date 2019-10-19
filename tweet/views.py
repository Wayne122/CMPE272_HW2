from django.shortcuts import render
from decouple import config
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.
import twitter


def get_api():
    api = twitter.Api(consumer_key=config('consumer_key'), consumer_secret=config('consumer_secret'), access_token_key=config('access_token_key'), access_token_secret=config('access_token_secret'))
    return api


def home(request):
    tweets = get_api().GetUserTimeline()
    return render(request, 'tweet/home.html', {'tweets': tweets})


class tweetForm(forms.Form):
    content = forms.CharField()


def create_tweet(request):
    form = tweetForm()
    if request.method == 'POST':
        form = tweetForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data
            get_api().PostUpdate(new_status.get('content'))
            return HttpResponseRedirect('/')
    return render(request, 'tweet/create_tweet.html', {'form': form})


def delete_tweet(request, id):
    get_api().DestroyStatus(id)
    return HttpResponseRedirect('/')
