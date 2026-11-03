def search_by_title(dvds, keyword):
    """Return DVDs whose title contains the given keyword."""
    return [dvd for dvd in dvds if keyword in dvd.title]
