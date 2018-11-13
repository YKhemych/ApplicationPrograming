from django.shortcuts import render, redirect, get_object_or_404
from mainApp.models import Events
from mainApp.models import Follow
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'mainApp\index.html')

@login_required
def allEvents(request):
    if 'date' in request.POST:
        a = request.POST['date'].split("-")
        currentDate = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
    else:
        currentDate = datetime.datetime.now()

    if 'title' in request.POST and 'description' in request.POST:
        if request.POST['title'] != '':
            user = request.user
            event = Events()
            event.title = request.POST['title']
            event.description = request.POST['description']
            event.date = currentDate
            event.save()
            follower = Follow()
            follower.event_id = event
            follower.user_id = user
            follower.save()


    followEvents = Follow.objects.all().filter(user_id = request.user)
    events = []
    for follow in followEvents:
        date = follow.event_id.date
        if(date.date() == currentDate.date()):
            events.append(follow.event_id)
        # print(events)

    return render(request, 'mainApp\events.html', { 'events': events, 'date':currentDate})

@login_required
def delete(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    event.delete()
    print(event)

    currentDate = datetime.datetime.now()
    followEvents = Follow.objects.all().filter(user_id = request.user)
    events = []
    for follow in followEvents:
        date = follow.event_id.date
        if(date.date() == currentDate.date()):
            events.append(follow.event_id)
    return render(request, 'mainApp\events.html', { 'events': events, 'date':currentDate})



@login_required
def detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    followers = Follow.objects.all().filter(event_id = event.id)
    date = event.date
    date = date.strftime('%Y-%m-%d')
    if 'title' in request.POST:
        if request.POST['title'] != event.title:
            print('title: ' + request.POST['title'])
            # print('title: ' + event.title)
            Events.objects.filter(id = event_id).update(title = request.POST['title'])
            event.title = request.POST['title']
    if 'description' in request.POST:
        if request.POST['description'] != event.description:
            Events.objects.filter(id = event_id).update(description = request.POST['description'])
            event.description = request.POST['description']
    if 'date' in request.POST:
        if request.POST['date'] != date:
            Events.objects.filter(id = event_id).update(date = request.POST['date'])
            event.date = request.POST['date']

    if 'username' in request.POST:
        try:
            user = User.objects.get(username = request.POST['username'])
            follower = Follow()
            follower.event_id = event
            follower.user_id = user
            follower.save()
            print(user);

        except User.DoesNotExist:
            if request.POST['username'] == '':
                return render(request, 'mainApp/event.html', {'event': event, 'followers': followers})
            else:
                return render(request, 'mainApp/event.html', {'event': event, 'followers': followers, 'error':'User does not exist'})




    return render(request, 'mainApp/event.html', {'event': event, 'followers': followers})

@login_required
def deleteFollower(request, event_id, follower_id):
    try:
        follower = Follow.objects.filter(user_id = follower_id).filter(event_id = event_id)
        follower.delete()
        event = get_object_or_404(Events, pk=event_id)
        followers = Follow.objects.all().filter(event_id = event.id)
    except User.DoesNotExist:
        event = get_object_or_404(Events, pk=event_id)
        followers = Follow.objects.all().filter(event_id = event.id)
        return render(request, 'mainApp/event.html', {'event': event, 'followers': followers, 'error':'User does not exist'})

    return render(request, 'mainApp/event.html', {'event': event, 'followers': followers})
