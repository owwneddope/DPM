import flask
from flask import render_template
import pickle
import sklearn
from sklearn.ensemble import GradientBoostingRegressor

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST','GET'])

@app.route('/index', methods = ['POST','GET'])
def main():

    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        #loaded_model = pickle.load(open('gradient_МПТ 6.4 580.pkl','rb'))
        try:
            loaded_model = pickle.load(open('regr_'+ flask.request.form['ser']
        + '_' + flask.request.form['sec'] + '.pkl','rb'))
            probeg_km = float(flask.request.form["probeg_km"])
            XX = float(flask.request.form["XX"])
            TP = float(flask.request.form["TP"])
            PP = float(flask.request.form["PP"])
            y_pred = loaded_model.predict([[probeg_km,XX,TP,PP]])
            return render_template('main.html', result = y_pred)
        except FileNotFoundError:
            return render_template('main.html', result = 'Введены некорректные значения серии или номера')
            
if __name__ == '__main__':
    app.run()