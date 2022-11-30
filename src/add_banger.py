from src.service import update_json_bollocks

print("what type of banger do u want to add?\n- tune\n- film")
type = input()


if type == "film":
    print("film name?")
    name = input()

    print("link?")
    link = input()

    print("on netflix?")
    on_netflix = input()

    print("on prime?")
    on_prime = input()

    update_json_bollocks(file_path="../data/films.json",
                         args={"name": name,
                               "link": link,
                               "on_netflix": on_netflix,
                               "on_prime": on_prime},
                         key="films")

elif type == "tune":
    print("tune name?")
    name = input()

    print("artist?")
    artist = input()

    print("link?")
    link = input()

    update_json_bollocks(file_path="../data/tunes.json",
                         args={"name": name,
                               "artist": artist,
                               "link": link},
                         key="tunes")

else:
    raise Exception("invalid input bud")