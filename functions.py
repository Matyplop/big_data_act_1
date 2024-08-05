import pandas as pd
import streamlit as st


def agregar_campeon(nombre, rol, vida_base, mana_base, armadura_base, daño_ataque_base, oro):

    encabezado = ["Nombre", "Rol", "Vida base",
                  "Mana base", "Armadura base", "Daño ataque base", "Eficiencia de Oro"]

    df = pd.read_csv("../champions.csv", names=encabezado, skiprows=1)
    campeon = pd.DataFrame({
        'Nombre': [nombre],
        'Rol': [rol],
        'Vida base': [vida_base],
        'Mana base': [mana_base],
        'Armadura base': [armadura_base],
        'Daño ataque base': [daño_ataque_base],
        'Eficiencia de Oro': [oro],
    })
    # aqui lo que quiero hacer es añadir lo de arriba al dataframe original , pero el append no funciona entonces uso el concat
    df2 = pd.concat([df, campeon], ignore_index=True)
    return df2


def buscar_campeon(selected_type, data):
    encabezado = ["Nombre", "Rol", "Vida base",
                  "Mana base", "Armadura base", "Daño ataque base", "Eficiencia de Oro"]

    df = pd.read_csv("../champions.csv", names=encabezado, skiprows=1)
    if type(data) is not str:
        resultados = df[df[selected_type] == data]
    else:
        resultados = df[df[selected_type].str.contains(
            data, case=False, na=False)]

    if not resultados.empty:
        print(f"Se encontraron {len(resultados)} resultados:")
        print(resultados)
    else:
        print("No se encontró el Campeón.")

    return resultados


# def modificar_campeon(selected_type,nombre_original):
    # encabezado = ["Nombre", "Rol", "Vida base",
    #               "Mana base", "Armadura base", "Daño ataque base", "Eficiencia de Oro"]
    #
    # df = pd.read_csv("../champions.csv", names=encabezado, skiprows=1)
    #
    # campeon_existente = df[df[selected_type].str.contains(
    #     nombre_original, case=False, na=False)]
    #
    # if campeon_existente.empty:
    #     print(f"No se encontró el Campeón '{nombre_original}'.")
    #     return
    #
    # return campeon_existente
    #
    # if nuevo_nombre:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Nombre'] = nuevo_nombre
    # if nuevo_rol:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Rol'] = nuevo_rol
    # if nuevo_hp:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Vida base'] = nuevo_hp
    # if nuevo_ap:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Mana base'] = nuevo_ap
    # if nuevo_armor:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Armadura base'] = nuevo_armor
    # if nuevo_attack:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Daño ataque base'] = nuevo_attack
    #
    # if nuevo_Oro:
    #     df.loc[df['Nombre'].str.contains(
    #         nombre_original, case=False, na=False), 'Oro'] = nuevo_Oro
