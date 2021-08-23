### Credit Risk Analysis

<p align="center">
  <img src="https://capital.com/files/imgs/glossary/1200x627x1/8-Credit%20Risk.jpg" />
</p>

A empresa Hobbit quer expandir seus negócios e para isso precisa automatizar o processo decisório de crédito, que até então vinha sendo feito de forma manual pelo seu time de analistas de crédito. Para isso, solicitou a você, cientista de dados, a análise da base dos créditos concedidos aos seus clientes no ano de 2020. O objetivo é, que a cada nova proposta de crédito, na sua plataforma digital, a aprovação (para bons clientes) ou recusa (para os maus clientes) seja decidida em poucos segundos.

Percebe-se através da análise que os principais fatores que impactam no risco de crédito são:

* Quantidade de crédito
* status da conta corrente existente
* idade
* duração no mês
* conta crítica do histórico de crédito / outros créditos existentes (não neste banco) 

**Considerações**:

* Clientes maus apresentam em média 954 euros a mais de créditos;
* Créditos com perfis bons são mais tendenciosos a não ter uma conta corrente, enquanto com Créditos maus possuem 80% de ser menor ou igual 0 e menor 200 DM
* Créditos com perfis maus tendem em média ter 5 meses a mais de uso de créditos
* A diferença entre idades dos perfis é de 3 anos sendo que perfis maus são mais novos com média 33 anos.
* Perfis bons tendem a ter mais contas criticas ou creditos em outros bancos.


Como modelo de predição foi utilizado um ensamble de árvore de decisões (Random Forests) obteve-se uma acurácia de 80%.

### Versão:

Python 3.6.5

Bibliotecas:

```pip install -r requirements.txt ```
