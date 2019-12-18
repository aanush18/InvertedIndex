# InvertedIndex
A simple program called TapSearch using which you may search a word within a set of documents to retrieve the top 10 paragraphs in which the word is present.

## API
TapSearch performs the following functions in the following sequence to get matching documents:

1. preProcessing() - Splits the user submission to index at paragraphs and index each paragraph as a separate document.
2. index() - Generates a mapping of word to paragraph in which the word is present
3. search() - Given a word, search for it and retrieve the top 10 paragraphs (documents) that contain it
4. clear() - Clears indices and document indices
