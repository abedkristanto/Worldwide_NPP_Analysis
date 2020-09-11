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
            #print(value, "coordinates is ", coord)
        except (KeyError, wikipedia.exceptions.PageError):
            #print("No wikipedia page named", value)
            new_value = value[:-2] + " NPP"
            #print("Search using keywords:", new_value)
            try:
                coord = wikipedia.page(new_value).coordinates
                #print(new_value, "coordinates is ", coord)
            except (KeyError, wikipedia.exceptions.PageError):
                #print("No wikipedia page named", new_value)
                new_value2 = new_value[:-6] + " NPP"
                #print("Search using keywords:", new_value2)
                try:
                    coord = wikipedia.page(new_value2).coordinates
                    #print(new_value2, "coordinates is ", coord)
                except (KeyError, wikipedia.exceptions.PageError):
                    #print("No wikipedia page named", new_value2)
                    not_found.append(value)
                    coord = (0,0)
        coordinate = [float(coord[0]), float(coord[1])]
        coord_list.append(coordinate)
    return coord_list, not_found