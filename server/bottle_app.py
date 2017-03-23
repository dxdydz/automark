
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run
from random import randrange
import json,os.path, numpy as np, pickle

SITE_PREFIX = '.' #Change to appropriate file structure prefix

TOL = 0.00001 #Tolerance value for evaluation numerical results

#Read in user details from user_details folder
user_list = [thing.split('.')[0] for thing in os.listdir(SITE_PREFIX+'/user_details/') if thing.split('.')[-1] == 'details']

user_progress = dict([])

def checkload_userprog(each_user):
    '''Load user progress from prog folder if it exists'''
    user_progfile = SITE_PREFIX+'/prog/'+str(each_user)+'.prog'
    if os.path.isfile(user_progfile):
        user_progress[each_user] = dict([])
        for line in open(user_progfile,'r'):
            a,b = line.rstrip().split(',')
            user_progress[each_user][a] = 'True' == b   # for line in open(user_progfile)]
    else:
        user_progress[each_user] = dict([])


for an_user in user_list: #Load users progress
    checkload_userprog(an_user)


def write_to_progfile(username,userprogdict):
    upf = open(SITE_PREFIX+'/prog/'+str(username)+'.prog','w')
    for key in userprogdict.keys():
        upf.write(key+','+str(userprogdict[key])+'\n')
    upf.close()

#Load data dictionary file with inputs and outputs
data_dict = pickle.load(open(SITE_PREFIX+'/data_dict.pickle','r'))


@route('/register_user/<username>/<name1>/<email1>',method='GET')
def register_user(username='foo',name1 = '',email1=''):#,name2='',email2=''):
    details_loc = SITE_PREFIX+'/user_details/'
    if username not in user_list and len(user_list)<150:
        user_list.append(username)
        checkload_userprog(username)
        if not os.path.isfile(details_loc+username+'.details'):
            udf = open(details_loc+username+'.details','w')
            udf.write(name1+', '+email1)#+'\n'+name2+', '+email2)
            udf.close()
            return "Right, that's you registered. Good luck!"
        else:
            return "Something weird happened. Have you already registered?"
    else:
        return "Username already registered."
    return "You should never see this. Something went wrong with our logic."


@route('/')
def hello_world():
    return '<center>Welcome to the Testing Center.<p>Please take a seat, your number will be called shortly.</center>'


@route('/test/<userid>',method='GET')
def get_test( userid = ''):
    if '' != userid:
        return { "success" : True, "userid": userid }


@route('/input/<userid>/<assignment>',method='GET')
def return_input(userid = '', assignment = ''):
    if userid in user_list and assignment in data_dict:
        random_ipd = randrange(len(data_dict[assignment]["ipd"]))
        return { "user" : userid, "ipd" : data_dict[assignment]["ipd"][random_ipd], "input" : data_dict[assignment]['inputs'][random_ipd] }


@route('/verify_input/<assignment>/<ipd:int>/<given_input>',method='GET')
def verify_input(assignment = '', ipd=0, given_input = ''):
    if assignment in data_dict and ipd in data_dict[assignment]['ipd']:
        try:
            to_verify = json.loads(given_input)
            if to_verify == data_dict[assignment]['inputs'][ipd]:
                return { "success" : True}
            else:
                return { "failure" : True}
        except:
            return { "Failure" : True}


@route('/result/<userid>/<assignment>/<ipd:int>/<answer>',method='GET')
def check_answer(userid='',assignment='',ipd=-1,answer=''):
    if userid in user_list and assignment in data_dict and ipd in data_dict[assignment]['ipd']:
        try:
            if assignment not in user_progress[userid]:
                user_progress[userid][assignment] = False
                write_to_progfile(userid,user_progress[userid])

            ipd_idx = data_dict[assignment]['ipd'].index(ipd)

            if np.sum(np.abs(np.array(json.loads(answer)) - data_dict[assignment]['outputs'][ipd_idx])) < TOL:
                if user_progress[userid][assignment] == False:
                    user_progress[userid][assignment] = True
                    write_to_progfile(userid,user_progress[userid])
                return {"correct": True }
            else:
                return {"correct": False}
        except:
            print "no answer"


@route('/submissions/<userid>')
def display_progress(userid=''):
    if userid in user_list:
        page = '<center><h3>AML/VSE 2016</h3><br>Practical Assignments<p>USER: '+str(userid)+'<p><table border="1"><tr><td><b>Assignment Name</b></td><td><b>Status</b></td></tr><tr>'
        for ass_key in sorted(data_dict.keys()):
            page = page+'<tr><td>'+ass_key+'</td><td>'
            if ass_key in user_progress[userid]:
                if user_progress[userid][ass_key] == True:
                    page = page +'COMPLETE'
                else:
                    page = page +'Attempted'
            page = page+'</td></tr>'
        page = page+'</table></center>'
        return page


#The below is for running online
#application = default_app()

#To run locally, use the following instead:
run(app=None, server='wsgiref', host='127.0.0.1', port=8080, interval=1, reloader=False, quiet=False, plugins=None, debug=None)
