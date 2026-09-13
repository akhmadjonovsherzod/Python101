from argparse import ArgumentParser
from typing import List, Optional, Sequence
import json as json_lib
import xml.etree.ElementTree as ET

import requests


class UnhandledException(Exception):
    pass


class FeedParseError(Exception):
    """Raised when the given XML cannot be parsed as valid XML."""
    pass


def _get_text(element, tag):
    """Return the text of the first child with this tag, or None if absent."""
    found = element.find(tag)
    return found.text if found is not None else None


def _get_categories(element):
    """Return a list of text values for all <category> children (possibly empty)."""
    return [c.text for c in element.findall("category")]


def _build_data(xml: str, limit: Optional[int] = None) -> dict:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        raise FeedParseError(f"Invalid XML: {e}")

    channel = root.find("channel")
    if channel is None:
        raise FeedParseError("No <channel> element found in feed")

    data = {}
    for tag in (
        "title", "link", "lastBuildDate", "pubDate",
        "language", "managingEditor", "description",
    ):
        value = _get_text(channel, tag)
        if value is not None:
            data[tag] = value

    categories = _get_categories(channel)
    if categories:
        data["category"] = categories

    items = channel.findall("item")
    if limit is not None:
        items = items[:limit]

    parsed_items = []
    for item in items:
        item_data = {}
        for tag in ("title", "author", "pubDate", "link", "description"):
            value = _get_text(item, tag)
            if value is not None:
                item_data[tag] = value

        item_categories = _get_categories(item)
        if item_categories:
            item_data["category"] = item_categories

        parsed_items.append(item_data)

    if parsed_items:
        data["items"] = parsed_items

    return data


def _format_console(data: dict) -> List[str]:
    lines = []

    if "title" in data:
        lines.append(f"Feed: {data['title']}")
    if "link" in data:
        lines.append(f"Link: {data['link']}")
    if "lastBuildDate" in data:
        lines.append(f"Last Build Date: {data['lastBuildDate']}")
    if "pubDate" in data:
        lines.append(f"Publish Date: {data['pubDate']}")
    if "language" in data:
        lines.append(f"Language: {data['language']}")
    if "category" in data:
        lines.append(f"Categories: {', '.join(data['category'])}")
    if "managingEditor" in data:
        lines.append(f"Editor: {data['managingEditor']}")
    if "description" in data:
        lines.append(f"Description: {data['description']}")

    for item in data.get("items", []):
        lines.append("")
        if "title" in item:
            lines.append(f"Title: {item['title']}")
        if "author" in item:
            lines.append(f"Author: {item['author']}")
        if "pubDate" in item:
            lines.append(f"Published: {item['pubDate']}")
        if "link" in item:
            lines.append(f"Link: {item['link']}")
        if "category" in item:
            lines.append(f"Categories: {', '.join(item['category'])}")
        if "description" in item:
            lines.append("")
            lines.append(item["description"])

    return lines


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.
    """
    data = _build_data(xml, limit)

    if json:
        return json_lib.dumps(data, indent=2, ensure_ascii=False).split("\n")

    return _format_console(data)


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)

    try:
        xml = requests.get(args.source).text
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()