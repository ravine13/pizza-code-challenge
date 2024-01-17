from random import randint, choice as rc
from faker import Faker

from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

pizza_data = [
    {"id": 1, "name": "Classic Margherita", "ingredients": "Tomato Sauce, Mozzarella, Basil"},
    {"id": 2, "name": "Pepperoni Passion", "ingredients": "Tomato Sauce, Mozzarella, Pepperoni"},
    {"id": 3, "name": "Hawaiian", "ingredients": "Tomato Sauce, Mozzarella, Ham, Pineapple"},
    {"id": 4, "name": "Veggie Supreme", "ingredients": "Tomato Sauce, Mozzarella, Bell Peppers, Mushrooms, Olives, Onions"},
    {"id": 5, "name": "Meat Lovers", "ingredients": "Tomato Sauce, Mozzarella, Pepperoni, Sausage, Ground Beef, Ham"},
    {"id": 6, "name": "BBQ Chicken", "ingredients": "BBQ Sauce, Mozzarella, Grilled Chicken, Red Onions, Bell Peppers"},
    {"id": 7, "name": "Taco Fiesta", "ingredients": "Refried Beans, Salsa, Cheddar, Ground Beef, Lettuce, Tomatoes, Sour Cream"},
    {"id": 8, "name": "Seafood Delight", "ingredients": "Tomato Sauce, Mozzarella, Shrimp, Calamari, Clams, Mussels"},
    {"id": 9, "name": "Four Cheese", "ingredients": "Tomato Sauce, Mozzarella, Cheddar, Feta, Parmesan"},
    {"id": 10, "name": "Chicken Alfredo", "ingredients": "Alfredo Sauce, Mozzarella, Grilled Chicken, Mushrooms, Spinach"}
]

restaurant_names = [
    "The Pizza Palace",
    "The Galitos ",
    "The Domino's Pizza",
    "The Kwa Mathee",
    "The Crispy Crust",
    "The chicken inn",
    "The sunset pizza palace",
    "The Doughy Delight",
    "The Papa John's",
    "The Sbarro"
]

fake = Faker()

def pizzas():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    restaurants = []    
    for i in range(10):
        restaurant_details = Restaurant(name=rc(restaurant_names), address=fake.address())
        restaurants.append(restaurant_details)
    db.session.add_all(restaurants)
    db.session.commit()
        
    pizzas= []
    for pizza_properties in pizza_data:
        pizza_details = Pizza(name=(pizza_properties["name"]), ingredients=pizza_properties["ingredients"])
        pizzas.append(pizza_details)
    db.session.add_all(pizzas)
    db.session.commit()
        
    restaurant_pizzas = []
    for i in range(10):
        restaurant_pizza = RestaurantPizza(
            price=randint(5, 30),
            restaurant_id =rc(restaurants).id,
            pizza_id=rc(pizzas).id
            )
        restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        pizzas()
