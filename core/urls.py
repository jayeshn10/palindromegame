from django.urls import path

from core.views import index, createGame, getBoard, updateBoard, gameList


urlpatterns = [
    path('', index, name="home"),
    path('game-list/', gameList, name="game-list"),
    path("create-game/", createGame, name="create-game"),
    path("getBoard/", getBoard, name="get-board"),
    path("updateBoard/", updateBoard, name="update-board")
                   
]