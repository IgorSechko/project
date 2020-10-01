from .models import FormData


FIELDS = FormData._meta.get_fields()


def evaluate(source):                          
    targets = FormData.objects.exclude(id=source.id) # QuerySet Class
    for target in targets:
        print(comapare(source, target))
    


        
    # print("DEBUG: TARGETS' IDS ARE")
    # print(list(targets.values("id")))
    # print("DEBUG: SOURCE'S ID IS")
    # print(source.id)


def comapare(source, target):
    overlap = [False,False,False]
    if source.first_name and target.first_name:
        if source.first_name != target.first_name:
            return False
        else:
            overlap[0] = True
    if source.surname and target.surname:
        if source.surname != target.surname:
            return False
        else:
            overlap[1] = True
    if source.fathername and target.fathername:
        if source.fathername != target.fathername:
            return False
        else:
            overlap[2] = True
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
    return overlap
    
    








    # for field in FIELDS: 
    #     field.value_from_object(source)


