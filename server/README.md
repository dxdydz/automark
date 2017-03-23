# Server

The heart of the server is the bottle app defined in bottle_app.py. This defines the main points of interaction with the server.

Additionally, there is a script make_data_dict.py which creates the data for evaluation of the assignments and saves it to a file named data_dict.pickle. User details are stored in the user_details folder, and their progress through the course is stored in the prog folder.

To create new assignments, define appropriate functions in make_data_dict, following the example present there. Then run the script, and re-start the bottle server.
