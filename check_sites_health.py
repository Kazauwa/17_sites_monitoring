import requests
from argparse import ArgumentParser
from whois import whois
from datetime import timedelta, datetime


def load_urls4check(path):
    with open(path, 'r') as reader:
        urls = reader.read().splitlines()
        return urls


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code == 200


def has_domain_been_prepaid(expiration_date, delta_days):
    now = datetime.now()
    return (expiration_date - now) > timedelta(days=delta_days)


def get_expiration_date(domain):
    expiration_date = whois(url).expiration_date
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[0]
    return expiration_date


def check_site_health(url, **kwargs):
    expiration_date = get_expiration_date(url)
    result = {
        'url': url,
        'is_avaliable': is_server_respond_with_200(url),
        'is_prepaid': has_domain_been_prepaid(expiration_date, kwargs['prepaid_delta'])
    }
    return result


def output_result_to_console(results):
    print('\nDomain: %s' % results['url'])
    print('Responds with 200: %s' % results['is_avaliable'])
    print('Prepaid in advance: %s' % results['is_prepaid'])


if __name__ == '__main__':
    parser = ArgumentParser(description='Check avaliability of give urls')
    parser.add_argument('-i', '--input_file', type=str, nargs='?', required=True, dest='input_file',
                        help='Path to .txt file with urls to check')
    parser.add_argument('-d', '--prepaid_delta', type=int, nargs='?', default=30,
                        help='Minimal number of days to be prepaid in advance for domain. Default is 30 days.')
    options = parser.parse_args()

    urls = load_urls4check(options.input_file)
    for url in urls:
        result = check_site_health(url, prepaid_delta=options.prepaid_delta)
        output_result_to_console(result)
