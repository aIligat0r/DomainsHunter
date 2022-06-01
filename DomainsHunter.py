import configparser
from re import match

from requests import get


CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")


class DomainsHunter:
    @staticmethod
    def search_keyword(keyword: str, category=True) -> list:
        if category is False:
            category = "&category=search_trends"
        else:
            category = "&category=all"

        response = get(
            f"https://api.reg.ru/api/regru2/domain/get_suggest?output_content_type=plain&use_hyphen=0"
            f"&username={CONFIG['regru_public_creds']['username']}&password={CONFIG['regru_public_creds']['username']}&word={keyword}" + category
        ).json()
        out_data = []
        for domain in response['answer']['suggestions']:
            for tld in domain['avail_in']:
                out_data.append(f"{domain['name']}.{tld}")
        return out_data

    @staticmethod
    def get_deleted(date: str = "", pr=None, len_domain=None) -> list:
        if date:
            assert match(r"^\d\d\d\d-\d\d-\d\d$", date)
            date = f"&deleted_from={date}"

        response = get(
            f"https://api.reg.ru/api/regru2/domain/get_deleted?password={CONFIG['regru_public_creds']['username']}&username={CONFIG['regru_public_creds']['password']}&hidereg=1" + date
        ).json()
        out_data = []
        for domain in response['answer']['domains']:
            if pr is not None or pr is not None:
                if domain['google_pr'] >= pr or domain['yandex_tic'] >= pr:
                    if len_domain is not None:
                        if len(domain['domain_name'].split(".")[0]) <= len_domain:
                            out_data.append(domain)
                    else:
                        out_data.append(domain)
            else:
                if len_domain is not None:
                    if len(domain['domain_name'].split(".")[0]) <= len_domain:
                        out_data.append(domain)
                else:
                    out_data.append(domain)
        return out_data

    @staticmethod
    def deleted_keyword(date: str, keyword: str) -> list:
        assert match(r"^\d\d\d\d-\d\d-\d\d$", date)

        get_deleted = DomainsHunter.get_deleted(date)
        out = []
        for domain in get_deleted:
            if domain['domain_name'].find(keyword) != -1:
                out.append(domain['domain_name'])
        return out

    @staticmethod
    def check_availability(domains: list) -> list:
        assert isinstance(domains, list)

        domains_list = [
            {'dname': domain} for domain in domains
        ]
        domains_list = str(domains_list).replace("'", '"')
        response = get(
            'https://api.reg.ru/api/regru2/domain/check?input_data={"domains":'
            + domains_list + "}&input_format=json" + f"&password={CONFIG['regru_public_creds']['password']}&username={CONFIG['regru_public_creds']['username']}"
        ).json()
        out_data = []
        for domain in response['answer']['domains']:
            if domain['result'] == "Available":
                out_data.append(domain['dname'])
        return out_data
