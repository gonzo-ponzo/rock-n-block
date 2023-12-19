from fastapi import APIRouter, status
import random
import string

from db.models import CreateTokenSchema, TokenSchema, Tokens
from config import (
    ENDPOINT_URI,
    CHAIN_ID,
    CONTRACT_ADDRESS,
    ABI_PATH,
    USER_WALLET,
    PRIVATE_KEY,
)
from contracts.constructor import Contract


tokens_api_router = APIRouter(prefix="/tokens")
mintable__nft_contract = Contract(
    endpoint_uri=ENDPOINT_URI,
    contract_address=CONTRACT_ADDRESS,
    chain_id=CHAIN_ID,
    abi_path=ABI_PATH,
)


@tokens_api_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_token(body: CreateTokenSchema) -> TokenSchema:
    """Creates new unique token in blockchain and writes it to database"""
    random_string = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(20)
    )
    transaction_hash = await mintable__nft_contract.mint(
        user_wallet=USER_WALLET,
        private_key=PRIVATE_KEY,
        owner=body.owner,
        media_url=body.media_url,
        random_string=random_string,
    )
    new_token = await Tokens.create(
        unique_hash=random_string,
        tx_hash=transaction_hash,
        media_url=body.media_url,
        owner=body.owner,
    )
    return TokenSchema.from_tortoise_orm(new_token)


@tokens_api_router.get("/list", status_code=status.HTTP_200_OK)
async def read_all_tokens() -> list[TokenSchema]:
    """Read list of all token objects"""
    return await TokenSchema.from_queryset(Tokens.all())


@tokens_api_router.get("/total_supply", status_code=status.HTTP_200_OK)
async def read_total_supply() -> dict[str, int]:
    """Read total supply of tokens in blockchain"""
    total_supply = await mintable__nft_contract.total_supply()
    return {"total_supply": total_supply}
