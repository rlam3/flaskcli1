from flask_script import Manager, Shell, Server

from app.application import create_app

manager = Manager(create_app())

def _make_context():
   return dict(app=manager)

# Access to shell
manager.add_command('shell',
    Shell(
        make_context=_make_context,
        use_ipython=True
    )
)

manager.add_command("runserver",
    Server(
        threaded=True,
        host='0.0.0.0',
        port=6000,
    )
)

if __name__ == '__main__':
    manager.run()
