from flask import Flask

from herbert_app import create_app

application = create_app()

if __name__ == "__main__":
	application.run()