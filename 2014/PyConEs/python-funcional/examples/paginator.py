from functools import reduce
from operator import add

def linkify_element(element):
    if isinstance(element, int):
        return "<li><a href=\"/page/{0}\">{0}</a></li>".format(element)
    else:
        return "<li>{0}</li>".format(element)

def linkify_formater(pages_list):
    pages_links = map(linkify_element, pages_list)
    return reduce(lambda x, y: x + "\n" + y, pages_links)


def shell_formater(pages_list):
    pages_strings = map(str, pages_list)
    return reduce(lambda x, y: x + " | " + y, pages_strings)


def dotter(current_list, element):
    if len(current_list) > 0 and element - current_list[-1] > 1:
        return current_list + ["...", element]
    return current_list + [element]


def paginator(pages, current, formater=linkify_formater):
    pages_list = range(1, pages + 1)
    if pages >= 10:
        pages_list = list(pages_list[0:3]) + list(pages_list[current-2:current+1]) + list(pages_list[-3:])
        pages_list = set(pages_list)
        pages_list = filter(lambda x: x >= 0, pages_list)
        pages_list = filter(lambda x: x < pages + 1, pages_list)
        pages_list = reduce(dotter, pages_list, [])

    return formater(pages_list)

if __name__ == "__main__":
    print(paginator(15, 7))
    print(paginator(15, 7, shell_formater))
