# Domains Hunter
## The project is designed to get domains from reg.ru
## Selecting a domain name by keywords (.ru, .su, .org, .info):
### Method of the DomainsHunter .search_keyword class:
##### Arguments:
+ keyword - the main keyword, for example, "home" or "domain". Required field.
+ category - (=False - search_trends, =True - all) the category of names to be selected. 'search_trends' — search trends, 'all' — everything.
### Example:
```python
from DomainsHunter import DomainsHunter as dh

results = dh.search_keyword("testdomainsearch", category=False)
print(results)
```
### Out:
```python
['Testdomainsearch.ru', 'Testdomainsearch.su', 'Testdomainsearch.org', 'Testdomainsearch.info']
```

## List of exempt domains:
### Method of the DomainsHunter .get_deleted class:
##### Arguments:
+ date - date of domain deletion, starting from which to include domains in the resulting list. Date format: 'YYYY-MM-DD'. By default, it is equal to the last date of domain deletion.
+ pr - it is Yandex TIC (pr>=yandex_tic) or Google PR (pr>=google_pr)
+ len_domain - domain length (3<=len_domain)
### Example:
```python
from DomainsHunter import DomainsHunter as dh

results = dh.get_deleted(date="2022-05-05", pr=1000, len_domain=7)
print(results)
```
### Out:
```python
[{'date_delete': '2022-05-06', 'domain_name': 'calls24.ru', 'first_create_date': '2009-04-03', 'google_pr': 0, 'registered': 'NOT REGISTERED', 'yandex_tic': 1800},
 {'date_delete': '2022-05-06', 'domain_name': 'soviki.ru', 'first_create_date': '2011-04-04', 'google_pr': 0, 'registered': 'NOT REGISTERED', 'yandex_tic': 3000}]
```
## Checking the availability of the domain:
### Method of the DomainsHunter .check_availability class:
##### Arguments:
+ domains - list of domains to check
### Example:
```python
from DomainsHunter import DomainsHunter as dh

results = dh.check_availability(["itistestdomain.ru", "itisjusttestdomain.org"])
print(results)
```
### Out:
```python
['itistestdomain.ru', 'itisjusttestdomain.org']
```
If the output is not empty, then the domains are free.