<h1>TCC</h1>
Trabalho de Conclusão de Curso - Universidade Anhembi Morumbi
<h2>Objetivos</h2>
Esse trabalho tem como objetivo a implementação de um algoritmo de Machine Learning (K-Means) para o agrupamento de pessoas com perfil similar ao caminharem nas ruas ou utilizarem o transporte público.
<h2>Tecnologias</h2>
<p>O algoritmo foi implementado na linguagem Python, utilizando as bibliotecas <a href="https://pandas.pydata.org/" target="_blank">Pandas</a>, <a href="https://matplotlib.org/" target="_blank">Matplotlib</a> e <a href="https://scikit-learn.org/stable/" target="_blank">Scikit-Learn</a>.</p>
<h2>Base de dados</h2>
A base de dados utilizada foi um arquivo csv, que se encontra nesse repositório. Esse arquivo contém as respostas adquiridas por meio de um questionário que foi elaborado com o intuito de obter os diferentes perfis das pessoas que caminham e/ou utilizam o transporte público. Esse questionário contém perguntas demográficas, perguntas relacionadas ao uso de determinados tipos de transporte, perguntas sobre preferências à certas características de uma caminhada/viagem e perguntas sobre a frequência que as pessoas saem de suas casas em determinados períodos do dia. Todos esses questionamentos foram feitos a fim de mapear os possíveis perfis das pessoas. O questionário foi realizado no Google Forms e respondido online. Ele obteve 333 respostas, ou seja, o algoritmo utilizou 333 dados para o agrupamento.
<h2>Etapas</h2>
Após a aquisição dos dados pelo questionário, foi necessário alguns passos antes da implementação do algoritmo:
<ul>
  <li>Transformação de dados qualitativos em dados quantitativos, para a utilização correta do algoritmo.</li>
  <li>Seleção de atributos mais importantes para o agrupamento.</li>
  <li>Análise de Componentes Principais (PCA) para a redução da dimensionalidade dos dados, melhorando a visualização e eliminando redundâncias e características menos importantes.</li>
  <li>Implementação do K-Means na base de dados criada.</li>
  <li>Validação do agrupamento gerado por meio do índice silhueta.</li>
</ul>
<h2>Outras Informações</h2>
O artigo desenvolvido nesse trabalho também se encontra nesse repositório, com maiores explicações sobre alguns conceitos utilizados e decisões de projeto.
