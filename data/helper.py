from flask import session
from flask_session import Session
from data.questions_answers import my_q_a
import operator

def id_type():
    id_Type = []
    for key in my_q_a:
       id_Type.append([key, my_q_a[key]['type']])
       
    return id_Type

def get_question(id):
    q = {}
    q_a = my_q_a[id]
    for key in q_a:
        if key != 'answer' and key != 'type':
            q[key] = q_a[key]
            
    return q
    
def check_answer(id, answer):
    quest_answer = my_q_a[id]['answer']
    
    quest_answer = [item.lower() for item in quest_answer]
    ans = [item.lower() for item in answer]
    
    if len(ans) == len(quest_answer):
        if set(ans) == set(quest_answer):
            return [{'id':id,'result': 'correct'}]
        else:
            return [{'id': id,'result':'You answered wrong','answer': answer}]
    else:
        return [{'id': id,'result':'You answered wrong', 'answer': answer}]
    

'''
This function is used to set up details on each user
and add them to a dictionary of all users
So I can store which question he has answered
and which question he has got wrong.
'''
def set_up_new_user(name):
    update_my_users = {}
    update_my_users['username'] = name
    update_my_users['answered'] = []
    update_my_users['wrong'] = []
    update_my_users['score'] = 0
    return update_my_users

def get_leaderboard(all_users, leaderboard):
    '''Return top 1 to 3 highest scores from users along with username or empty list in no correct answers'''
    l = []
    if len(leaderboard) > 0:
        l = leaderboard
        for user,score in all_users.items():
            if score['score'] != 0:
                r =(user,score['score'])
                l.append(r)
        l = list(set(l))
        l.sort(key = operator.itemgetter(1), reverse = True)
        
    else:
        for user,score in all_users.items():
            if score['score'] != 0:
                r =(user,score['score'])
                l.append(r)
        
    l.sort(key = operator.itemgetter(1), reverse = True)
   
    return(l[:3])


def add_user_online(all_users,user, all_online):
        
    add_user = {}
    add_user['username'] = all_users[user]['username']
    add_user['score'] = all_users[user]['score']
    
    all_online[user] = add_user
    return all_online
    
def remove_user_online(user, all_online):
   del all_online[user]

   return all_online
  
def update_user_online(user, all_online):
    update = all_online[user]
    update['score'] = update['score']+1
    all_online[user] = update
    return all_online
        
    
    
    
    
    
    