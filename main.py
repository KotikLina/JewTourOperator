from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def index():
    css = "../static/JewTourOperator.css"
    return render_template("JewTourOperator.html", title="aviasales - Главная", css=css)


@app.route('/listOfTours')
def list_of_tours():
    list_tours = [
        {'image': '/static/images/Asstana.jpg', 'title': 'Тур в Assтану',
         'description': 'Город богат достопримечательностями, включая знаменитую Байтерек, '
                        'Оперный театр, торговый центр "Хан Шатыр", Национальный музей Казахстана и многое другое',
         'url': '/tourDescription?tour=Asstana'},
        {'image': '/static/images/Shymkent.jpg', 'title': 'Тур в Шымкент',
         'description': 'Красивый город с уникальными мечетями, музеями и парками,'
                        ' где можно попробовать национальную кухню.',
         'url': '/tourDescription?tour=Shymkent'},
        {'image': '/static/images/Ust-Kamenogorsk.jpg', 'title': 'Тур в Усть-Каменогорск',
         'description': 'В городе есть множество памятников, парков и садов. '
                        'Здесь можно покататься на лыжах и сноуборде зимой, '
                        'а летом провести время на реке и посетить удивительные горные озера.',
         'url': '/tourDescription?tour=Ust-Kamenogorsk'},
        {'image': '/static/images/Alma-Aty.jpg', 'title': 'Тур в АлмаАту',
         'description': 'крупный город, который является центром экономики и культуры Центральной Азии.'
                        ' Город славится своей красивой природой, национальной кухней, музеями и '
                        'известным на весь мир озером Иссык-Куль',
         'url': '/tourDescription?tour=AlmaAty'},
        {'image': '/static/images/Aktay.jpg', 'title': 'Тур в Актау',
         'description': 'Супер мотивационная речь почему вы должны выбрать именно этот тур',
         'url': '/tourDescription?tour=Aktay'},
    ]
    random_tours = random.sample(list_tours, 3)
    css = "../static/ListOfTours.css"
    return render_template("ListOfTours.html", title="aviasales - Список туров", css=css, random_tours=random_tours)


@app.route('/tourDescription')
def tour_description():
    name_tour = request.args.get('tour')
    css = "../static/TourDescription.css"
    return render_template('TourDescription.html', title="aviasales - Описание тура", css=css, name_tour=name_tour)


if __name__ == '__main__':
    app.run(debug=True)
