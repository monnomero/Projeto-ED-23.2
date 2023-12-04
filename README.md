Árvore AVL para Manejamento de Cores de Forma Única

Descrição do Projeto:

	Este projeto implementa uma árvore AVL para gerenciar cores RGB. Ele permite a inserção, busca, remoção e visualização de cores, assim como a criação de arte abstrata usando uma seleção manual, a partir do mouse, ou aleatória de cores.

Autores:

	Nome do Autor: Henrique de Oliveira Noronha

Contexto de Aplicação:

	Este projeto foi desenvolvido para fins educacionais e artísticos. Ele oferece uma maneira única e interativa de manipular e visualizar cores, a partir do balanceamento da árvore AVL, além de criar arte abstrata a partir de uma seleção de cores. Um exemplo de aplicação seria o de analisar como uma paleta de cores presente em uma pintura se comporta em uma árvore AVL, além de poder fazer uma arte abstrata rudimentar a partir dessa paleta.

Estruturas de Dados Utilizadas:

	O projeto utiliza uma Árvore AVL para armazenar e gerenciar as cores RGB. A estrutura da árvore AVL é escolhida por sua capacidade de balanceamento automático, garantindo operações eficientes de inserção, busca e remoção, além de proporcionar uma visão única sobre a relação das cores RGB.

Instruções de Execução:
	Para executar o programa, siga as etapas abaixo:

	Certifique-se de ter o Python, assim como as bibliotecas utilizadas listadas abaixo instalados.
		Bibliotecas: pyautogui, numpy, matplotlib, mouse
	Clone ou baixe o repositório do projeto.
	Execute o arquivo Python arvore_avl_cores.py em seu ambiente Python.

Instruções de Uso:

	Inserir cores manualmente: Utilize a opção "ICM" e insira as cores no formato 255,255,255 (R,G,B).
	Inserir cores com o mouse: Escolha "ICCM" para selecionar cores com o mouse.
	Buscar cores na árvore: Use "B" para buscar uma cor específica na árvore.
	Deletar cores: Utilize "D" para deletar uma cor específica na árvore.
	Plotar o gradiente das cores: Escolha "PG" para visualizar um gradiente das cores armazenadas na árvore.
	Plotar a animação das cores em inorder: Use "PA" para visualizar uma animação das cores na ordem em que estão na árvore.
	Plotar uma arte abstrata: Escolha "PAA" para criar uma arte abstrata após adicionar cores manualmente com o mouse ou aleatoriamente até uma potência de 4 a partir de 4^4 com as cores na árvore.
	Printar a travessia inorder: Use "PTI" para visualizar a travessia inorder da árvore.
	Limpar o terminal: Use "C" para limpar a tela do terminal.
	Resetar a árvore: Utilize "R" para resetar a árvore.
	Finalizar o programa: Digite "FIM" para encerrar o programa.

Referências
- Slides da Professora 
- Data Structure and Algorithmic Thinking with Python
- StackOverflow
