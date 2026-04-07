# Análise de Artigo: Métodos Numéricos em Otimização Many-Objective

## 📌 Identificação do Conceito de Métodos Numéricos
* **Tema Principal:** Raízes de Funções.
* **Método Específico Aplicado no Artigo:** Método iterativo de Newton-Raphson.

## 📝 Descrição do Problema e Solução

### O Problema
Em algoritmos de otimização com muitos objetivos (Many-Objective Optimization), o sistema precisa gerar um conjunto de soluções que seja próximo da frente ideal (convergência) e bem distribuído (diversidade). Para medir isso corretamente, o algoritmo precisa descobrir qual é a "curvatura" (geometria $p$) dessa Fronteira de Pareto.

### O Método Clássico e o Método Heurístico
Historicamente, algoritmos como o GFM-MOEA usam métodos clássicos de ajuste não-linear (como o algoritmo de Levenberg-Marquardt) para modelar essa curva. 
O próprio autor do artigo havia tentado simplificar isso anteriormente no algoritmo AGE-MOEA original, usando uma heurística matemática simples baseada em um único ponto central da curva.

### A Limitação
* **Do método clássico (Levenberg-Marquardt):** Possui um custo computacional massivo, inviabilizando sua execução a cada geração do algoritmo.
* **Da heurística (AGE-MOEA antigo):** Ausência de estabilidade e precisão. O cálculo do erro é grosseiro e o valor da curvatura muda drasticamente dependendo de qual ponto da curva é escolhido como referência.

### A Solução Proposta
O artigo propõe abandonar o ajuste não-linear e a heurística falha, transformando a modelagem da curva em um problema puramente de busca de raízes, onde $f(p) = 0$. 
Para resolver isso, aplica-se o **Método de Newton-Raphson**. A solução é elegante porque o Newton-Raphson converge rapidamente (média de 3 a 4 iterações), mantendo o baixo custo computacional, mas garantindo a precisão exata da curvatura independentemente do ponto escolhido.
