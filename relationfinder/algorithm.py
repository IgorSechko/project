from .models import FormData, Relation
import threading
import math


FIELDS = FormData._meta.get_fields()

# radius in meters
EARTH_RADIUS_POLAR = 6356800
EARTH_RADIUS_EQUATORIAL = 6378100


def evaluate(src):
    thread = threading.Thread(target=run, args=(src,))
    thread.daemon = True
    thread.start()


def run(source):
    targets = FormData.objects.exclude(user=source.user)  # QuerySet Class
    for target in targets:
        result = comapare(source, target)
        if result:
            relation = Relation()
            relation.found_by = source
            relation.reference_to = target
            relation.similarity = result
            relation.save()


def comapare(source, target):
    overlap = 0.0
    if source.first_name and target.first_name:
        if source.first_name != target.first_name:
            return 0  # means False
        else:
            overlap += 0.15
    if source.surname and target.surname:
        if source.surname != target.surname:
            return 0
        else:
            overlap += 0.25
    if source.fathername and target.fathername:
        if source.fathername != target.fathername:
            return 0
        else:
            overlap += 0.15
    if places_bruteforce_comparison(source, target):
        overlap += 0.20
    return overlap


def places_bruteforce_comparison(source, target):
    for i in range(1, 4):
        for j in range(1, 4):
            if place_comparison(source, target, i, j):
                return True
    return False


def place_comparison(source, target, i, j):
    d_latitude = getattr(source, 'place{}_x'.format(i)) - getattr(target, 'place{}_x'.format(j))
    d_longtitude = getattr(source, 'place{}_y'.format(i)) - getattr(target, 'place{}_y'.format(j))
    d_y = EARTH_RADIUS_POLAR*2*math.pi*d_latitude/360
    d_x = EARTH_RADIUS_EQUATORIAL*2*math.pi*d_longtitude/360
    rad_sum = getattr(source, 'place{}_radius'.format(i)) + getattr(target, 'place{}_radius'.format(j))
    if math.sqrt(d_x*d_x + d_y*d_y) < rad_sum:
        return True
    else:
        return False

    # if source.birth_year and target.birth_year:
    #     if source.birth_year != target.birth_year:
    #         return False
    #     else:
    #         overlap[3] = True
    # if source.death_year and target.death_year:
    #     if source.death_year != target.death_year:
    #         return False
    #     else:
    #         overlap[4] = True

    # for field in FIELDS:
    #     field.value_from_object(source)
