import math

def regra_trapezio(f, a, b, n):
    """
    Calcula a integral numérica de uma função 'f' de 'a' até 'b'
    usando a regra do trapézio com 'n' subintervalos.

    Args:
        f (function): A função a ser integrada. Deve aceitar um único argumento numérico.
        a (float): O limite inferior da integração.
        b (float): O limite superior da integração.
        n (int): O número de trapézios (subintervalos).

    Returns:
        float: O valor aproximado da integral.
    """
    if n <= 0:
        raise ValueError("O número de trapézios (n) deve ser um inteiro positivo.")

    # 1. Calcular a largura de cada trapézio
    h = (b - a) / n

    # 2. Iniciar a soma com os termos das extremidades (f(a) e f(b))
    #    De acordo com a fórmula, eles não são multiplicados por 2.
    soma = f(a) + f(b)

    # 3. Somar os termos do meio (multiplicados por 2)
    for i in range(1, n):
        x_i = a + i * h
        soma += 2 * f(x_i)

    # 4. Multiplicar a soma final por h/2 para obter a área total
    resultado = (h / 2) * soma
    
    return resultado

# --- ÁREA DE EXEMPLO E UTILIZAÇÃO ---

# Para usar com sua função, basta alterar o conteúdo da função f(x) abaixo.
# Lembre-se que você pode usar funções da biblioteca 'math'.
def minha_funcao(x):
    """Função matemática a ser integrada."""
    # Exemplo 1: Uma parábola simples, f(x) = x^2
    return x**2
    
    # Exemplo 2: Uma função trigonométrica, f(x) = sin(x)
    # return math.sin(x)

    # Exemplo 3: Uma função mais complexa, f(x) = e^(-x^2)
    # return math.exp(-x**2)

if __name__ == "__main__":
    # --- Parâmetros da Integração ---
    
    # Limite inferior de integração
    limite_inferior = 0.0
    
    # Limite superior de integração
    limite_superior = 1.0
    
    # Número de trapézios (quanto maior, mais preciso o resultado)
    qtd_trapezios = 1000

    # --- Execução e Resultados ---
    
    # Chama a função de integração
    valor_integral = regra_trapezio(minha_funcao, limite_inferior, limite_superior, qtd_trapezios)

    print(f"Função a ser integrada: f(x) = x^2")
    print(f"Intervalo de integração: de {limite_inferior} a {limite_superior}")
    print(f"Número de trapézios utilizados: {qtd_trapezios}")
    print("-" * 40)
    print(f"Valor aproximado da integral: {valor_integral}")
    
    # Para f(x) = x^2, o valor exato da integral de 0 a 1 é 1/3
    valor_exato = 1/3
    erro = abs(valor_exato - valor_integral)
    print(f"Valor exato da integral: {valor_exato}")
    print(f"Erro da aproximação: {erro:.10f}")