# Automação de Cadastro de Produtos

## Resumo
Este projeto em Python foi elaborado com o propósito de automatizar o processo de cadastro de produtos no sistema de uma empresa. Utilizando a biblioteca PyAutoGUI e Pandas para leitura do arquivo, o script possibilita a realização de ações como a abertura do navegador Google Chrome, efetuação do login no site corporativo, importação de uma base de dados, leitura da referida base e subsequente cadastro automatizado dos produtos no sistema empresarial.
## Funcionamento
As adaptações necessárias a se fazer para que o código funcione para sua empresa são:
- Trocar o link de acesso do site para cadastro e o login (linha 21);
- Importar a base de dados a ser utilizada (linha 39); 
- Alterar os nomes das colunas e se preferível, adicionar algum tratamento específico para o sistema da empresa (linha 50 a 79);
## Observações
Se for de sua preferência, é possível modificar o py.press(‘tab’) para py.click(x=, y=), porém os valores do x e y teriam que ser mudados de acordo com o tamanho da tela, resolução ou até mesmo um monitor de modelo diferente.<br>
A biblioteca time foi utilizada apenas para garantir o carregamento da aba e do site de forma que não corra o risco de dar algum bug no código.

 
