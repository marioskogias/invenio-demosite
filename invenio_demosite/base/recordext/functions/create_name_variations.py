def create_name_variations(author):
    """
    Add a new field 'name_variations' in the author dict

    @param the dictionary representing the author
    @return the enhanced dictionary
    """
    from invenio.modules.indexer.tokenizers.BibIndexAuthorTokenizer import \
            BibIndexAuthorTokenizer
    author_tokenizer = BibIndexAuthorTokenizer()
    name = author['full_name']
    value = author_tokenizer.tokenize_for_fuzzy_authors(name)
    return value
