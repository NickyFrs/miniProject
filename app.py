from taskManager import taskmanager


app = taskmanager()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)
