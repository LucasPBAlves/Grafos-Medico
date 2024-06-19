Doctors Without Weekends
Trabalho de Organização de Horários de Trabalho para a matéria de Grafos, 5° período de Engenharia da Computação da PUC Minas

Implementação de Algoritmo de Designação de Médicos com PyQt6
Este repositório contém o código-fonte de uma aplicação para organizar os horários de trabalho dos médicos em um grande hospital, desenvolvida em Python utilizando a biblioteca gráfica PyQt6. A aplicação utiliza o algoritmo de Edmonds-Karp para garantir que haja pelo menos um médico de plantão em cada dia de períodos especiais, como feriados.

Sobre o Projeto
O objetivo deste projeto é fornecer uma ferramenta interativa para a designação de médicos em períodos de feriados, permitindo aos usuários verificar se é possível selecionar um médico para trabalhar em cada dia de férias, respeitando restrições específicas. O projeto foi desenvolvido como parte de um trabalho acadêmico sobre algoritmos e teoria dos grafos.

Autores
Lucas Pimenta Brito Alves
Funcionalidades
Entrada dos períodos de férias e disponibilidade dos médicos.
Validação de entradas para garantir valores positivos e corretos.
Utilização do algoritmo de Edmonds-Karp para determinar a designação possível de médicos.
Interface gráfica interativa com navegação entre diferentes telas para entrada de dados e visualização de resultados.
Pré-requisitos
Para executar o projeto, você precisará ter instalado em seu sistema:

Python 3.x
PyQt6
Você pode instalar a PyQt6 usando o pip, o gerenciador de pacotes do Python:

bash
Copiar código
pip install PyQt6
Como Executar
Para rodar a aplicação, clone o repositório para sua máquina local e execute o arquivo principal:

bash
Copiar código
git clone https://github.com/LucasPBAlves/Doctors-Without-Weekends
cd Doctors-Without-Weekends
python main.py
Navegação das Telas e Funcionalidades
Tela 1: Entrada de K, N e C
Permite ao usuário especificar os valores de:

K: Número de períodos de férias.
N: Número de médicos.
C: Máximo de dias que um médico pode trabalhar em feriados.
Tela 2: Entrada dos Dias de Férias
Permite ao usuário especificar os dias de férias para cada período:

Cada período de férias é representado por uma lista de dias separados por vírgulas.
Exemplo: 1,2,3,4
Tela 3: Entrada da Disponibilidade dos Médicos
Permite ao usuário especificar os dias disponíveis para cada médico:

Cada médico é representado por uma lista de dias separados por vírgulas.
Exemplo: 1,2,3,4
Tela 4: Resultado
Exibe se é possível ou não a atribuição de médicos para todos os dias de férias, respeitando as restrições impostas:

Mensagem de sucesso ou falha na designação dos médicos.
Botão para reiniciar o processo.
Exemplo de Uso
Tela 1: Insira K, N e C.
Clique no botão "Próximo".
Tela 2: Insira os dias de férias para cada período.
Clique no botão "Próximo".
Tela 3: Insira os dias disponíveis para cada médico.
Clique no botão "Próximo".
Tela 4: Veja o resultado da designação dos médicos.
Clique no botão "Recomeçar" para iniciar novamente.
Estrutura do Código
O código está estruturado em várias classes que representam as diferentes telas e a lógica principal da aplicação. As classes principais são:

MainApp: Classe principal que gerencia a navegação entre as telas.
Screen1: Tela para entrada de K, N e C.
Screen2: Tela para entrada dos dias de férias.
Screen3: Tela para entrada da disponibilidade dos médicos.
Screen4: Tela de resultado.
Cada classe de tela herda de QWidget e utiliza layouts e widgets do PyQt6 para construir a interface do usuário.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Contato
Para mais informações, entre em contato:

Lucas Pimenta Brito Alves - lucaspbritoalves@example.com
