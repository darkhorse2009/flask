from app import create_app
from flask.ext.script import Manager, Server

app = create_app('default')
manager = Manager(app)

if __name__ == '__main__':
    app.run(debug=False, threaded=True)


#####test
#
#test2
#
##test3
#
#
#end
#
#test4
#test5
#
#
#