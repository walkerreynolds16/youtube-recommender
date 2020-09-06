import sys
import setupServer

application = setupServer.createFlaskApp()
app = application
setupServer.setup(app, sys.argv)
