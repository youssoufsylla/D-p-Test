import pickle

def load_user_data(serialized_data):
    return pickle.loads(serialized_data)