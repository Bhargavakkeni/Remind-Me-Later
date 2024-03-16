from django.shortcuts import render
from rest_framework.decorators import api_view
import logging
from rest_framework import status
from rest_framework.response import Response
from .serializers import ReminderDataSerializer
from .models import ReminderData

# Create your views here.
logging.basicConfig(level=logging.INFO, format="%(asctime)s-[%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s",
                    filename='apirequests.log')
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def reminder(request,*args, **kwargs):
    if(len(kwargs) >= 1):
        id = kwargs['id']
        try:
            reminder = ReminderData.objects.all().get(id=id)
        except Exception as e:
            logging.debug(f"Couldn't found record with id {id}")
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        id = 0
    print(id)
    if request.method == 'GET':
        logging.info('GET method is triggered returning all reminders')
        if(id!=0):
            serializer = ReminderDataSerializer(reminder)
        else:
            reminders = ReminderData.objects.all()
            serializer = ReminderDataSerializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        logging.info('Post method is triggered Posting the data')
        serializer = ReminderDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status= status.HTTP_200_OK)
        else:
            logging.debug("Couldn't post data")
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        logging.info('PUT method is triggerd updating the existing record')
        if(id==0):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ReminderDataSerializer(reminder, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status= status.HTTP_200_OK)
        else:
            logging.debug("Couldn't update the record")
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if(id==0):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        logging.info(f"DELETE method is triggered deleting the record with id {id}")
        reminder.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)