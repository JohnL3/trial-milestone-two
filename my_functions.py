from data.questions_answers import my_q_a
import operator

def set_up_new_user(user):
    my_user = {}
    my_user['username'] = user
    my_user['answered'] = []
    my_user['wrong'] = []
    my_user['score'] = 0
    
    return my_user
    
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
    
    
def get_leaderboard(all_users):
    '''Return top 1 to 3 highest scores from users along with username or empty list in no correct answers'''
    l = []
    for user,score in all_users.items():
        if score['score'] != 0:
            r =(user,score['score'])
            l.append(r)
        
    l.sort(key = operator.itemgetter(1), reverse = True)
   
    return(l[:3])
    
def get_users_scores(all_users):
    scores = []
    for key in all_users:
        scores.append((all_users[key]['username'],all_users[key]['score']))
        
    return scores