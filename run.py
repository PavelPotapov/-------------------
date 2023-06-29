from blog import create_app, db



app = create_app()

from blog.routes import *
from blog.admin import *

if __name__ == '__main__':
    #create_table
    #db.init_app(app)
    app.run()
