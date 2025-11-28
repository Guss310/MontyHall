# Monty Hall – Simulación en Python

## Cómo ejecutar

Usa Windows PowerShell:

```powershell
# Ejecutar el script
python .\monty_hall.py
```

Vas a ver una simulación individual y luego resultados para 1.000, 10.000 y 100.000 repeticiones con y sin cambio.

## Resultados esperados (teoría)

- Cambiar de puerta ≈ probabilidad de ganar de 2/3.
- No cambiar de puerta ≈ probabilidad de ganar de 1/3.

Las simulaciones deberían aproximarse a estos valores a medida que aumenta `n`.

## Breve explicación

- Se posiciona al azar el auto detrás de una de las 3 puertas y el participante elige una al azar.
- El presentador, que sabe dónde está el auto, abre una puerta que no fue elegida y no tiene el auto.
- Si el participante cambia, se queda con la única puerta cerrada restante.
- Se registra si la puerta final contiene el auto.

## Referencias

- Wikipedia: https://es.wikipedia.org/wiki/Problema_de_Monty_Hall
- Explainer (en inglés): https://mathworld.wolfram.com/MontyHallProblem.html
