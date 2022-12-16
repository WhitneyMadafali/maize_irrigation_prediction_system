from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
import numpy as np
import pickle
from . import db
from .models import Input
#from .models import Post
#from .import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)

#load the trained model
knn = pickle.load(open('model/knn.pkl', 'rb'))

@views.route("/")
@views.route("/index")
@login_required
def index():
    
    return render_template("index.html", user=current_user)

#Redirect to predict page with the output
@views.route("/index/predict", methods=['POST'])
@login_required
def predict():
    int_data = [int(x) for x in request.form.values()]
    data= [np.array(int_data)]
    prediction = knn.predict(data)
    output = round(prediction[0], 2)
    #return redirect(url_for('views.index'), prediction_text='Maize irrigation prediction is {}'.format(prediction))
    return render_template("index.html", user=current_user, prediction_text='Maize irrigation prediction is {}'.format(output))

#@views.route("/")
#@views.route("/prediction_irrigation")
#@login_required
#def predict_irrigation():
 #   return render_template("prediction.html", user=current_user)



