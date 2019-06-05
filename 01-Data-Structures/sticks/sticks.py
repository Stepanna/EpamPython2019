import collections
import operator


def parse_to_python(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_wine:
        lines = []
        lines = file_wine.read()[2:-3]

    js_dicts = []
    raw_content = lines.split('}, {"')
    content = [raw_content[i].split(', "') for i, v in enumerate(raw_content)]
    for i, value in enumerate(content):
        js_dicts.append({})
        for j, string in enumerate(value):
            js_dicts[i].update({string.split('": ')[0].strip('"'):
                                string.split('": ')[1].strip('"')})
    return js_dicts


def multi_replace(data, *subs):
    for sub in subs:
        data = data.replace(*sub)
    return data


def dump_to_json(js_dicts, filename):
    with open(filename, 'w', encoding='utf-8') as out:
        data = str(js_dicts)
        subs = [("[{\'", '[\n{"'), ("\'}]", '"}\n]'), ("\'}, {\'", '"},\n {"'),
                ("\': \'", '": "'), ('\': "', '": "'), ("\', \'", '",\n "'),
                (", \'", ',\n "'), ("\'}, {\'", '"},\n {"'), ('\\\\', '\\'),
                ('},', "\n},"), ("': {'", '": {"'), ("': ", '": '),
                ("'}}", '"}}'), ("['", '["'), ("']", '"]'), ("{'", '{"')]
        data = multi_replace(data, *subs)
        out.write(data)
    return data


def merge_distinct(filedata):
    obj_tuples = []
    for file in filedata:
        obj_tuples.extend([tuple(diction.items()) for diction in file])
    final_list = []
    distinct_obj = set(obj_tuples)
    for s in distinct_obj:
        final_list.append(dict(s))
    return final_list


def price_or_var(sort_data):
    price = sort_data['price']
    if price == 'null':
        return 0, sort_data['variety']
    return int(price), sort_data['variety']


def calc_var_statistic(res_list):
    varieties = ['Gew\\u00fcrztraminer', 'Riesling', 'Merlot',
                 'Madera', 'Tempranillo', 'Red Blend']
    stat_data = ['avg_price', 'min_price', 'max_price',
                 'most_common_country', 'most_common_region', 'average_score']
    wines_stat = dict.fromkeys(varieties)
    for winek in wines_stat.keys():
        wines_stat[winek] = dict.fromkeys(stat_data)

    for wine in wines_stat.keys():
        prices, scores = [], []
        countries, regions = collections.Counter(), collections.Counter()
        for val in res_list:
            if val['variety'] == wine:
                if val['price'] != 'null':
                    prices.append(int(val['price']))
                if val['country'] != 'null':
                    countries[val['country']] += 1
                if val['region_1'] != 'null':
                    regions[val['region_1']] += 1
                if val['region_2'] != 'null':
                    regions[val['region_2']] += 1
                if val['points'] != 'null':
                    scores.append(int(val['points']))

        if prices:
            avg_price = sum(prices)/len(prices)
            min_price = min(prices)
            max_price = max(prices)
            avg_score = sum(scores)/len(scores)
            wines_stat[wine]['avg_price'] = round(avg_price, 2)
            wines_stat[wine]['min_price'] = min_price
            wines_stat[wine]['max_price'] = max_price
            common_country = countries.most_common(1)[0][0]
            wines_stat[wine]['most_common_country'] = common_country
            common_region = regions.most_common(1)[0][0]
            wines_stat[wine]['most_common_region'] = common_region
            wines_stat[wine]['average_score'] = round(avg_score, 2)
    return wines_stat


def price_not_null_max(res_list):
    price = res_list['price']
    if price == 'null':
        return 0
    return int(price)


def price_not_null_min(res_list):
    price = res_list['price']
    if price == 'null':
        return 2500
    return int(price)


def points_not_null_max(res_list):
    points = res_list['points']
    if points == 'null':
        return 0
    return int(points)


def points_not_null_min(res_list):
    points = res_list['points']
    if points == 'null':
        return 2500
    return int(points)


def calc_full_statistic(res_list):
    stats = ['most_expensive_wine', 'cheapest_wine', 'highest_score',
             'lowest_score', 'most_expensive_country', 'cheapest_country',
             'most_rated_country', 'underrated_country',
             'most_active_commentator']
    stat_dict = dict.fromkeys(stats)

    max_price = max(res_list, key=price_not_null_max)['price']
    expens_wines = [max_price]
    expens_wines.extend([wine_dict['title'] for wine_dict in res_list
                         if wine_dict['price'] == max_price])
    stat_dict['most_expensive_wine'] = expens_wines

    min_price = min(res_list, key=price_not_null_min)['price']
    cheap_wines = [min_price]
    cheap_wines.extend([wine_dict['title'] for wine_dict in res_list
                        if wine_dict['price'] == min_price])
    stat_dict['cheapest_wine'] = cheap_wines
    high_score = max(res_list, key=points_not_null_max)['points']
    stat_dict['highest_score'] = high_score
    low_score = min(res_list, key=points_not_null_min)['points']
    stat_dict['lowest_score'] = low_score
    country_prices, country_points = {}, {}

    for wine_dict in res_list:
        if wine_dict['country'] != 'null':
            country_prices[wine_dict['country']] = None
    for key in country_prices.keys():
        prices = []
        for wine_dict in res_list:
            if key == wine_dict['country']:
                if wine_dict['price'] != 'null':
                    prices.append(int(wine_dict['price']))
                else:
                    prices.append(0)
        if prices:
            country_prices[key] = round(sum(prices)/len(prices), 2)
    exp_country = max(country_prices.items(), key=operator.itemgetter(1))[0]
    stat_dict['most_expensive_country'] = exp_country
    cheap_countr = min(country_prices.items(), key=operator.itemgetter(1))[0]
    stat_dict['cheapest_country'] = cheap_countr

    for wine_dict in res_list:
        if wine_dict['country'] != 'null':
            country_points[wine_dict['country']] = None
    for key in country_points.keys():
        prices = []
        for wine_dict in res_list:
            if key == wine_dict['country']:
                if wine_dict['points'] != 'null':
                    prices.append(int(wine_dict['points']))
        country_points[key] = round(sum(prices)/len(prices), 2)
    most_rated = max(country_points.items(), key=operator.itemgetter(1))[0]
    stat_dict['most_rated_country'] = most_rated
    unerrated = min(country_points.items(), key=operator.itemgetter(1))[0]
    stat_dict['underrated_country'] = unerrated

    freq_commrs = collections.defaultdict(int)
    for wine_dict in res_list:
        if wine_dict['taster_name'] != 'null':
            freq_commrs[wine_dict['taster_name']] += 1
    commentator = max(freq_commrs.items(), key=operator.itemgetter(1))[0]
    stat_dict['most_active_commentator'] = commentator
    return stat_dict


def damp_to_md(stat, filename):
    table_head = '| |'
    table_head += str(list(stat['statistics']['wine']['Riesling'].keys()))
    subs = [("', '", '|'), ("['", ''), ("']", ''), ("_", ' '),
            ('avg', 'average'), ("\\u00fc", u"\u00FC")]
    table_head = multi_replace(table_head, *subs)
    table = []
    for key, val in stat['statistics']['wine'].items():
        row = []
        row.append(str(key))
        for k, v in val.items():
            if v is None:
                row.append('-')
            else:
                row.append(str(v))
        table.append('|'.join(row))
    leftow = list(stat['statistics'].keys())[1:]
    rightow = list(stat['statistics'].values())[1:]
    common_stat = str([list(pairs) for pairs in zip(leftow, rightow)])
    subs = [("', '", '\n > * '), ("[['", '* '), ("']], ['", '\n* '),
            ("]], ['", '\n* '), ("', '", ': '),
            ("']]", '\n'), ("'], ['", "\n* "), ("', ['", ' - '),
            ("]], ['", '\n'), ("\\u00e2", u"\u00E2"), ("\\u00e9", u"\u00E9")]
    common_stat = multi_replace(common_stat, *subs)
    with open(filename, 'w', encoding='utf-8') as mdfile:
        mdfile.write('# Statistics\n\n')
        mdfile.write('## Wine\n\n')
        mdfile.write(f'{table_head}\n')
        mdfile.write('-|-|-|-|-|-|-|\n')
        for item in table:
            mdfile.write(f'{item}\n')
        mdfile.write('## Full statistic\n')
        mdfile.write(common_stat)


filenames = ['winedata_1.json', 'winedata_2.json']
filedata = []
for i, fname in enumerate(filenames):
    appendics = parse_to_python(fname)
    filedata.append(sorted(appendics, key=price_or_var, reverse=True))
full_data = merge_distinct(filedata)
dump_to_json(full_data, 'winedata.json')
variety_stat = calc_var_statistic(full_data)
full_stat = calc_full_statistic(full_data)
stats = {'statistics': {'wine': variety_stat, **full_stat}}
dump_to_json(stats, 'stats.json')
damp_to_md(stats, 'stat.md')
