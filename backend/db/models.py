from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Tokens(models.Model):
    id = fields.IntField(pk=True)
    unique_hash = fields.CharField(unique=True, max_length=50)
    tx_hash = fields.CharField(max_length=50)
    media_url = fields.CharField(max_length=512)
    owner = fields.CharField(max_length=50)


TokenSchema = pydantic_model_creator(Tokens)
CreateTokenSchema = pydantic_model_creator(Tokens, include=("media_url", "owner"))
