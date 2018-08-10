import unittest
from my_functions import set_up_new_user, get_question, check_answer, get_leaderboard, get_users_scores

class Test_setup_users(unittest.TestCase):
    
    def test_returns_a_dictionary(self):
        '''Test is to ensure we return a dictionary'''
        
        user = 'John_L3'
        users = set_up_new_user(user)
        self.assertTrue(type(users) is dict)
        
    def test_it_sets_username_to_user(self):
        ''' Test to ensure user passed to function is the value for key username'''
        
        user = 'John_L3'
        users = set_up_new_user(user)
        self.assertEqual(users['username'],'John_L3')
        
    def test_returns_dict_length_4(self):
        '''Test to check the size of dict returned is 4'''
        
        user = 'John_L3'
        new_user = set_up_new_user(user)
        self.assertEqual(len(new_user),4)
        
    def test_has_key_answered_and_wrong_score(self):
        '''Test to see it has key answered and wrong score'''
        
        user = 'John_L3'
        new_user = set_up_new_user(user)
        
        self.assertIn('answered',new_user)
        self.assertIn('wrong',new_user)
        self.assertIn('score', new_user)
        
    def test_key_answered_and_wrong_are_lists(self):
        '''Test to ensure key values answered and wrong are of type list'''
        
        user = 'John_L3'
        new_user = set_up_new_user(user)
        
        self.assertTrue(type(new_user['answered']) is list)
        self.assertTrue(type(new_user['wrong']) is list)
        
class Test_my_get_question(unittest.TestCase):
    
    def test_returns_a_dictionary(self):
        '''Test is to ensure we return a dictionary'''
        
        quest = get_question('0')
        
        self.assertTrue(type(quest) is dict)
        
    def test_keys_not_in_dict(self):
        '''Returned dict should not have keys answer and type'''
        
        quest = get_question('0')
            
        self.assertNotIn('answer',quest)
        self.assertNotIn('type',quest)
        
class Test_my_get_answer(unittest.TestCase):
    '''Tests to ensure my check_answer function works'''
    
    def test_id_passed_to_function(self):
        '''ensure id passed to function returns a list'''
        
        result = check_answer('0', ['Dictionary', 'List', 'Set', 'Tuple'])
        
        self.assertTrue(type(result) == list)
        
        
        
    def test_valid_return_for_correct_answer(self):
        '''Ensure a valid answer is not missed 
        if more than one part to answer, even if order or results is mixed'''
        
        result = check_answer('0', ['Tuple', 'List', 'Set', 'Dictionary'])
        
        self.assertEqual(result[0]['result'],'correct')
        
    def test_valid_return_for_incorrect_answer(self):
        '''Ensure a wrong answer if picked up'''
        
        result = check_answer('0', ['Tuple', 'Set', 'Dictionary']) 
        
        self.assertEqual(result[0]['result'],'You answered wrong')
        
        
    def test_valid_length_of_answer_but_wrong_answer(self):
        '''Ensure for multiple parts to answer if any are wrong it is picked up'''
        
        result = check_answer('0', ['Tuple', 'Set', 'Dictionary','array'])
        
        self.assertEqual(result[0]['result'],'You answered wrong')
    
    
    def test_for_wrong_answers_players_answers_are_returned(self):
        '''Wrong answers should return list containg players answer/s'''
        
        answer = ['Tuple', 'Set']
        result = check_answer('0', answer)
        
        
        self.assertEqual(answer, result[0]['answer'])
        
class Test_setup_leaderboard(unittest.TestCase):
    '''Tests for my leaderboard function'''
    
    def test_get_leaderboard_returns_list(self):
        '''Ensure get_leaderboard returns a list'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':2},
            'e':{'username':'e','ans':[],'wrong':[],'score':5},
            'a':{'username':'a','ans':[],'wrong':[],'score':9},
            'b ':{'username':'b','ans':[],'wrong':[],'score':6},
            'c':{'username':'c','ans':[],'wrong':[],'score':2},
            'd':{'username':'d','ans':[],'wrong':[],'score':7}
        }
        
        result = get_leaderboard(my_users)
        
        self.assertTrue(type(result) == list)
        
    def test_returns_list_length_greater_than_0(self):
        '''Should return a list of length of at least one if a user has played game and answered a question correctly'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':1},
        }
        
        result = get_leaderboard(my_users)
        
        self.assertEqual(1,len(result))
        
    def test_returns_list_length_0_if_no_one_answers_correctly(self):
        '''Should return an empty list if user/s played game and have answered no questions correctly'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':0},
        }
        
        result = get_leaderboard(my_users)
        
        self.assertEqual(0,len(result))
        
    
    def test_returns_list_length_3(self):
        '''Should return a list of length 3 if 3 or more players have answered questions correctly'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':2},
            'e':{'username':'e','ans':[],'wrong':[],'score':5},
            'a':{'username':'a','ans':[],'wrong':[],'score':9},
            'b ':{'username':'b','ans':[],'wrong':[],'score':6},
            'c':{'username':'c','ans':[],'wrong':[],'score':2},
            'd':{'username':'d','ans':[],'wrong':[],'score':7}
        }
        
        result = get_leaderboard(my_users)
        
        self.assertEqual(3,len(result))
        
    def test_returns_usernames_score(self):
        '''Should return tuples with username and score and highest score/username pair should be first in list'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':2},
            'e':{'username':'e','ans':[],'wrong':[],'score':5},
            'a':{'username':'a','ans':[],'wrong':[],'score':9},
            'b':{'username':'b','ans':[],'wrong':[],'score':6},
            'c':{'username':'c','ans':[],'wrong':[],'score':2},
            'd':{'username':'d','ans':[],'wrong':[],'score':7}
        }
        
        result = get_leaderboard(my_users)
        
        self.assertEqual(9,result[0][1])
        self.assertEqual('a',result[0][0])
        self.assertTrue(type(result[0]) == tuple)
        
class Test_get_users_scores(unittest.TestCase):
    '''Test my get_users_scores function'''
    
    def test_returns_list(self):
        '''should return list of users and scores'''
        my_users = {}
        all_scores_users = get_users_scores(my_users)
        
        self.assertTrue(type(all_scores_users) == list)
     
    def test_return_list_containg_list(self):
        '''Should return a list of tuples containing usernames and scores for each user on the game page'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':2}
        }
        all_scores_users = get_users_scores(my_users)
   
        self.assertTrue(len(all_scores_users) == 1)
        
        self.assertTrue(type(all_scores_users[0]) == tuple)
        
    def test_tuples_in_list_contain_two_elements(self):
        '''Test the tuples returned contain two elements'''
        
        my_users = {
            'j':{'username':'j','ans':[],'wrong':[],'score':2},
            'e':{'username':'e','ans':[],'wrong':[],'score':5},
        }
        all_scores_users = get_users_scores(my_users)
        print(all_scores_users)
        
        self.assertTrue(2 == len(all_scores_users[0]))