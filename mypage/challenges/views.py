from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {"jan":"Jan","feb":"Feb","mar":"Mar"}

def monthlychallenge_num(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        return HttpResponseRedirect(redirect_month)
    except:
        return HttpResponseNotFound("num>months")

def monthlychallenge(request, month):
    try:
        challengetext = monthly_challenges[month]
        return HttpResponse(challengetext)
    except:
        return HttpResponseNotFound("Month Not Supported")

