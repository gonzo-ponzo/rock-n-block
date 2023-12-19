from web3 import Web3, AsyncHTTPProvider
from web3.middleware import geth_poa_middleware

from config import USER_WALLET


class Contract:
    def __init__(
        self, endpoint_uri: str, contract_address: str, chain_id, abi_path: str
    ):
        self.chain_id = chain_id
        self.provider = AsyncHTTPProvider(endpoint_uri=endpoint_uri)
        self.w3 = Web3(self.provider)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        with open(abi_path, "r") as abi_file:
            abi = abi_file.read()
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    async def mint(
        self,
        user_wallet: str,
        private_key: str,
        owner: str,
        random_string: str,
        media_url: str,
    ) -> str:
        """Send transaction to blockchain"""
        nonce = self.w3.eth.get_transaction_count(user_wallet)
        build_params = {
            "chainId": self.chain_id,
            "from": USER_WALLET,
            "gas": 2500000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": nonce,
        }
        transaction = await self.contract.functions.mint(
            owner, random_string, media_url
        ).buildTransaction(build_params)
        signed_transaction = await self.w3.eth.account.sign_transaction(
            transaction, private_key
        )
        transaction_hash = await self.w3.eth.send_raw_transaction(
            signed_transaction.rawTransaction
        )
        return transaction_hash.hex()

    async def total_supply(self) -> int:
        """Get total supply of tokens"""
        return await self.contract.functions.totalSupply().call()
