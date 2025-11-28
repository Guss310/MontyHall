# El comando para ejecutar es: 'python .\monty_hall.py'

import random
from typing import Tuple, List


def simular_monty_hall(cambiar_puerta: bool) -> bool:
    """Simula una única partida del problema de Monty Hall.

    La función imprime los detalles solicitados:
      - Puerta elegida por el participante
      - Puerta donde está el auto
      - Puerta abierta por el presentador
      - En caso de cambio, cuál es la nueva puerta elegida
      - Resultado del concurso (gana o no el auto)

    Args:
        cambiar_puerta (bool): True si el participante cambia de puerta, False si no.

    Returns:
        bool: True si el participante gana el auto, False en caso contrario.
    """
    puertas = [1, 2, 3]

    puerta_auto = random.randint(1, 3)
    puerta_elegida = random.randint(1, 3)

    # El presentador abre una puerta con cabra que no sea la elegida por el participante.
    opciones_para_abrir = [p for p in puertas if p != puerta_elegida and p != puerta_auto]
    puerta_abierta = random.choice(opciones_para_abrir)

    # Si el participante cambia, elige la única puerta cerrada restante.
    if cambiar_puerta:
        nueva_puerta = next(p for p in puertas if p not in (puerta_elegida, puerta_abierta))
        puerta_final = nueva_puerta
    else:
        nueva_puerta = None
        puerta_final = puerta_elegida

    gano = puerta_final == puerta_auto

    # Impresiones solicitadas
    print("Puerta elegida por el participante:", puerta_elegida)
    print("Puerta donde está el auto:", puerta_auto)
    print("Puerta abierta por el presentador:", puerta_abierta)
    if cambiar_puerta:
        print("Cambio de puerta: la nueva puerta elegida es", nueva_puerta)
    else:
        print("Sin cambio de puerta")
    print("Resultado:", "GANA el auto" if gano else "NO gana el auto")
    print("-" * 40)

    return gano



def _ronda_silenciosa(cambiar_puerta: bool) -> bool:
    """Simula una ronda sin imprimir, para usar en experimentos masivos."""
    puertas = [1, 2, 3]
    puerta_auto = random.randint(1, 3)
    puerta_elegida = random.randint(1, 3)
    opciones_para_abrir = [p for p in puertas if p != puerta_elegida and p != puerta_auto]
    puerta_abierta = random.choice(opciones_para_abrir)

    if cambiar_puerta:
        puerta_final = next(p for p in puertas if p not in (puerta_elegida, puerta_abierta))
    else:
        puerta_final = puerta_elegida

    return puerta_final == puerta_auto


def jugar_n_veces(cambiar_puerta: bool, n: int) -> Tuple[int, float]:
    """Ejecuta n partidas y retorna (ganadas, frecuencia_relativa_ganar)."""
    ganadas = 0
    for _ in range(n):
        if _ronda_silenciosa(cambiar_puerta):
            ganadas += 1
    frecuencia = ganadas / n if n > 0 else 0.0
    return ganadas, frecuencia


def _formatear_resultados(n: int, ganadas: int, frecuencia: float) -> str:
    return f"n={n:,} | ganadas={ganadas:,} | freq={frecuencia:.4f}"


def experimentos(repeticiones: List[int] = [1_000, 10_000, 100_000]) -> None:
    """Corre experimentos para varias 'n' con y sin cambio y muestra resultados."""
    print("\n=== Estrategia: CAMBIAR de puerta ===")
    for n in repeticiones:
        g, f = jugar_n_veces(True, n)
        print(_formatear_resultados(n, g, f))

    print("\n=== Estrategia: NO CAMBIAR de puerta ===")
    for n in repeticiones:
        g, f = jugar_n_veces(False, n)
        print(_formatear_resultados(n, g, f))

    # Conclusión breve
    print("\nConclusión teórica esperada:")
    print("- Cambiar ~ 2/3 de probabilidad de ganar.")
    print("- No cambiar ~ 1/3 de probabilidad de ganar.")


if __name__ == "__main__":
    # Ejemplo de una sola simulación visible
    print("Simulación individual (cambiar=True):")
    simular_monty_hall(True)

    # Experimentos masivos
    experimentos()