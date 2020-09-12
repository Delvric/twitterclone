from django.shortcuts import render, reverse, HttpResponseRedirect

from django.views.generic import TemplateView
from .forms import TweetForm
from .models import TweetModel
from notification.models import NotificationModel
from twitteruser.models import TwitterUser

import re


# Create your views here.


# @login_required

class CreateTweetView(TemplateView):

    def get(self, request):
        form = TweetForm()
        return render(request, 'tweet.html', {'form': form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            notifications: = TweetModel.objects.create(
                text=data.get('text', ),
                posted_by=request.user,
            )
            at_tag = re.findall(r'(?<=@)\w+', data.get('text', ))
            new_tweet = TweetModel.objects.create(
                text=data.get('text', ),
                posted_by=request.user,
            )
            if at_tag:
                for at in at_tag:
                    new_tweet = NotificationModel.objects.create(
                        tweet=new_tweet,
                        user=TwitterUser.objects.get(username=at),)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'tweet.html', {'form': form})


class TwitterView(TemplateView):

    def get(self, request, tweet_id):
        tweet = TweetModel.objects.get(id=tweet_id)
        return render(request, 'tweet_view.html', {'tweet': tweet})
