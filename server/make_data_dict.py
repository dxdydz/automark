#This file creates the testing data and expected results. 

import numpy as np
import pickle, os.path

DD_LOC = './data_dict.pickle'

def crdict(some_thing):
    '''Function to package data as a dictionary for transmission via JSON'''
    something_type = type(some_thing).__name__
    if something_type == 'ndarray':
        return { 'data':some_thing.tolist(), 'type':something_type }
    else:
        return { 'data' : some_thing, 'type':something_type }


def create_add():
    '''Example function for creating a problem. In this case, the function the
    students must implement is a simple addition function. Returns: a dict with
    a set of input values and corresponding set of correct results.'''
    
    #We define the dict with a list of inputs and a list of expected outputs
    week_one_dict = {'inputs':[],'outputs':[]}

    #We also create a set of random ID numbers to match student submissions
    #with the appropriate result in the database.
    ipds = list(np.random.choice(10000, 100, replace=False))

    week_one_dict['ipd'] = ipds
    for ipd in ipds:
        np.random.seed(ipd+22071988)
        a = np.random.randint(1, 100)
        b = np.random.randint(1, 100)
        result = a+b

        #'inputs' should contain the names of the function arguments (defined in notebook)
        #and the values should be passed through crdict()
        week_one_dict['inputs'].append(  {'a': crdict(a), 'b':crdict(b)} )
        week_one_dict['outputs'].append(result)

    return week_one_dict




if __name__ == '__main__':
    data_dict = dict([])
    
    #Load file if it exists...
    if os.path.isfile(DD_LOC):
        data_dict = pickle.load(open(DD_LOC, 'r'))

    data_dict['Toy Example'] = create_add()

    #Save file
    pickle.dump(data_dict, open(DD_LOC,'w'))
