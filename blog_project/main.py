from blog import app, db


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(host='127.0.0.1', debug=True, port=5000)
