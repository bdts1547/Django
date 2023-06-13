###Implement: 
Django, Ajax



##### Note
Create object Message with foreignKey is Room
```
new_message = Message.objects.create(username=username, text=message, room_id=Room(id=room_id))
new_message.save() // Save into database
```