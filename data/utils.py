import json
from sys import stderr


def upload_json(json_path):
    json_content = []
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            json_content = json.load(json_file)
    except FileNotFoundError:
        stderr.write(f"failed to find {json_path}.\n")
    except json.JSONDecodeError:
        stderr.write(f"failed to decode {json_path}.\n")
    return json_content


# def download_json(json_path, json_content):
#     with open(json_path, 'w') as json_file:
#         json.dump(json_content, json_file, indent=2, ensure_ascii=False)
#
#
# def main():
#     users = upload_json('users.json')
#     offers = upload_json('offers.json')
#     orders = upload_json('orders.json')
#
#
# if __name__ == '__main__':
#     main()
