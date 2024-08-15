import streamlit as st
from functions import agregar_campeon, buscar_campeon
import pandas as pd
encabezado = ["Nombre", "Rol", "Vida base",
              "Mana base", "Armadura base", "Daño ataque base", "Eficiencia de Oro"]

roles_disponibles = ['Support', 'Mid', 'ADC', 'Jungle', 'Top']


logo = st.sidebar.image("./logito.png", width=200)


df = pd.read_csv('champions.csv', names=encabezado, skiprows=1)

st.page_link("champions.py", label="Home", icon="🏠")



st.write("### Bienvenido a la base de datos de campeones de LoL")
options = ['Selecciona una opción', 'Ingresar nuevo campeón',
           'Filtrar por datos', 'Modificar campeón existente']
selected = st.sidebar.selectbox(
    '¿Que acción desea realizar?', options)

if selected == options[0]:
    df
if selected == options[1]:
    df_show = st.dataframe(df)
    valor_predeterminado_vida = 100  # un valor cualquiera
    with st.sidebar.form(key='my_form'):

        Nombre = st.text_input(

            "Ingresa nombre",
        )
        Rol = st.selectbox(
            "Rol", roles_disponibles)

        Vida_base = st.number_input(
            "Vida base", value=float(valor_predeterminado_vida)
        )

        Mana_base = st.number_input(
            "Mana base", value=float(valor_predeterminado_vida)
        )

        Armadura_base = st.number_input(
            "Armadura base", value=float(valor_predeterminado_vida)
        )

        Daño_ataque_base = st.number_input(
            "daño de ataque base ", value=float(valor_predeterminado_vida)
        )

        Eficiencia_de_oro = st.number_input(
            "Eficiencia de oro", value=float(valor_predeterminado_vida)
        )
        submit_button = st.form_submit_button(label='Agregar')
    if submit_button:
        df2 = agregar_campeon(Nombre, Rol, Vida_base, Mana_base,
                              Armadura_base, Daño_ataque_base, Eficiencia_de_oro)
        df2.to_csv('champions.csv', mode='w', index=False)
        df_show.empty()
        df2

elif selected == options[2]:
    selected_type = st.sidebar.selectbox(
        'Seleccione tipo de dato', encabezado)
    with st.sidebar.form(key='my_form'):
        if (selected_type == encabezado[0] or selected_type == encabezado[1]):
            data = st.text_input(
                "Ingrese parametro de busqueda",
            )
        else:
            data = st.number_input(
                "Ingrese parametro de busqueda",
            )

        submit_button2 = st.form_submit_button(label='Aceptar')
    if submit_button2:
        if selected_type == encabezado[6]:
            data = float(data)
        elif selected_type != encabezado[0] and selected_type != encabezado[1]:
            data = int(data)
        df3 = buscar_campeon(selected_type, data)
        df3

elif selected == options[3]:
    seleccionar_campeon = st.sidebar.selectbox(
        "Selecciona Campeón a modificar", df["Nombre"])
    with st.sidebar.form(key='my_form'):
        if seleccionar_campeon:
            champion_data = df[df['Nombre'] == seleccionar_campeon].iloc[0]
            rol = st.selectbox(
                "Rol", roles_disponibles, index=roles_disponibles.index(champion_data["Rol"]))
            vida_base = st.number_input(
                "Vida base", value=float(champion_data["Vida base"]))
            mana_base = st.number_input(
                "Mana base", value=float(champion_data["Mana base"]))
            armadura_base = st.number_input(
                "Armadura base", value=float(champion_data["Armadura base"]))
            dano_ataque_base = st.number_input(
                "Daño ataque base", value=float(champion_data["Daño ataque base"]))
            eficiencia_oro = st.number_input(
                "Eficiencia de Oro", value=float(champion_data["Eficiencia de Oro"]))
            submit_button3 = st.form_submit_button(label='Guardar cambios')

        if submit_button3:
            with st.spinner("Generando cambios.."):
                st.balloons()

            df.loc[df['Nombre'] == seleccionar_campeon,
                   'Vida base'] = vida_base
            df.loc[df['Nombre'] == seleccionar_campeon,
                   'Rol'] = rol
            df.loc[df['Nombre'] == seleccionar_campeon,
                   'Mana base'] = mana_base
            df.loc[df['Nombre'] == seleccionar_campeon,
                   'Armadura base'] = armadura_base
            df.loc[df['Nombre'] == seleccionar_campeon,
                   'Daño ataque base'] = dano_ataque_base
            df.loc[df['Nombre'] == seleccionar_campeon,
                   'Eficiencia de Oro'] = eficiencia_oro

            # el "w" pensé que funcionaba pero no
            df.to_csv("champions.csv", mode='w', index=False)

    st.dataframe(df)  # ahi lo dejé afuera
