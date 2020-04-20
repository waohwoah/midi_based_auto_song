import learn


def initialize():
    if input("Clean & Reinitialize Model?\nY to clean\nN to modify\n").strip().upper() == 'Y':
        create()
        save()
    else:
        try:
            load()
        except:
            print("Model not available/corrupted!\nCreating new model...")
            create()
            save()


def load():
    learn.load_model()
    print("Model loaded succesfully!")


def save():
    learn.save_model()
    print("Model created succesfully!")


def create():
    learn.create_model()
    print("Model added succesfully!")


# initialize()
