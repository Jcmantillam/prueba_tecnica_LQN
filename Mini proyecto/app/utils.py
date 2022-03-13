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
            and seache the object in db.
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
