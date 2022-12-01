
"""
Let's assume that the names of the three tables are as follows:
# Before model/table name is Animal(zero)
# After model/table names are AnimalPart1 and AnimalPart2


# BEFORE:
tblZero: id | name | type name | qty
1 | one | cat | 2
2| two | cat | 7
3 | three | dog | 4
4 | four | cat | 8
5 | five | dog | 1
6 | six | fish | 2


# AFTER:
tblTwo: typeID | typeName
1 | cat
2 | dog
3 | fish


tblOne: id | name | typeID | qty
1 | one | 1 | 2
2| two | 1 | 7
3 | three | 2 | 4
4 | four | 1 | 8
5 | five | 2 | 1
6 | six | 3 | 2

"""

def migrate_old_data_to_a_new(request):
    # getting Table Zero data
    table_zero_queryset = Animal.objects.all()

    unique_type_names_list = list(set(Animal.objects.all().values_list('type_name', flat=True)))

    for instance in table_zero_queryset:

        # creating objects in table Two
        for unique_type_name in unique_type_names_list:
            AnimalPart2.objects.get_or_create(typeID=unique_type_names_list.index(unique_type_name) + 1, typeName=unique_type_name)

        type_instance = AnimalPart2.objects.get(typeName=instance.type_name)

        # creating objects in table one
        AnimalPart1.objects.get_or_create(id=instance.id, name=instance.name, typeID=type_instance.typeID, qty=instance.qty)

    return HttpResponse("Some Response")
    