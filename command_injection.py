from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

import subprocess
import shlex

app = Flask(__name__)

app.config['SECRET_KEY'] = '164359012aeccde26359d603d234d3c4'

class injectionForm(FlaskForm):
    command = StringField('Command')
    submit = SubmitField('Submit')

@app.route('/')
def home_page():
    return 'This is a demo application of command injection vulnerability'

'''
@app.route('/testing')
def home():
    return render_template('testing.html')
'''

@app.route('/vulnerable_function', methods=['GET', 'POST'])
def vulnerable_function():
    form = injectionForm()
    return render_template('command_injection_ui_vul.html', title = 'Vulnerable Function', form = form)

@app.route('/non_vulnerable_function', methods=['GET', 'POST'])
def non_vulnerable_function():
    form = injectionForm()
    return render_template('command_injection_ui.html', title = 'Vulnerable Function', form = form)

@app.route('/non_vul_results', methods=['GET', 'POST'])
def non_vul_results():
    if(request.method == 'POST'):
        command_result = request.form['command']
        command = 'cat {source}'.format(source=command_result)
        command_1 = shlex.split(command)
        re = subprocess.check_output(command_1, shell=False)
        re_array = re.decode('ascii').splitlines()
        return render_template('show_results.html', result = re_array)

@app.route('/vul_results', methods=['GET', 'POST'])
def vul_results():
    if(request.method == 'POST'):
        command_result = request.form['command']
        command = 'cat {source}'.format(source=command_result)
        re = subprocess.check_output(command, shell=True)
        re_array = re.decode('ascii').splitlines()
        return render_template('show_results.html', result = re_array)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
