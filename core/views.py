import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from core.models import PalindromeGame
from core.utils import isPalindrome, updateString

# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def index(request):
    return Response({})

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def gameList(request):
    games = PalindromeGame.objects.all()
    game_list = []
    for game in games:
        game_list.append({"game-ID":game.id, "value_string": game.value})
    data = {
         "game-list" : game_list   
    }
    return Response(data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createGame(request):
    game = PalindromeGame.objects.create()
    data = {
         "game-ID" : game.id   
    }
    return Response(data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getBoard(request):
    game_id = request.data.get('game-ID', None)
    if game_id:
        try:
            game = PalindromeGame.objects.get(id=game_id)
        except Exception as ex:
            game = None
            print(str(ex))
            return Response({
                "error":"Something went wrong please check game-ID"
            })
        
        data = {
            "value_string" : game.value   
        }
        return Response(data)
    else:
        return Response({ "error":"game-ID is required"})

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def updateBoard(request):
    game_id = request.data.get('game-ID', None)
    add_character = request.data.get('add_character', None)
    if game_id:
        if add_character and len(add_character) == 1:
            pattern = re.compile("[A-Za-z]+")
            if not pattern.fullmatch(add_character):
                return Response({
                    "error":"please check string it should be one character between a - z"
                })
        else:
            return Response({
                    "error":"please check string it should be one character between a - z"
                })
        try:
            game = PalindromeGame.objects.get(id=game_id)
            game.value = updateString(game.value, add_character)
            game.save()
            if len(game.value) == 6:
                if isPalindrome(game.value):
                    data = {
                        "value_string" : game.value,
                        "is_palindrome" : True,
                        "message" : "string is palindrome"  
                    }
                    return Response(data)
                else:
                    data = {
                            "value_string" : game.value,
                            "is_palindrome" : False,
                            "message" : "string is not palindrome"  
                    }
                    return Response(data)
            else:
                data = {
                        "value_string" : game.value,
                        "message" : "play more"  
                }
                return Response(data)
        except Exception as ex:
            game = None
            print(str(ex))
            return Response({
                "error":"Something went wrong please check game-ID"
            })
    else:
        return Response({ "error":"game-ID is required"})