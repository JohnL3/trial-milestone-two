import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_session import Session
from flask_socketio import SocketIO, send
import json
from data.helper import get_question, set_up_new_user, id_type, check_answer, get_leaderboard, add_user_online, update_user_online, remove_user_online

my_users = {}
leader_board = []
online = {}
all_users_scores = []


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mycrazyoldcodingsecret'
socketio = SocketIO(app)

SESSION_TYPE = 'filesystem'

app.config.from_object(__name__)
Session(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    username = ''
    
    if 'username' in session:
        username = session.get('username')
        
    if request.method == 'POST':
        username = request.form['username']
       
        if 'username' in session:
            if session.get('username') == username:
                return redirect(url_for('game'))
        else:
            session['username'] = username
            my_users[username] = set_up_new_user(username)
    
            return redirect(url_for('game'))
    
    return render_template('index.html',username=username)
    
    
@app.route('/leavegame', methods=['GET', 'POST'])
def leavegame():
    global leader_board
    leader_board = get_leaderboard(my_users, leader_board)
    socketio.emit('leaders', {'data': leader_board})
    return redirect(url_for('index'))
    
@app.route('/game', methods=['POST', 'GET'])
def game():
    global leader_board
    global online
    idType = id_type()
    if 'username' in session:
        if session.get('username') in my_users:
            user = session.get('username')
            del my_users[user]['username']
            my_users[user] = set_up_new_user(user)
            
            if not user in online:
                online = add_user_online(my_users, user, online)
            else:
                online = remove_user_online(user,online)
                online = add_user_online(my_users,user,online)
                
            leader_board = get_leaderboard(my_users, leader_board)
           
            print('online',online)
            
            socketio.emit('in_out_game', {'data': online})
            socketio.emit('leaders', {'data': leader_board})
            
            return render_template('game.html',username=user, type_id = idType, on_line = online, leader = leader_board)
        else:
             user = session.get('username')
             my_users[user] = set_up_new_user(user)
             
             if not user in online:
                online = add_user_online(my_users, user, online)
             else:
                online = remove_user_online(user,online)
                online = add_user_online(my_users,user,online)
             print('')
             print('ONLINE',online)
             leader_board = get_leaderboard(my_users, leader_board)
            
             socketio.emit('in_out_game', {'data': online})
             socketio.emit('leaders', {'data': leader_board})
             
             return render_template('game.html',username=user, type_id = idType, on_line = online, leader = leader_board)
            
    else:
        return redirect(url_for('index'))
    
    
@app.route('/questions', methods=['POST', 'GET'])
def questions():
    socketio.emit('leaders', {'data': leader_board})
    if 'username' in session:
        if session.get('username') not in my_users:
            user = session.get('username')
            my_users[user] = set_up_new_user(user)
        
        if request.method == 'POST':
            data = request.get_json()
            
            my_quest = get_question(data['quest_id'])
        
            my_users[session.get('username')]['answered'].append(data['quest_id'])
         
            return jsonify(my_quest)
        
@app.route('/answer', methods=['POST'])
def answer():
    global online
    if request.method == 'POST':
        data = request.get_json()
       
        user = session.get('username')
        
        result = check_answer(data['questionId'],data['answer'])
       
        if result[0]['result'] == 'correct':
            online = update_user_online(user, online)
            my_users[session.get('username')]['score'] = my_users[session.get('username')]['score']+1
            
        socketio.emit('in_out_game', {'data': online})
        score = my_users[user]['score']
        socketio.emit('my_score',{'score': score,'user':user})
        
        data = {'msg': result}
        return jsonify(data)
        
        
@socketio.on('message')
def handleMessage(msg):
    socketio.emit('message', {'data': msg}, broadcast=True)

 
@socketio.on('exitgame')
def exitgame(usr):
    global online
    user =''
    user = usr
    
    if user in online:
        online = remove_user_online(user, online)
        print('EXITED GAME',user)
        print('EXITED GAME',online)
        socketio.emit('in_out_game', {'data': online})
    
    

if __name__ == "__main__":
    socketio.run(app,host=os.getenv('IP'), port=int(os.getenv('PORT')))