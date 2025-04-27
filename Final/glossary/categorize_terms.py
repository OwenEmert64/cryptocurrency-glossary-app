from glossary.models import Term

def auto_categorize_terms():
    for term in Term.objects.all():
        text = (term.term + " " + term.definition).lower()

        if any(word in text for word in ['bitcoin', 'altcoin', 'fiat', 'wallet', 'ledger', 'public key', 'private key', 'web3']):
            term.category = 'Basics'
        elif any(word in text for word in ['blockchain', 'block', 'node', 'hash', 'hashrate', 'consensus mechanism', 'genesis block', 'smart contract', 'mining', 'validator', 'sharding', 'sidechain', 'snapshot']):
            term.category = 'Blockchain Concepts'
        elif any(word in text for word in ['dex', 'defi', 'yield farming', 'tvl', 'flash loan', 'impermanent loss', 'liquidity pool', 'liquidity', 'market cap', 'slippage', 'pump and dump', 'rug pull', 'presale', 'synthetic asset', 'yield aggregator', 'watchlist']):
            term.category = 'Trading/DeFi'
        elif any(word in text for word in ['cold wallet', 'hot wallet', 'multisig wallet', 'dusting attack', 'escrow', 'kyc', 'time-lock', 'oracles', 'scamcoin', 'security token', 'tor']):
            term.category = 'Security'
        elif any(word in text for word in ['token', 'nft', 'rebase token', 'wrapped token', 'utility token']):
            term.category = 'Tokens/NFTs'
        elif any(word in text for word in ['layer 1', 'layer 2', 'lightning network', 'zk-rollup', 'zero-knowledge proof']):
            term.category = 'Scaling/Layer 2'
        elif any(word in text for word in ['airdrop', 'ico', 'ieo', 'daico', 'degen', 'fomo', 'fud', 'whale', 'rekt', 'hodl', 'shill', 'whitelisting', 'moon']):
            term.category = 'Events/Behavior'
        elif any(word in text for word in ['mev', 'merkle tree', 'nonce', 'proof of stake', 'proof of work', 'stablecoin', 'vesting']):
            term.category = 'Advanced Crypto Terms'
        else:
            term.category = 'Misc'

        term.save()

    print("✅ Auto-categorization complete!")
