def matchingStrings(strings: 'list[str]', queries: 'list[str]'):
    return [strings.count(query) for query in queries ]
    