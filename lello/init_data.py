from django.http import JsonResponse

from datetime import datetime, date, timedelta

from django.contrib.auth.models import User
from users.models import UserDetail, Team, Member
from boards.models import Board, List, Card
from calendars.models import Calendar, Event

def create_initial_data(request):

    admin = User(
        username = "admin",
        email = "admin@admin.com",
        is_superuser = True,
        is_staff = True
    )
    admin.set_password("admin")
    admin.save()
    adminDetail = UserDetail.objects.create(
        user = admin,
        gender = 'M'
    )

    willi = User(
        username = "willi",
        email = "willi@willi.com",
    )
    willi.set_password("admin")
    willi.save()
    williDetail = UserDetail.objects.create(
        user = willi,
        gender = 'M'
    )

    luca = User(
        username = "luca",
        email = "luca@luca.com",
    )
    luca.set_password("admin")
    luca.save()
    lucaDetail = UserDetail.objects.create(
        user = luca,
        gender = 'M'
    )

    teamAdmin = Team.objects.create(name="Admin Team")
    teamAdmin.members.add(admin)

    teamUVG = Team.objects.create(name="Team UVG")
    teamUVG.members.add(admin)
    teamUVG.members.add(willi)
    teamUVG.members.add(luca)

    board1 = Board.objects.create(
        name = "Board del Admin",
        owner = admin,
        is_private = True,
        team = teamAdmin,
    )

    calendar1 = Calendar.objects.create(
        board = board1,
    )

    board2 = Board.objects.create(
        name = "Board UVG",
        owner = admin,
        is_private = True,
        team = teamUVG,
    )

    calendar2 = Calendar.objects.create(
        board = board2,
    )

    list1B1 = List.objects.create(
        name = "Lista 1",
        hours_estimated = 0,
        hours_done = 0,
        board = board1,
    )

    list2B1 = List.objects.create(
        name = "Lista 2",
        hours_estimated = 0,
        hours_done = 0,
        board = board1,
    )

    list1B2 = List.objects.create(
        name = "Lista 1",
        hours_estimated = 0,
        hours_done = 0,
        board = board2,
    )

    card1 = Card.objects.create(
        title = "Card 1",
        number = 1,
        hours_estimated = 0,
        hours_done = 0,
        lista = list1B1,
    )

    event1 = Event.objects.create(
        calendar = calendar1,
        title = "Evento de Card 1",
        date = (date.today() - timedelta(days=1)),
    )

    card2 = Card.objects.create(
        title = "Card 2",
        number = 2,
        hours_estimated = 0,
        hours_done = 0,
        lista = list2B1,
    )

    event2 = Event.objects.create(
        calendar = calendar1,
        title = "Evento de Card 2",
        date = datetime.now(),
    )

    card3 = Card.objects.create(
        title = "Card 2",
        number = 1,
        hours_estimated = 0,
        hours_done = 0,
        lista = list1B2, 
    )

    event3 = Event.objects.create(
        calendar = calendar2,
        title = "Evento de Card 1 B2",
        date = datetime.now(),
    )

    data = {
        'status': 'Ok',
        'Data': 'Data imported',
    }

    return JsonResponse(data)
