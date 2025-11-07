import os
from dataclasses import dataclass

DEFAULT_MAINNET_PROXY_URL = "https://gateway.dharitri.org"
DEFAULT_MAINNET_API_URL = "https://api.dharitri.org"
DEFAULT_MAINNET_DEEP_HISTORY_URL = DEFAULT_MAINNET_PROXY_URL
ENV_MAINNET_PROXY_URL = os.environ.get("MAINNET_PROXY_URL")
ENV_MAINNET_API_URL = os.environ.get("MAINNET_API_URL")
ENV_MAINNET_DEEP_HISTORY_URL = os.environ.get("MAINNET_DEEP_HISTORY_URL")

DEFAULT_DEVNET_PROXY_URL = "https://devnet-gateway.dharitri.org"
DEFAULT_DEVNET_API_URL = "https://devnet-api.dharitri.org"
DEFAULT_DEVNET_DEEP_HISTORY_URL = DEFAULT_DEVNET_PROXY_URL
ENV_DEVNET_PROXY_URL = os.environ.get("DEVNET_PROXY_URL")
ENV_DEVNET_API_URL = os.environ.get("DEVNET_API_URL")
ENV_DEVNET_DEEP_HISTORY_URL = os.environ.get("DEVNET_DEEP_HISTORY_URL")

DEFAULT_TESTNET_PROXY_URL = "https://testnet-gateway.dharitri.org"
DEFAULT_TESTNET_API_URL = "https://testnet-api.dharitri.org"
DEFAULT_TESTNET_DEEP_HISTORY_URL = DEFAULT_TESTNET_PROXY_URL
ENV_TESTNET_PROXY_URL = os.environ.get("TESTNET_PROXY_URL")
ENV_TESTNET_API_URL = os.environ.get("TESTNET_API_URL")
ENV_TESTNET_DEEP_HISTORY_URL = os.environ.get("TESTNET_DEEP_HISTORY_URL")


@dataclass
class Configuration:
    chain_id: str
    proxy_url: str
    api_url: str
    deep_history_url: str
    explorer_url: str
    legacy_delegation_contract: str
    system_governance_contract: str
    cosigner_url: str
    liquid_staking_contracts: list[str]


CONFIGURATIONS = {
    "mainnet": Configuration(
        chain_id="1",
        proxy_url=ENV_MAINNET_PROXY_URL or DEFAULT_MAINNET_PROXY_URL,
        api_url=ENV_MAINNET_API_URL or DEFAULT_MAINNET_API_URL,
        deep_history_url=ENV_MAINNET_DEEP_HISTORY_URL or DEFAULT_MAINNET_DEEP_HISTORY_URL,
        explorer_url="https://explorer.dharitri.org",
        legacy_delegation_contract="drt1qqqqqqqqqqqqqpgqxwakt2g7u9atsnr03gqcgmhcv38pt7mkd94q8vqld4",
        system_governance_contract="drt1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqrllls7q9tur",
        cosigner_url="https://tools.dharitri.org",
        liquid_staking_contracts=[
            "drt1qqqqqqqqqqqqqpgq2khda0rx207gvlqg92dq5rh0z03a8dqf78sspnhumx",
            "drt1qqqqqqqqqqqqqpgqdnpmeseu3j5t7grds9dfj8ttt70pev66ah0se3prxc",
        ],
    ),
    "devnet": Configuration(
        chain_id="D",
        proxy_url=ENV_DEVNET_PROXY_URL or DEFAULT_DEVNET_PROXY_URL,
        api_url=ENV_DEVNET_API_URL or DEFAULT_DEVNET_API_URL,
        deep_history_url=ENV_DEVNET_DEEP_HISTORY_URL or DEFAULT_DEVNET_DEEP_HISTORY_URL,
        explorer_url="https://devnet-explorer.dharitri.org",
        legacy_delegation_contract="drt1qqqqqqqqqqqqqpgq97wezxw6l7lgg7k9rxvycrz66vn92ksh2tssmj7a6l",
        system_governance_contract="drt1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqrllls7q9tur",
        cosigner_url="https://devnet-tools.dharitri.org",
        liquid_staking_contracts=["drt1qqqqqqqqqqqqqpgqlavy2909f0pa9yf66es5cwh53m0wue28u7hsrelfc5"],
    ),
    "testnet": Configuration(
        chain_id="T",
        proxy_url=ENV_TESTNET_PROXY_URL or DEFAULT_TESTNET_PROXY_URL,
        api_url=ENV_TESTNET_API_URL or DEFAULT_TESTNET_API_URL,
        deep_history_url=ENV_TESTNET_DEEP_HISTORY_URL or DEFAULT_TESTNET_DEEP_HISTORY_URL,
        explorer_url="https://testnet-explorer.dharitri.org",
        legacy_delegation_contract="drt1qqqqqqqqqqqqqpgq97wezxw6l7lgg7k9rxvycrz66vn92ksh2tssmj7a6l",
        system_governance_contract="drt1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqrllls7q9tur",
        cosigner_url="https://testnet-tcs-api.dharitri.org",
        liquid_staking_contracts=[],
    ),
}
