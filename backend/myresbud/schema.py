import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphql import GraphQLError
from django.db.models import Q
import django_filters

from .models import Resturant
from users.schema import UserType

from utils.googleapi import ResturantInfo
from utils.googleapi import GMAPS_API_KEY
from utils.zomatoapi import Zomato

ZomatoObj = Zomato()

class ResturantType(DjangoObjectType):
    class Meta:
        model = Resturant


class Query(graphene.ObjectType):
    resturants = graphene.List(ResturantType, search=graphene.String())

    def resolve_resturants(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(name__icontains=search) |
                Q(cuisines__icontains=search) |
                Q(address__icontains=search) |
                Q(price__exact=search)
            )

            return Resturant.objects.filter(filter)

        return Resturant.objects.all()


class ResturantNode(DjangoObjectType):
    class Meta:
        # Assume you have an Animal model defined with the following fields
        model = Resturant
        filter_fields = {
            'rating': ['exact', 'gte', 'gt']
        }
        interfaces = (relay.Node, )

class QueryR(graphene.ObjectType):
    resturant = relay.Node.Field(ResturantNode)
    all_resturants = DjangoFilterConnectionField(ResturantNode)

class CreateResturant(graphene.Mutation):
    resturant = graphene.Field(ResturantType)

    class Arguments:
        name = graphene.String(required=True)
        # notes = graphene.String()

    def mutate(self, info, name):
        # user = info.context.user
        userlocation = 'New York, NY'

        # if user.is_anonymous:
        #     raise GraphQLError('Log in to add a resturant.')

        ResturantObject = ResturantInfo(name, GMAPS_API_KEY, userlocation)
        info = ResturantObject.placeInfo()

        passers = ZomatoObj.match(name)
        if passers is not None:
            j = passers[0][1]['cuisines']
            if isinstance(j, str):
                cuisines = j.split()
            else:
                cuisines = j
        else:
            cuisines = ['Unknown']

        resturant = Resturant(name=info['name'], address=info['address'],
                    notes="", rating=info['rating'], price=info['price'],
                    phone_number=info['phonenumber'], website=info['website'], 
                    slug=info['id'], cuisines=cuisines
                    ) #posted_by=user
        resturant.save()
        return CreateResturant(resturant=resturant)


class UpdateResturant(graphene.Mutation):
    resturant = graphene.Field(ResturantType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()
        phone_number = graphene.String()
        notes = graphene.String()

    def mutate(self, info, id, name, address, phone_number, notes):
        # user = info.context.user
        resturant = Resturant.objects.get(id=id)

        # if resturant.posted_by != user:
        #     raise GraphQLError('Not permitted to update this record.')

        resturant.name = name
        resturant.address = address
        resturant.phone_number = phone_number
        resturant.notes = notes

        resturant.save()

        return UpdateResturant(resturant=resturant)


class DeleteResturant(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        # user = info.context.user
        resturant = Resturant.objects.get(id=id)

        # if resturant.posted_by != user:
        #     raise GraphQLError('Not permitted to delete this record.')

        resturant.delete()

        return DeleteResturant(id=id)

class Mutation(graphene.ObjectType):
    create_resturant = CreateResturant.Field()
    update_resturant = UpdateResturant.Field()
    delete_resturant = DeleteResturant.Field()
