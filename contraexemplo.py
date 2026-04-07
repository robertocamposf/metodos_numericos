import math

def heuristica_antiga(a1, a2):
    """
    Equação 4 do artigo: A heurística antiga do AGE-MOEA que apresentava instabilidade.
    """
    M = 2.0 # Número de objetivos (2D neste exemplo)
    soma = a1 + a2
    return math.log(M) / (math.log(M) - math.log(soma))

def newton_raphson(a1, a2, tolerancia=0.001, max_iter=10):
    """
    Equações 8 e 9 do artigo: O método de Newton-Raphson proposto para corrigir a falha.
    """
    p = 1.0 # Chute inicial (Semente sugerida no artigo)
    erro = 1.0
    iteracao = 0

    print("\n--- Iniciando Iterações do Newton-Raphson ---")

    while erro > tolerancia and iteracao < max_iter:
        p_antigo = p

        # f(p) = log( a1^p + a2^p )
        soma_p = math.pow(a1, p) + math.pow(a2, p)
        f_p = math.log(soma_p)

        # Derivada f'(p) = ( a1^p * log(a1) + a2^p * log(a2) ) / ( a1^p + a2^p )
        # Prevenindo erro de log(0) conforme o artigo: (a_i)^p * log(a_i) = 0 se a_i == 0
        termo1 = math.pow(a1, p) * math.log(a1) if a1 > 0 else 0
        termo2 = math.pow(a2, p) * math.log(a2) if a2 > 0 else 0
        derivada_f_p = (termo1 + termo2) / soma_p

        # p_n+1 = p_n - f(p_n) / f'(p_n)
        p = p - (f_p / derivada_f_p)

        erro = abs(p - p_antigo)
        iteracao += 1
        
        print(f"Iteração {iteracao} | p atual = {p:.8f} | Erro = {erro:.8f}")

    return p

if __name__ == "__main__":
    # Ponto B do exemplo gráfico do artigo: B = (cos(pi/8), sin(pi/8))
    # Por estar em um círculo perfeito, a curvatura REAL procurada é p = 2.0
    B1 = math.cos(math.pi / 8)
    B2 = math.sin(math.pi / 8)

    print(f"Ponto de teste B = ({B1:.4f}, {B2:.4f})")
    print("Curvatura real esperada: p = 2.0000")

    # Teste 1: Heurística Falha
    p_errado = heuristica_antiga(B1, B2)
    print(f"\n[Resultado Heurística Antiga] p = {p_errado:.8f}")
    print("-> Erro grosseiro. O valor dependia da posição do ponto.")

    # Teste 2: Método Numérico Proposto
    p_correto = newton_raphson(B1, B2)
    print(f"\n[Resultado Newton-Raphson]  p = {p_correto:.8f}")
    print("-> Preciso e estável. Convergiu para a resposta correta em poucas iterações.")
