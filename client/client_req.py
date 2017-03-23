import sys, json, requests, numpy as np


def register_id(usernm,mem1):
    s = requests.Session()
    base = 'http://localhost:8080/' #REPLACE THIS WITH YOUR SERVER ADDRESS

    rin = s.get(base+'register_user/'+'/'.join([usernm,mem1[0],mem1[1]]))
    try:
        print rin.text
    except:
        sys.exit("Something didn't work.")

def test_student_function(userid, assignment, function_to_test, argument_keys):
    if not userid:
        print "Please remember to insert your user id."
        return
    if userid=='replace_with_name':
        print "Hey! Is your name *really* 'replace_with_name'? How weird!"
        return
    s = requests.Session()
    base = 'http://localhost:8080/' #REPLACE WITH SERVER ADDRESS

    rin = s.get(base+'input/'+str(userid)+'/'+assignment)
    try:
        din = json.loads(rin.text)
    except:
        print "Error loading response. Are you sure you've entered a valid user number?"
        sys.exit()

    arglist = []
    for item in argument_keys:
        if din['input'][item]['type'] == 'ndarray':
            arglist.append(np.array(din['input'][item]['data']))
        else:
            arglist.append(din['input'][item]['data'])

    testresult = function_to_test(*arglist)
    rout = s.get(base+'result/'+str(userid)+'/'+assignment+'/'+str(din['ipd'])+'/'+json.dumps(np.array(testresult).tolist()))

    dout = json.loads(rout.text)

    if dout['correct']:
        print "Test was successful. Congratulations!"
    else:
        print "Test failed. Please review your code."
