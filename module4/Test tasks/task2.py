from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    result = data

    for filter_function in filters:
        result = filter_function(result)

    result = selector(result)

    return result


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def selector(data):

        result = []

        for row in data:
            new_row = {}

            for col in columns:
                new_row[col] = row[col]

            result.append(new_row)

        return result
    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def filter_data(data):

        result = []

        for row in data:
            if row[column]  in values:
                result.append(row)
        return result
    return filter_data

def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()

