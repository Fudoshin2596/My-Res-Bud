import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from .models import Resturant
from users.schema import UserType


class ResturantType(DjangoObjectType):
    class Meta:
        model = Resturant


class Query(graphene.ObjectType):
    resturants = graphene.List(ResturantType, search=graphene.String())

    def resolve_resturants(self, info, search=None):
        if search:
            filter = (
                Q(name__icontains=search) |
                Q(address__icontains=search)
            )
            return Resturant.objects.filter(filter)

        return Resturant.objects.all()


class CreateResturant(graphene.Mutation):
    resturant = graphene.Field(ResturantType)

    class Arguments:
        name = graphene.String()
        address = graphene.String()
        notes = graphene.String()
        rating = graphene.Int()
        price = graphene.String()
        phone_number = graphene.String()
        website = graphene.String()
        slug = graphene.String()

    def mutate(self, info, name, address, notes, rating, price, phone_number, website, slug):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError('Log in to add a resturant.')

        resturant = Resturant(name=name, address=address, notes=notes, rating=rating, price=price, phone_number=phone_number, website=website, slug=slug,
                      posted_by=user)
        resturant.save()
        return CreateResturant(resturant=resturant)


class UpdateResturant(graphene.Mutation):
    resturant = graphene.Field(ResturantType)

    class Arguments:
        resturant_id = graphene.Int(required=True)
        name = graphene.String()
        address = graphene.String()
        phone_number = graphene.String()

    def mutate(self, info, resturant_id, name, address, phone_number):
        user = info.context.user
        resturant = Resturant.objects.get(id=resturant_id)

        if resturant.posted_by != user:
            raise GraphQLError('Not permitted to update this record.')

        resturant.name = name
        resturant.address = address
        resturant.phone_number = phone_number

        resturant.save()

        return UpdateResturant(resturant=resturant)


class DeleteResturant(graphene.Mutation):
    resturant_id = graphene.Int()

    class Arguments:
        resturant_id = graphene.Int(required=True)

    def mutate(self, info, resturant_id):
        user = info.context.user
        resturant = Resturant.objects.get(id=resturant_id)

        if resturant.posted_by != user:
            raise GraphQLError('Not permitted to delete this record.')

        resturant.delete()

        return DeleteResturant(resturant_id=resturant_id)



class Mutation(graphene.ObjectType):
    create_resturant = CreateResturant.Field()
    update_resturant = UpdateResturant.Field()
    delete_resturant = DeleteResturant.Field()
