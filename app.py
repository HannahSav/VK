from flask import Flask
from config import Config
from models import db
from routes import auth, orders, products, warehouses

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(orders.bp)
app.register_blueprint(products.bp)
app.register_blueprint(warehouses.bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
