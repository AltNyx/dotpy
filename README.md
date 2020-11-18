# whatsapp.py

Send timed whatsapp messages.

## Usage

`Note: You need to setup whatsapp web to use these.`

## Install dependencies

`pip install -r requirements.txt`

### Send quick messsge

```python
phone_no = 'phone_number'
message = 'happy birthday!'

Whatsapp.send_quick_message(phone_no, message)
```

### Send scheduled messsge

```python
phone_no = 'phone_number'
message = 'happy birthday!'


#This sends the message to the specified phone number at 10:30Am
Whatsapp.send_scheduled_message(phone_no, 10, 30, message)

# Hour should be in range [0, 23]
# Minutes should be in range [0, 59]
```
