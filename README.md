# Astrobirds

Por: Alexandre Magno e Júlia Paiva

# 1. Como rodar?

1. Inicialmente, é necessário ter a versão 3.10 ou superior do Python. [Guia para download/update](https://www.geeksforgeeks.org/how-to-update-python-on-windows/);
2. Neste repositório do github do projeto, clique no botão verde "Code" e selecione a opção de "download zip";
3. Extraia o conteúdo do zip para uma pasta no seu computador;
4. Abra um terminal na pasta e execute o comando "pip install -r requirements.txt" para instalar as bibliotecas necessárias;
5. Abra essa pasta em um editor de código e execute o arquivo "main.py".

# 2. Como jogar?

Uma iminente chuva de meteoros está proxima de atingir a Terra, portanto:
1. Utilize o ponteiro para atirar na direção dos asteroides verdes que aparecem na tela;
2. Você terá 5 vidas, cada vez que for atingido por um asteroide perde uma;
3. Próximo à Terra há um satélite vermelho. Ele possui antigravidade que afasta os meteoros, portanto, esse pode ser seu maior aliado;
* Utilizar um mouse é o mais recomendado para o Astrobirds.

# 3. Modelos físicos utilizados

   Em Astrobirds utilizamos conceitos Mecânica Classica, especificamente Cinemática e Gravitação Universal, com o intuíto de criar um ambiente que simulasse o espaço dentro do jogo. Como base para o cálculo da movimentação dos disparos, planetas e asteorides, a Cinemática atuou por meio de Movimento Uniformemente Variado para determinar novas velocidades e posições desses objetos frame a frame. Isso ocorreu, por meio de formulas adaptadas, partindo de: V = V0 + a * t, S = S0 + V0 * t + (a * t^2)/2.
   Contudo, o principal recurso de Astrobirds é a simulação de gravidade que atrai e repele os objetos, alterando a resultante de aceleração de cada um deles. Isso é resultado de uma soma vetorial entre acelerações gravitacionais: g = (G * M)/d^2 geradas pelos planetas e atuando sobre as partículas. 
  
# 4. Física sobre Objetos

| Objeto | Modelo Físico | Gravidade |
| --- | --- | --- |
| Terra | Fixo na tela | Gera atração gravitacional sobre Meteoros e Raios |
| Lua | Movimento Circular Uniforme | Gera atração gravitacional oposta (*) |
| Meteoro | Movimento Uniforme Variado | Não gera atração gravitacional |
| Raio | Movimento Uniforme Variado | Não gera atração gravitacional |

(*) Calcula aceleração sobre objetos como um planeta, porém com uma constante gravitacional negativa. Gerando assim, uma resultante também negativa que repele as partículas de raios e meteoros.
 
# 5. GIF do jogo

![alt-text](https://github.com/juliapaiva1/Astrobirds/blob/main/gif_jogo.gif)
