# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


def index(request):
    return render(request, 'fives/index.html')


def findapitch(request):
    return render(request, 'fives/findapitch.html')


def chat(request):
    return render(request, 'chat/chat.html')


class IndexView1(View):
    template_name = 'fives/dragon.html'

    def get(self, request):
        return render(request, self.template_name, context=None)

    def index(request):
        return render(request, 'fives/index.html')

    def myAccount(request):
        return render(request, 'fives/MyAccount.html')

    def newGame(request):
        return render(request, 'fives/NewGame.html')

    def existingGame(request):
        return render(request, 'fives/ExistingGame.html')

    #  def findPitch(request):
      #  return render(request, 'fives/findapitch.html')

