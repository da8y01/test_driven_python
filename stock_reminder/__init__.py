if __name__ == "__main__":
    import doctest
#    doctest.testmod()
#   # doctest: +ELLIPSIS
#   # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    doctest.testfile("readme.txt", verbose=True, optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)
    #doctest.testfile("readme.txt")