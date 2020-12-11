from .models import Card, Relation
from django.db.models import Q
import threading
import math
import time


FIELDS = Card._meta.get_fields()

# radius in meters
EARTH_RADIUS_POLAR = 6356800
EARTH_RADIUS_EQUATORIAL = 6378100

RELATION_MATRIX = {
    "Отец/Мать": {
        "Отец/Мать": "родной брат/сестра",
        "Дед/Бабушка": "родной племянник(ца)",
        "Прадед/Прабабушка": "двоюродный внук/внучка",
        "Прапрадед/Прапрабабушка": "двоюродный правнук/правнучка",
    },
    "Дед/Бабушка": {
        "Отец/Мать": "родной дядя/тётя",
        "Дед/Бабушка": "двоюродный брат/сестра",
        "Прадед/Прабабушка": "двоюродный племянник(ца)",
        "Прапрадед/Прапрабабушка": "троюродный внук/внучка",
    },
    "Прадед/Прабабушка": {
        "Отец/Мать": "двоюродный дед/бабушка",
        "Дед/Бабушка": "двоюродный дядя/тётя",
        "Прадед/Прабабушка": "троюродный брат/сестра",
        "Прапрадед/Прапрабабушка": "троюродный племянник(ца)",
    },
    "Прапрадед/Прапрабабушка": {
        "Отец/Мать": "двоюродный прадед/прабабушка",
        "Дед/Бабушка": "троюродный дед/бабушка",
        "Прадед/Прабабушка": "троюродный дядя/тётя",
        "Прапрадед/Прапрабабушка": "4-юродный брат/сестра",
    },
}


def evaluate(src):
    thread = threading.Thread(target=run, args=(src,))
    thread.daemon = False
    thread.start()


def run(source):
    time.sleep(1)
    targets = select_targets(source)
    for target in targets:
        time.sleep(0.04)
        result = comapare(source, target)
        if result:
            print(result)
            relation1 = Relation()
            relation1.referenced_by = source
            relation1.referencing = target
            relation1.similarity = result
            relation1.connection_type = RELATION_MATRIX[source.relation_level][target.relation_level]
            relation1.save()

            relation2 = Relation()
            relation2.referenced_by = target
            relation2.referencing = source
            relation2.similarity = result
            relation2.connection_type = RELATION_MATRIX[target.relation_level][source.relation_level]
            relation2.save()


def select_targets(source):
    Q_obj = form_Q_object(source)
    targets = Card.objects.exclude(
        user=source.user).filter(Q_obj, sex=source.sex)
    return targets


def form_Q_object(source):
    if source.first_name:
        Q_first_name = Q(first_name=source.first_name) | Q(first_name=None)
    else:
        Q_first_name = Q()
    if source.surname:
        Q_surname = Q(surname=source.surname) | Q(surname=None)
    else:
        Q_surname = Q()
    if source.fathername:
        Q_fathername = Q(fathername=source.fathername) | Q(fathername=None)
    else:
        Q_fathername = Q()
    Q_final = Q_first_name & Q_surname & Q_fathername
    return Q_final


def comapare(source, target):
    similarity = 0.0
    if source.first_name and target.first_name:
        if source.first_name != target.first_name:
            return 0  # means False
        else:
            similarity += 0.15
    if source.surname and target.surname:
        if source.surname != target.surname:
            return 0
        else:
            similarity += 0.25
    if source.fathername and target.fathername:
        if source.fathername != target.fathername:
            return 0
        else:
            similarity += 0.15
    if places_bruteforce_comparison(source, target):
        similarity += 0.25
    dates_cmpr_result = dates_comparison(source, target)
    if dates_cmpr_result is False:
        return 0
    else:
        similarity += dates_cmpr_result
    return similarity


def dates_comparison(source, target):
    num = 0.0
    if source.birth_year and target.birth_year:
        if abs(target.birth_year - source.birth_year) < 5:
            num += 0.10
        else:
            return False
    if source.death_year and target.death_year:
        if abs(target.death_year - source.death_year) < 5:
            num += 0.10
        else:
            return False

    return num


def places_bruteforce_comparison(source, target):
    for i in range(1, 4):
        for j in range(1, 4):
            if place_comparison(source, target, i, j):
                return True
    return False


def place_comparison(source, target, i, j):
    if (getattr(source, 'place{}_x'.format(i)) is None) or (getattr(target, 'place{}_x'.format(j)) is None):
        return False
    d_latitude = getattr(source, 'place{}_x'.format(i)) - \
        getattr(target, 'place{}_x'.format(j))
    d_longtitude = getattr(source, 'place{}_y'.format(
        i)) - getattr(target, 'place{}_y'.format(j))
    d_y = EARTH_RADIUS_POLAR*2*math.pi*d_latitude/360
    d_x = EARTH_RADIUS_EQUATORIAL*2*math.pi*d_longtitude/360
    rad_sum = getattr(source, 'place{}_radius'.format(i)) + \
        getattr(target, 'place{}_radius'.format(j))
    if math.sqrt(d_x*d_x + d_y*d_y) < rad_sum:
        return True
    else:
        return False

