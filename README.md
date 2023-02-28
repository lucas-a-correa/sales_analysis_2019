# Análise de Vendas - 2019

## Análise de vendas de uma loja online no ano de 2019

## 1. Sumário

* Contexto
* Dados
* Análise
* Conclusão

## 2. Contexto

O presente relatório busca analisar os dados de vendas no ano de 2019 de uma loja online. O relatório acompanha uma [apresentação]() em PowerPoint e busca explicar os detalhes desta.

##3. Dados

Os dados utilizados foram obtidos de um dataset do [Kaggle](https://www.kaggle.com/datasets/knightbearr/sales-product-data).
Os dados são divididos em 12 arquivos CSV, um para cada mês do ano. Foi utilizado um [script]() em Python para a limpeza e análise dos dados.

O único problema encontrado nos dados foi o fato de que todos os arquivos CSV possuiam alguma quantidade de linhas nulas ou com repetições dos títulos das colunas. No total, foram encontradas 900 linhas com algum desses problemas, ou 0,48% dos dados. Esses problemas apresentavam-se distribuídos entre os arquivos de cada mês, com uma prevalência de entre 0,23% e 0,34% de dados nulos e 0,14% e 0,24% de linhas repetidas. O fato de estar distribuído em porcentagens similares entre todos os meses, sem que nenhum se destaque em particular, aponta para algum problema na conversão dos dados ou no próprio sistema que recebe a entrada dessas dados, sendo interessante o exame para que se evitem erros futuros.

## 4. Análise

![Vendas_Anuais](https://user-images.githubusercontent.com/120389170/221806053-eb812bd7-f21e-43a3-b6d9-7e1750ac5c00.png)

No gráfico acima podemos observar o total de vendas por mês, bem como a receita total por mês. As vendas foram bem distribuídas durante o ano, com um total de 178.440 mil vendas e uma receita de US$ 34,49 milhões, uma média de 14.453 vendas por mês e um desvio-padrão de 3.882, com uma leve tendência nos últimos 3 meses do ano, que representam cerca de 32% das vendas do ano, provavelmente explicadas pelos feriados no final do ano, para os quais as pessoas costumas comprar presentes.

![Paretto_Produtos](https://user-images.githubusercontent.com/120389170/221806597-c9417932-d061-4601-9b1a-94fb10424d70.png)

Em seguida, podemos analisar as vendas por produto e suas respectivas importâncias. Vemos que 7 produtos representam 74,38% das vendas, de um total de 19 produtos. Destes, os dois mais vendidos, com 28,05% das vendas, são diferentes tipos de pilhas, enquanto os demais 5 são produtos para smartphones (carregadores e fones de ouvido) e representam 46,33% das vendas. Entretanto, observemos o gráfico abaixo, que destaca a receita por produto:

![Paretto_Receita](https://user-images.githubusercontent.com/120389170/221831816-0dbc3cdb-5852-46be-9cba-1d4d1f762a56.jpg)

Vemos que 7 produtos concentram 79,5% da receita total, e somente um deles está entre os que mais vendem. Isso é explicado pelo preço individual de cada produto. O Apple Airpod, que é o 6° produto mais vendido e a 7ª maior receita é o produto com o 11° maior preço e encontra-se no meio do caminho entre esses dois grupos. Em relação aos demais, verificamos que os outros 6 produtos mais vendidos são os 6 menores valores, e dos demais 6 produtos com maior receita todos encontram-se entre os 9 maiores preços, como destaca-se no gráfico abaixo:

![Paretto_Receita](https://user-images.githubusercontent.com/120389170/221831845-8e58dc2f-d5fe-4823-aa6b-1aec48d1f2bc.jpg)

Esse é um comportamento esperado, uma vez que um menor preço tende a gerar uma maior demanda e, consequentemente, um maior volume de vendas. Mas como a diferença de preço entre o produto mais vendido e o mais caro é de quase US$ 1.700, a quantidade de demanda é mais do que suficiente para gerar a diferença de receita.

![Vendas_por_Local](https://user-images.githubusercontent.com/120389170/221831225-d45dd24b-7e0f-4afa-93d5-616c02acd272.png)

Na sequência, o gráfico destaca as localidades e suas respectivas receitas. Podemos observar que nossas vendas são divididas em 3 grandes regiões, Costa Leste, Costa Oeste e Sul. Nestas, 4 cidades, São Francisco e Los Angeles na Costa Oeste, Nova Iorque e Boston na Costa Leste, concentram 63,9% da receita anual.

![Vendas_Hora](https://user-images.githubusercontent.com/120389170/221831943-2fca0b77-433f-4cd8-bfd8-873dca79069b.png)

Por fim, observamos a quantidade de vendas realizadas ao longo do dia. Como podemos esperar, a grande maioria (84,97%) das vendas se concentram no período de 9h às 21h, quando a maior parte das pessoas está acordada, mas dentro desse período podemos realizar algumas análises. 56% das vendas são realizadas no período de 12h às 20h, apontando uma maior preferência para a tarde e o final do dia para as compras. Podemos verificar dois picos de vendas em torno de 12h e 19h. Esses picos podem ser explicados por acontecerem no horário de almoço e na volta do trabalho para casa, horários em que as pessoas podem utilizar seus aparelhos eletrônicos com mais tranquilidade e realizar compras.

## 5. Conclusão

Com base na análise acima, podemos destacar alguns pontos de atenção:

* Necessidade de avaliar o sistema de lançamento e conversão de dados para evitar erros;
* Analisar o relacionamento com os fornecedores dos produtos mais vendidos e dos produtos com maior potencial de renda, buscando evitar a interrupção da cadeia de suprimentos e verificar a possibilidade de maximizar os lucros;
* Orientar a logística da empresa de acordo com os dados de localização das vendas, verificando se nossa atual estrutura logística atende as necessidades locais e se nossos Centros de Distribuição encontram-se em locais que façam sentido logísticamente.
* Planejar nossos recursos para os períodos de pico, em menor escala, nos horários do dia com maior acesso, em grande escala, nos meses do ano com maior volume de vendas, buscando certificar-se de que nossos recursos humanos, logísticos e operacionais são suficientes para atender a alta demanda.
