from app.models import Planet, Film

def generic_model_mutation_process(model, data, id=None, commit=True):
    '''
    Method used to create or update objects in db.

    Parameters
    ----------
        model : django.db.model
            model in which the data should be inserted
        data : Dict
            enlists the fields that will be used in the model
        id : int(optional)
            used to indicate if the process will be an update,
            and searches the object in db.
        commit: bool(optional)
            indicates if the object will be seved on db
    Returns
    -------
        model object seved or updated, or None if get model object went wrong
    '''
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item


def create_or_update_character_mutation_process(people, data, id=None):
    '''
    Method used to create or update characters, it is a realtionship between
    Film and People, the last has a realtion with Planet

    Parameters
    ----------
        model : People
            model in which the data should be inserted
        data : Dict
            enlists the fields that will be used in the model
        id : int(optional)
            used to indicate if the process will be an update,
            and searches the object in db.
    Returns
    -------
        model object seved or updated, or None if get model object went wrong
    '''
    if 'home_world_name' in data.keys():
        planet_object = Planet.objects.filter(name=data.pop('home_world_name'))
    else:
        planet_object = False
    
    if 'films_names' in data.keys():
        films = Film.objects.filter(title__in=data.pop('films_names'))
    else:
        films = False

    if id:
        people_object = people.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass
        for field, value in data.items():
            setattr(people_object, field, value)
    else:
        people_object = people(**data)
    
    if planet_object:
        people_object.home_world = planet_object.first()

    if films:
        for film in films:
            film.characters.add(people_object)

    people_object.save()

    return people_object
