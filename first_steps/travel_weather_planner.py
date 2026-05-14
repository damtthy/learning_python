distance_mi = 7
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)


# --- Versión Optimizada (Generada por IA, referencia practica) ---

# if not distance_mi:
#     print(False)

# elif distance_mi <= 1:
#     # Si la distancia es corta, el resultado depende de si NO llueve
#     print(not is_raining)

# elif 1 < distance_mi <= 6:
#     # Distancia media: Necesitas bici Y que no llueva
#     print(has_bike and not is_raining)

# else:
#     # Distancia larga ( > 6): Auto o App de transporte
#     print(has_car or has_ride_share_app)