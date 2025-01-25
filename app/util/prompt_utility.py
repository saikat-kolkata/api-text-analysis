
def system_message_named_entity():
    labels = [
    "person",      # people, including fictional characters
    "org",         # organizations, companies, agencies, institutions
    "gpe",         # geopolitical entities like countries, cities, states
    "loc",         # non-gpe locations
    "product",     # vehicles, foods, appareal, appliances, software, toys 
    "event",       # named sports, scientific milestones, historical events
    "work_of_art", # titles of books, songs, movies
    "language",    # any named language
    "date",        # absolute or relative dates or periods
    "time"        # time units smaller than a day
    ]
    return f"""
    You are an expert in Natural Language Processing. Your task is to identify common Named Entities (NER) in a given text.
    The possible common Named Entities (NER) types are exclusively: ({", ".join(labels)})."""

def assisstant_message():
    return """
    EXAMPLE:
    Text: 'In Germany, in 1440, goldsmith Johannes Gutenberg invented the movable-type printing press. His work led to an information revolution and the unprecedented mass-spread / 
    of literature throughout Europe. Modelled on the design of the existing screw presses, a single Renaissance movable-type printing press could produce up to 3,600 pages per workday.'
    {{
        "gpe": ["Germany", "Europe"],
        "date": ["1440"],
        "person": ["Johannes Gutenberg"],
        "product": ["movable-type printing press"],
        "event": ["Renaissance"],
        "quantity": ["3,600 pages"],
        "time": ["workday"]
    }}
    """