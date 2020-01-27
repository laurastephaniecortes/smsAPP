from twilio.rest import Client
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def test():
    r = requests.get("http://easy-mtapi.herokuapp.com/by-id")

    # Your Account SID from twilio.com/console
    account_sid = "AC4e6ffa07363705b56bca2f0002b5a79a"
    # Your Auth Token from twilio.com/console
    auth_token  = "8c3adf12edd1f1c0ba4fa7c79c027599"

    client = Client(account_sid, auth_token)

    if r.status_code is 200:
        message = client.messages.create(
            to="+16316037142", 
            from_="+16063930977",
            body="Easy MTAPI is running!")
        #return "Everything is Fine!"
        return render_template("home.html")
    else:
        message = client.messages.create(
            to="+16316037142", 
            from_="+16063930977",
            body="There was a Problem Reaching Easy MTAPI")
        #return "Something Went Wrong!"
        return render_template("about.html")

    

if __name__ == "__main__":
    app.run()

