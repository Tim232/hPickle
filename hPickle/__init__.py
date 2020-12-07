import pickle

module = "Python Pickle Handler"

def save(filename, data):
    print(f'[PICKLE MODULE] [Process] Saving {filename}...')
    with open(filename,  mode='wb') as f:
        pickle.dump(data, f)
    print(f'[PICKLE MODULE] [Success] Saved {filename}!')
    return data


def load(filename):
    print(f'[PICKLE MODULE] [Process] Loading {filename}...')
    with open(filename,  mode='rb') as f:
        data = pickle.load(f)
    print(f'[PICKLE MODULE] [Success] Loaded {filename}!')
    return data


def check(filename):
    print(f'[PICKLE MODULE] [Process] Checking {filename}...')
    try:
        load(filename)
        print(f'[PICKLE MODULE] [Success] Successfully checked {filename}!')
        return True # data
    except FileNotFoundError:
        print(f'[PICKLE MODULE] [Fail] {filename} does not exist...')
        return False
    except pickle.UnpicklingError:
        print(f'[PICKLE MODULE] [Fail] {filename} is an invalid pickle file...')
        return False
