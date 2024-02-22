def obtenerPaises(obj):
    objeto = {
        'Pais': obj['Country/Territory'],
        'Poblacion Mundial': float(obj['World Population Percentage']),
        'Continente': obj['Continent']
    }
    return objeto