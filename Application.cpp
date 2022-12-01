// Converted from Application.py
#include <QtCore/QUrl>
#include <QtGui/QGuiApplication>
#include <QtQml/QQmlApplicationEngine>
#include <QtWidgets/QApplication>

class Application
{
public:
engineQQmlApplicationEngineappQGuiApplication
    Application()
    {
        app = QApplication();
        engine = QQmlApplicationEngine();
    }

    void load_qml(const QString & qml)
    {
        engine->load(QUrl::fromLocalFile(qml));
    }

    void run()
    {
        sys->exit(app->exec());
    }
};
