def wiki_get_coordinates(places_list):
    '''
    Get location coordinate of places in a list
    Args:
        places_list: string list of places

    Return:
        coord_list: list of coordinates of the inputted places
        not_found: list of places without wikipedia page available 
    '''
    import wikipedia
    coord_list = []
    not_found = []
    for n, value in enumerate(places_list):
        try:
            coord = wikipedia.page(value).coordinates
            keywords = value
            #print(value + " NPP", "coordinates is ", coord)
        except (KeyError, wikipedia.exceptions.PageError,
        wikipedia.exceptions.DisambiguationError):
            #print("No wikipedia page named", value)
            new_value = value + " Nuclear Power Plant"
            #print("Search using keywords:", new_value)
            try:
                coord = wikipedia.page(new_value).coordinates
                keywords = new_value
                #print(new_value, "coordinates is ", coord)
            except (KeyError, wikipedia.exceptions.PageError,
            wikipedia.exceptions.DisambiguationError):
                #print("No wikipedia page named", new_value)
                new_value2 = value[:-2] + " NPP"
                #print("Search using keywords:", new_value2)
                try:
                    coord = wikipedia.page(new_value2).coordinates
                    keywords = new_value2
                    #print(new_value2, "coordinates is ", coord)
                except (KeyError, wikipedia.exceptions.PageError,
                wikipedia.exceptions.DisambiguationError):
                    #print("No wikipedia page named", new_value2)
                    new_value3 = new_value2[:-4] + " Nuclear Power Plant"
                    #print("Search using keywords:", new_value3)
                    try:
                        coord = wikipedia.page(new_value3).coordinates
                        keywords = new_value3
                        #print(new_value3, "coordinates is ", coord)
                    except (KeyError, wikipedia.exceptions.PageError,
                    wikipedia.exceptions.DisambiguationError):
                        #print("No wikipedia page named", new_value3)
                        new_value4 = new_value2[:-6] + " NPP"
                        #print("Search using keywords:", new_value4)
                        try:
                            coord = wikipedia.page(new_value3).coordinates
                            keywords = new_value3
                            #print(new_value3, "coordinates is ", coord)
                        except (KeyError, wikipedia.exceptions.PageError,
                        wikipedia.exceptions.DisambiguationError):
                            #print("No wikipedia page named", new_value3)
                            new_value5 = new_value2[:-6] + " Nuclear Power Plant"
                            #print("Search using keywords:", new_value5)
                            try:
                                coord = wikipedia.page(new_value5).coordinates
                                keywords = new_value5
                                #print(new_value5, "coordinates is ", coord)
                            except (KeyError, wikipedia.exceptions.PageError,
                            wikipedia.exceptions.DisambiguationError):
                                #print("No wikipedia page named", new_value5)
                                not_found.append(value)
                                keywords = value
                                coord = (0,0)
        coordinate = [keywords, float(coord[0]), float(coord[1])]
        coord_list.append(coordinate)
    return coord_list, not_found