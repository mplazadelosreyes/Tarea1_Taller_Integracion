from django.shortcuts import render
import requests
#from django.template import loader

# https://github.com/curiousrohan/ramapi/blob/master/ramapi/ramapi.py
base_url = "https://rickandmortyapi.com/api/"
episode_url = base_url+"episode/"
character_url = base_url+"character/"
location_url = base_url+"location/"


def index(request):
    r = requests.get(episode_url).json()
    episodios = []
    while True:
        # print(r['info'])
        for todo_item in r['results']:
            dicc = {'id': todo_item['id'],
                    'name': todo_item['name'],
                    'air_date': todo_item['air_date'],
                    'episode': todo_item['episode']}
            episodios.append(dicc)
            # print('{} {} {}'.format(todo_item['name'], todo_item['air_date'],
            #  todo_item['episode']))
        next_url = r['info']['next']
        if next_url == '':
            break
        r = requests.get(next_url).json()
    # print(episodios)
    # print(r['results'])
    context = {'all_episodes': episodios}
    return render(request, 't1/index.html', context)


def episode(request, episode_id):
    url = episode_url + '{}'.format(episode_id)
    # print(url)
    r = requests.get(url).json()
    # name, air_date, episode, characters
    info_episodio = [
        {'name': r['name'], 'air_date': r['air_date'], 'episode': r['episode']}]
    list_characters = r['characters']
    for elem in list_characters:
        r2 = requests.get(elem).json()
        dicc_characters = {'id': r2['id'], 'name': r2['name']}
        info_episodio.append(dicc_characters)
    #print(info_episodio)
    context = {'info_episode': info_episodio}
    return render(request, 't1/episode.html', context)


def character(request, character_id):
    url = character_url + '{}'.format(character_id)
    r = requests.get(url).json()
    info_character = []
    if r['type'] == '':
        info_character = [{'name': r['name'], 'status': r['status'], 'species':
            r['species'], 'type': 'Not type', 'gender': r['gender']}]
    if r['type'] != '':
        info_character = [
            {'name': r['name'], 'status': r['status'], 'species': r['species'],
             'type': r['type'], 'gender': r['gender']}]
    if r['origin']['name'] == 'unknown':
        dicc_origin = {'origin': 'unknown'}
        info_character.append(dicc_origin)
    if r['origin']['name'] != 'unknown':
        get_id = (r['origin']['url']).split('/')
        id = int(get_id[-1])
        dicc_origin = {'origin': r['origin']['name'], 'id': id}
        info_character.append(dicc_origin)
    if r['location']['name'] == 'unknown':
        dicc_location = {'location': 'unknown'}
        info_character.append(dicc_location)
    if r['location']['name'] != 'unknown':
        get_id = (r['location']['url']).split('/')
        id = int(get_id[-1])
        dicc_location = {'location': r['location']['name'], 'id': id}
        info_character.append(dicc_location)
    for e in r['episode']:
        r_episode = requests.get(e).json()
        dicc_episode = {'episode': r_episode['name'], 'id': r_episode['id']}
        info_character.append(dicc_episode)
    # diccionario imagen
    dicc_image = {'image': r['image']}
    info_character.append(dicc_image)
    #print(info_character)
    context = {'info_character': info_character}
    return render(request, 't1/character.html', context)


def location(request, location_id):
    url = location_url + '{}'.format(location_id)
    r = requests.get(url).json()
    info_location = [
        {'name': r['name'], 'type': r['type'], 'dimension': r['dimension']}]
    for elem in r['residents']:
        r_char = requests.get(elem).json()
        dicc_char = {'resident': r_char['name'], 'id': r_char['id']}
        info_location.append(dicc_char)
    context = {'info_location': info_location}
    return render(request, 't1/location.html', context)


def search(request):
    if request.method == 'GET':
        name = request.GET.get('search', None)
    # busqueda
    # personajes
    search_character_url = "https://rickandmortyapi.com/api/character/?name={}".format(name)
    r_char = requests.get(search_character_url).json()
    info_busqueda = []
    # print(r_char)
    if 'error' in r_char.keys():
        pass
    else:
        while True:
            for todo_item in r_char['results']:
                dicc = {'id': todo_item['id'],
                        'character': todo_item['name']}
                info_busqueda.append(dicc)
            next_url = r_char['info']['next']
            if next_url == '':
                break
            r_char = requests.get(next_url).json()
    # episodios
    search_episode_url = "https://rickandmortyapi.com/api/episode/?name={}".format(name)
    r_ep = requests.get(search_episode_url).json()
    if 'error' in r_ep.keys():
        pass
    else:
        while True:
            for todo_item in r_ep['results']:
                dicc = {'id': todo_item['id'],
                        'episode': todo_item['name']}
                info_busqueda.append(dicc)
            next_url = r_char['info']['next']
            if next_url == '':
                break
            r_ep = requests.get(next_url).json()
    # location
    search_location_url = "https://rickandmortyapi.com/api/location/?name={}".format(name)
    r_loc = requests.get(search_location_url).json()
    # print(r_loc)
    if 'error' in r_loc.keys():
        pass
    else:
        while True:
            for todo_item in r_loc['results']:
                dicc = {'id': todo_item['id'],
                        'location': todo_item['name']}
                info_busqueda.append(dicc)
            next_url = r_loc['info']['next']
            if next_url == '':
                break
            r_loc = requests.get(next_url).json()
    #print(info_busqueda)
    context = {'search_result': info_busqueda}
    return render(request, 't1/search.html', context)



