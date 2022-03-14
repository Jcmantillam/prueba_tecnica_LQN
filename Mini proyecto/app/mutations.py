import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType, PeopleType
from .utils import generic_model_mutation_process, create_or_update_character_mutation_process


class CreateOrUpdatePlanet(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return CreateOrUpdatePlanet(planet=planet)


class CreateOrUpdateCharacter(graphene.relay.ClientIDMutation):

    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.String(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=False)
        home_world_name = graphene.String(required=False)
        films_names = graphene.List(graphene.String)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'people': People, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        people = create_or_update_character_mutation_process(**data)
        return CreateOrUpdateCharacter(people=people)
