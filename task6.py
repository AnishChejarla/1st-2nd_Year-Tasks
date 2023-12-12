import requests

def get_block_transactions(block_hash):
    api_key = '' 
    url = f'https://api.etherscan.io/api?module=proxy&action=eth_getBlockByHash&tag={block_hash}&boolean=true&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == '1':
        return data['result']['transactions']
    else:
        return []

def append_to_text_file(transactions, file_path):
    with open(file_path, 'a') as file:
        for transaction in transactions:
            file.write(str(transaction) + '\n')

def print_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

def main():
    block_hash = '0x8770370795abd425663700458f73ab62e879161d20e5ab87c6d0bb24b6552fe3' 
    transactions = get_block_transactions(block_hash)
    file_path = 'block_transactions.txt'
    append_to_text_file(transactions, file_path)
    print_file_content(file_path)
main()