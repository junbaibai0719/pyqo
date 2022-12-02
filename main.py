from src.Application import Application

if __name__ == '__main__':
    app = Application()
    app.load_qml("qml/App.qml")
    app.run()
