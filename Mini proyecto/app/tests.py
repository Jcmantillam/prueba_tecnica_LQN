import json
from turtle import pd
from app.models import Planet

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)


class CreatePlanet(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
            mutation CreateOrUpdatePlanet {
              createOrUpdatePlanet(
                input: {
                  name: "Tierra",
                  climate: "unknow",
                  rotationPeriod: "24"}
              ) {
                planet {
                  name
                }
              }
            }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(content['data']['createOrUpdatePlanet']['planet']['name'], "Tierra")

class UpdatePlanet(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
            mutation CreateOrUpdatePlanet {
              createOrUpdatePlanet(
                input: {
                  name: "Tierra",
                  climate: "unknow",
                  rotationPeriod: "24"}
              ) {
                planet {
                  id
                  name
                }
              }
            }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        response = self.query(
            '''
            mutation CreateOrUpdatePlanet {
              createOrUpdatePlanet(
                input: {
                  id: "UGxhbmV0VHlwZTo2Mw=="
                  name: "Earth",
                  climate: "unknow",
                  rotationPeriod: "24"
                }
              ) {
                planet {
                  id
                  name
                }
              }
            }
            ''',
        )

        content = json.loads(response.content)
        self.assertEqual(content['data']['createOrUpdatePlanet']['planet']['name'], "Earth")


class CreateCharacter(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
            mutation CreateOrUpdateCharacter {
              createOrUpdateCharacter(
                input: {
                  name: "John Doe"
                  height: "170"
                  mass: "77"
                  hairColor: "brown"
                  skinColor: "fair"
                  eyeColor: "brown"
                  birthYear: "19BBY"
                  gender: "male"
                  homeWorldName: "Tatooine"
                  filmsNames: ["A New Hope"]
                }
              ) {
                people{
                  id
                  name
                  homeWorld{
                    name
                  }
                }
              }
            }
            ''',
        )
    

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(content['data']['createOrUpdateCharacter']['people']['name'], "John Doe")


class UpdateCharacter(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
            mutation CreateOrUpdateCharacter {
              createOrUpdateCharacter(
                input: {
                  name: "John Doe"
                  height: "170"
                  mass: "77"
                  hairColor: "brown"
                  skinColor: "fair"
                  eyeColor: "brown"
                  birthYear: "19BBY"
                  gender: "male"
                  homeWorldName: "Tatooine"
                  filmsNames: ["A New Hope"]
                }
              ) {
                people{
                  id
                  name
                  homeWorld{
                    name
                  }
                }
              }
            }
            ''',
        )

        self.assertResponseNoErrors(response)

        response = self.query(
            '''
            mutation CreateOrUpdateCharacter {
              createOrUpdateCharacter(
                input: {
                  id: "UGVvcGxlVHlwZTo4OQ=="
                  name: "John Doe 2"
                }
              ) {
                people{
                  id
                  name
                  homeWorld{
                    name
                  }
                }
              }
            }
            ''',
        )

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(content['data']['createOrUpdateCharacter']['people']['name'], "John Doe 2")
