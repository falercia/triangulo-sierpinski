import random
import matplotlib.pyplot as plt


def sierpinski(num_pontos: int, seed: int | None = None):
    """
    Desenha o Triângulo de Sierpinski usando o Chaos Game.
    num_pontos = quantidade de pontos a plotar (quanto mais, mais definido).
    seed = semente opcional para reproduzir o mesmo resultado.
    """
    if num_pontos <= 0:
        raise ValueError("num_pontos deve ser > 0")

    if seed is not None:
        random.seed(seed)

    # Vértices do triângulo (equilátero, coordenadas simples)
    A = (0.0, 0.0)
    B = (1.0, 0.0)
    C = (0.5, 0.8660254037844386)  # sqrt(3)/2

    vertices = [A, B, C]

    # Começa de um ponto aleatório dentro do triângulo (aqui: média com pesos aleatórios)
    r1, r2, r3 = random.random(), random.random(), random.random()
    s = r1 + r2 + r3
    x = (r1*A[0] + r2*B[0] + r3*C[0]) / s
    y = (r1*A[1] + r2*B[1] + r3*C[1]) / s

    xs = []
    ys = []

    # (Opcional) descartar alguns passos iniciais para "estabilizar"
    burn_in = 20

    for i in range(num_pontos + burn_in):
        vx, vy = random.choice(vertices)
        x = (x + vx) / 2.0
        y = (y + vy) / 2.0

        if i >= burn_in:
            xs.append(x)
            ys.append(y)

    # Plot
    plt.figure(figsize=(8, 7))
    plt.scatter(xs, ys, s=0.2, marker='.', linewidths=0)
    plt.axis('equal')
    plt.axis('off')
    plt.title(f"Triângulo de Sierpinski — {num_pontos:,} pontos")
    plt.show()


if __name__ == "__main__":
    try:
        n = int(input("Informe a quantidade de pontos (ex: 50000): ").strip())
        sierpinski(n)
    except ValueError as e:
        print(f"Entrada inválida: {e}")
