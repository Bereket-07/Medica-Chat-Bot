import os
from flask import Flask,request,jsonify,render_template
from dotenv import load_dotenv
from medicalai import main_ai_chat_bot


# Load environment variables
load_dotenv()
# initialize flask app
app = Flask(__name__)


# set a secret key for session management
app.secret_key = os.getenv("FLASK_SECRET_KEY","default_secret_key")


# database configuration



@app.route("/medical",methods=['GET'])
def homepage():
    return render_template('chat.html')


@app.route("/medicalchatbot", methods=["GET" , "POST"])
def chatwithMediaclassitant():
    msg = request.json.get("message")
    response  = main_ai_chat_bot(msg)
    return jsonify({"reply":response})



if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)