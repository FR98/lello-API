from django.http import JsonResponse

from django.contrib.auth.models import User
from users.models import UserDetail, Team, Member
from boards.models import Board, List, Card

def create_initial_data(request):

    admin = User.objects.create(
        username = "admin",
        email = "admin@admin.com",
        is_superuser = True,
        is_staff = True
    )
    admin.set_password("admin")

    adminDetail = UserDetail.objects.create(
        user = admin,
        gender = 'M'
    )

    teamAdmin = Team.objects.create(name="Admin Team")
    teamAdmin.members.add(admin)

    board1 = Board.objects.create(
        name = "Board 1",
        owner = admin,
        is_private = True,
        team = teamAdmin
    )

    list1 = List.objects.create(
        name = "Lista 1",
        hours_estimated = 0,
        hours_done = 0
    )

    card1 = Card.objects.create(
        title = "Card 1",
        number = 1,
        hours_estimated = 0,
        hours_done = 0
    )

    data = {
        'status': 'Ok',
        'Data': 'Data imported',
    }

    return JsonResponse(data)
