"""
search_engine.py

Search utility to find students, professors, theses, courses.
"""
def simple_search(collection: list, predicate):
    return [item for item in collection if predicate(item)]
