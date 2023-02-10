from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError
from flask import Flask, render_template, request


test= Flask(__name__)
print(test)



@test.route("/test",methods= ['POST','GET'])
def hello_world():
    
    if (request.method== 'POST'):
        body= request.form['body']
        send_push_message("testing sheet",body)
        
        
    return render_template('Notification_Test.html', name='BOH')






def send_push_message(token, message, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
    except PushServerError as exc:
        # Encountered some likely formatting/validation error.
        print(exc)
    except (ConnectionError, HTTPError) as exc:
        print(exc)

    try:
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
        response.validate_response()
    except DeviceNotRegisteredError as e:
        # Mark the push token as inactive
        print(e)
    except PushTicketError as exc:
        # Encountered some other per-notification error.
        print(exc)



