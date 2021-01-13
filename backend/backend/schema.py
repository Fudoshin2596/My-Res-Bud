import graphene
import myresbud.schema
import users.schema
# import graphql_jwt


class Query(users.schema.Query, myresbud.schema.Query, myresbud.schema.QueryR, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, myresbud.schema.Mutation, graphene.ObjectType):
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
