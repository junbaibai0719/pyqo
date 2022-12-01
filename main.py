from Application import Application

if __name__ == '__main__':
    app = Application()
    import main_rc
    app.load_qml("qrc:/qml/App.qml")
    app.run()
