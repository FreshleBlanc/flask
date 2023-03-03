from app import app
from flask import render_template
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return 'This is where you contact that guy.'

@app.route('/blog')
def blog():
    return 'Be the influencer you have always wanted to be.'

@app.route('/shop')
def shop():
    return 'Retail therapy is not the best therapy but hey, its some therapy.'

@app.route('/duck')
def duck():
    return 'The quakiest quackers of the quack-a-ton'


user_data = { #mock user table
   'dylans': {
        'user_id': 1,
        'email': 'dylans@gmail.com',
        'name': 'Dylan Smith',
        'favorite_color': 'Purple',
        'is_active': True

    },
    'jdoe': {
        'user_id': 2,
        'email': 'johndoe@gmail.com',
        'name': 'John Doe',
        'favorite_color': 'Orange',
        'is_active': True
    },
    'jenm': {
        'user_id': 3,
        'email': 'jenm@yahoo.com',
        'name': 'Jen Max',
        'favorite_color': 'Blue',

        'is_active': False
    }
}


#functions/Endpoints:
#get all users and theri data
#get all user emails
#get a user by the user name
# get user by email
#find all users with a specified favorite color


@app.route('/api/users')
def get_users():
    return user_data


@app.route('/api/users/emails')
def get_user_emails():
    emails = []

    for user in user_data.values():
        email.append(user[emails])

    return emails


@app.route('/api/users/active')
def get_active_users():
    full_names = []

    for user in user_data.values():
        if user['is_active'] == True:
            full_names.append(user['name'])

    return full_names



@app.route('/api/user/<username>')
def get_user_name(username):
    if username in user_data:
        return user_data[username]

    return f'user with username {username} not found'

@app.route('/api/user/email/<email>')
def get_user_by_email(email):
    result = None

    for user in user_data.values():
        if user['email'] == email:
            return user
    
    return f'user with email {email} not found'


@app.route('/api/user/color/<favorite_color>')
def get_user_by_color(favorite_color):
    users = []

    for user in user_data.values():
        if user['favorite_color'].lower() == favorite_color.lower():
            users.append(user)

    return users



car_data = {
0: {
    "name": "Maruti Swift Dzire VDI",
    "year": 2014,
    "selling_price": 450000
},
1: {
    "name": "Skoda Rapid 1.5 TDI Ambition",
    "year": 2014,
    "selling_price": 370000
},
2: {
    "name": "Honda City 2017-2020 EXi",
    "year": 2006,
    "selling_price": 158000
}
}

# Get all cars
# Get cars in a dictionary separated by year, for example:
car_year_result = {
    2014: ["Maruti Swift Dzire VDI","Skoda Rapid 1.5 TDI Ambition"],
    2006: ["Honda City 2017-2020 EXi"]
}
# Get a car by it's ID (it's ID is just the key in the car data dictionary)

# Get all cars below a given price point, so if the user enters 380000, you'd show the second and third cars




@app.route('/api/cars')
def get_cars():
   return car_data


@app.route('/api/cars/year')
def get_cars_by_year():
    result = {}

    for car in car_data.values():
        if car['year'] in result:
            if result['year']:
                result[car['year']].append(car['name'])
            else:
                result[car['year']] = [car['name']]




@app.route('/api/cars/<id>')
def get_car_by_id(id):
    id = int(id)
    if id in car_data:
        return car_data[id]
    
    return f'ID number {id} not found'
    

