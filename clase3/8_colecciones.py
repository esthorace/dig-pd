paises: dict[str, dict] = {
    "Japón": {"capital": "Tokio", "población": 126476461, "idioma": "Japonés"},
    "España": {"capital": "Madrid", "población": 47450795, "idioma": "Español"},
    "Francia": {"capital": "París", "población": 65273511, "idioma": "Francés"},
}

japon = paises["Japón"]
print(japon)
japon_poblacion = paises["Japón"]["población"]
print(japon_poblacion)
