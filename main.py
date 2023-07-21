from flask import Flask, render_template

app = Flask(__name__)

""" app route para definir la ruta que se recibe mediante el get, se pueden tener varias """
@app.route('/')
def prueba123():
    """ la sentencia (def) sirve para crear la funcion que se invoca al entrar a la ruta establecida anteriormente """
    """ dentro del return irá lo que nos returna la funcion y se mostrará en la vista de nuestro proyecto """
    return "<center><h2>Hola mundo 2687386</h2></center>"
    

""" acá creamos otra ruta diferente con una nueva función y nuevas instrucciones dentro de la misma """
@app.route('/paises')
def paises():
    
    continentes = [
        {
            "nombre" : "América",
            "paises" : [
                        {
                         "nombre" : "Colombia",
                         "capital" : "Bogotá",
                         "modena" : "peso colombiano",
                         "poblacion" : 51,
                         "superficie" : 1142000
                         },
                        {
                         "nombre" : "Perú",
                         "capital" : "Lima",
                         "moneda" : "Sol",
                         "poblacion" : 33,
                         "superficie" : 1285000
                        }
                        ]
        },
        {
            "nombre" : "Europa",
            "paises" : [
                        { "nombre" : "Reino Unido",
                         "capital" : "Londres",
                         "modena" : "Libra esterlina",
                         "poblacion" : 67,
                         "superficie" : 243610000
                         },
                        {
                         "nombre" : "Francia",
                         "capital" : "Paris",
                         "moneda" : "Euro",
                         "poblacion" : 68,
                         "superficie" : 551695000
                        },
                        {
                         "nombre" : "Italia",
                         "capital" : "Roma",
                         "moneda" : "Euro",
                         "poblacion" : 59,
                         "superficie" : 302073000
                        }
                        ]
        },
        {
            "nombre" : "Asia",
            "paises" : [
                        { "nombre" : "Japon",
                         "capital" : "Tokio",
                         "modena" : "Yen",
                         "poblacion" : 125,
                         "superficie" : 377973000
                         }
                        ]
        }
    ]
    paises = [
        [
            {
                "nombre" : "América",
                "paises" : [
                            "Colombia",
                            "Argentina",
                            "México",
                            "Perú"
                            ]
            }
        ],
        [
            {
                "nombre" : "Europa",
                "paises" : [
                            "España",
                            "Italia",
                            "Reino Unido",
                            "Francia",
                            "Andorra"
                            ]
            }
        ],
        [
            {
                "nombre" : "Asia",
                "paises" : [
                            "Japon",
                            "Korea",
                            "China",
                            "Vietnam",
                            "Korea del norte"
                            ]
            }   
        ]
    ]
    #Lista en python
    """ paises = [
        [
            'Colombia',
            'Argentina',
            'Mexico'
        ],
        [
            'España',
            'Italia',
            'Reino Unido'
        ],
        [
            'Japon',
            'Korea',
            'China'
        ]
    ] """
    
    """ Variables de conteo """    
    
    longitud_america = len(paises[0][0]["paises"])
    longitud_europa = len(paises[1][0]["paises"])
    longitud_asia = len(paises[2][0]["paises"])
    print(longitud_america)
    print(longitud_europa)
    print(longitud_asia)
    user = 'Andres Yate'
    """ Se declara una variable de tipo string y mediante el metodo render_template (que se importa desde Flask). Además se le envia la variable a la vista """
    """ Se debe tener las vistas en una carpeta llamada (templates) y puede ser en HTML u otros lenguajes""" 
    return render_template('paises_listas.html', 
                           user = user, 
                           continentes = paises, 
                           america = longitud_america, 
                           europa = longitud_europa, 
                           asia = longitud_asia
                           )