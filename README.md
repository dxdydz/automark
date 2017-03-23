# AutoMark
AutoMark is a lightweight, bottle-based evaluation server for python programming assignments. The basic idea is simple: students are given functions to fill in, with predefined arguments and returns. These functions are tested using data provided by the server, and the results are sent back to the server, where the student's success is logged.

The server component is present in the server folder, along with a README describing its components in more detail.

The client component is in client, and consists primarily of a clientside script that should be in the pythonpath for the user.

##Dependencies

I'm not sure, but at least:

- numpy
- Bottle
- Jupyter (for assignment notebooks)

##Running example

This repository is set up for running locally. To try it out, run the server script bottle_app.py with

    python server/bottle_app.py

Then load up the client/Example.ipynb notebook in Jupyter notebook. You can execute the code blocks and see what it looks like from the student's perspective. The student is able to check their progress at the submissions page, which locally will be http://localhost:8080/submissions/username.

##Running on PythonAnywhere

For our course, we have run this on the free service http://pythonanywhere.com. You'll need to comment out the line at the bottom of bottle_app.py, as well as change the destination address in client_req.py.
