from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css" integrity="sha512-10/jx2EXwxxWqCLX/hHth/vu2KY3jCF70dCQB8TSgNjbCVAC/8vai53GfMDrO2Emgwccf2pJqxct9ehpzG+MTw==" crossorigin="anonymous" referrerpolicy="no-referrer">
    <style>
        /* Coloque os estilos do arquivo style.css aqui */
        * {
            box-sizing: border-box;
        }

        body.fixed .cabeçalho-link {
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background-color: black;
            background-size: cover;
            background-repeat: no-repeat;
            border-radius: 20px;
            background-size: 100% 100%;
            background-attachment: fixed;
            font-family: Arial, sans-serif;
            margin: 50;
            padding: 100px;
            display: flex;
            flex-direction: column;
            border-radius: 30px;
            border: solid 3px rgb(12, 72, 235);
        }

        section {
            display: block;
            padding: 100px;
            border: solid 3px rgb(12, 72, 235);
            margin: 20px;
            border-radius: 30px;
            /* Arredonda as bordas do section */
        }

        footer {
            border: solid 3px rgb(12, 72, 235);
            border-radius: 30px;
            color: rgb(12, 72, 235);
            text-align: center;
            padding: 10px;
        }

        /* Arredonda as bordas do body */

        .background {
            background-color: black;
            background-repeat: no-repeat;
            /* Evita a repetição da imagem */
            background-size: cover;
            /* Ajusta o tamanho para cobrir todo o elemento */
            background-position: center;
            /* Centraliza a imagem no elemento */
        }

        header {
            border-radius: 15px;
            color: #fff;
            padding: 10px 0;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            border-radius: 100px;
            color: #fff;
            padding: 1px;
            margin-bottom: 20px;
        }

        .cabeçalho-link ul {
            list-style: none;
            padding: 0;
            display: flex;
        }

        .cabeçalho-link li {
            margin-right: 20px;
        }

        .cabeçalho-link a {
            text-decoration: none;
            color: #fff;
            font-weight: bold;
            font-size: 18px;
        }

        .cabeçalho-link a:hover {
            color: #0909fa;
            transition: 0.3s all;
        }

        .container-text {
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        span {
            color: #0909fa;
        }

        .text h3 {
            color: #0909fa;
            font-size: 28px;
        }

        h3 {
            text-align: center;
            color: #fff;
        }

        h2 {
            text-align: center;
            color: #fff;
        }

        h1 {
            text-align: center;
            color: #fff;
        }

        h4 {
            text-align: center;
            color: #fff;
        }

        .p_footer {
            text-align: center;
        }

        .fonte18 {
            font-size: 18px;
        }

        p {
            text-align: justify;
            color: #fff;
        }

        label {
            color: #fff;
        }

        .text h1 {
            color: #fff;
            font-size: 36px;
        }

        .text p {
            color: #fff;
            font-size: 16px;
            text-align: center;
            margin: 20px 0;
        }

        .redes-social a {
            text-decoration: none;
            color: #0909fa;
            font-size: 24px;
            margin: 0 10px;
        }

        button {
            color: #0909fa;
            background: transparent;
            padding: 5px;
            border-radius: 15px;
            font-size: 12px;
            cursor: pointer;
            width: 150px;
        }

        button:hover {
            background-color: #0909fa;
            color: #fff;
            transition: 0.5s;
        }

        .btn {
            background: transparent;
            color: #fff;
            padding: 10px 20px;
            border: 1px black;
            cursor: pointer;
            margin-top: 20px;
            /* Adiciona margem de 20px na parte superior */
        }

        .logo {
            height: 40px;
            width: 40px;
            background: transparent;
            border: 3px solid #0909fa;
            color: #0909fa;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            cursor: pointer;
        }

        .red {
            color: red;
        }

        .project-secction {
            display: flex;
            /* Torna a seção um contêiner flexível */
            flex-direction: column;
            /* Organiza os elementos verticalmente */
            padding: 100px;
            margin: 20px;
            border: solid 3px rgb(12, 72, 235);
            border-radius: 30px;
            /* Arredonda as bordas do .project */
        }

        .project-secction img {
            display: flex;
            border: solid 3px rgb(12, 72, 235);
            margin: 20px;
            max-width: 100%;
            height: auto;
            border-radius: 15000px;
            /* Arredonda as bordas das imagens dentro de .project */
        }

        .project-secction2 {
            display: flex;
            /* Torna a seção um contêiner flexível */
            flex-direction: column;
            /* Organiza os elementos verticalmente */
            padding: 100px;
            margin: 20px;
            border: solid 3px rgb(12, 72, 235);
            border-radius: 30px;
            /* Arredonda as bordas do .project */
        }

        .project-secction2 img {
            display: flex;
            border: solid 3px rgb(12, 72, 235);
            margin: 20px;
            max-width: 100%;
            height: auto;
            border-radius: 50px;
            /* Arredonda as bordas das imagens dentro de .project */
        }

        #form {
            text-align: center;
            display: block;
            /* Torna a seção um contêiner block */
            padding: 10px;
            margin: 50px;
            border: solid 3px rgb(12, 72, 235);
            border-radius: 30px;
            /* Arredonda as bordas do .project */
        }

        .margen-class {
            padding: 30px;
            border: solid 3px rgb(12, 72, 235);
            margin: 30px;
            border-radius: 30px;
            /* Arredonda as bordas das classes .margen-class */
        }

        #about {
            display: auto;
            /* Ativa o layout de duas colunas usando flexbox */
            justify-content: space-between;
            /* Colunas distribuídas horizontalmente */
        }

        .column {
            border-radius: 10px;
            flex: 1;
            /* Faz com que as colunas ocupem a mesma largura */
            padding: 10px;
            /* Adicione preenchimento interno para separação */
            border: 3px solid rgb(12, 72, 235);
            /* Adicione bordas para separação visual */
        }

        /* Adaptação dos estilos do menu para o seu caso */

        /* Exemplo de media query para dispositivos móveis */

        @media screen and (max-width: 768px) {
            body {
                padding: 20px;
                /* Reduza o preenchimento */
            }
            header {
                padding: 20px;
            }
            .column {
                padding: 10px;
                margin: 10px;
                border: 1px solid rgb(12, 72, 235);
            }
            .project-secction {
                padding: 10px;
                margin: 10px;
            }
            .project-secction img {
                border: 1px solid rgb(12, 72, 235);
            }
        }
    </style>
    <title>Quantum Computer</title>
</head>

<body>
    <script>
        // Adiciona uma classe "fixed" ao menu quando o usuário rola a página
        window.onscroll = function() {
            var navbar = document.getElementById("navbar");
            var body = document.body;

            if (window.pageYOffset >= navbar.offsetTop) {
                body.classList.add("fixed");
            } else {
                body.classList.remove("fixed");
            }
        };
    </script>

    <div>
        <header>

            <img class="logo" src="img/Qiskit.JPG" alt="Logo do Qiskit" style="width: 100px; height: 100px;">

            <!-- logo -->

            <div class="cabeçalho-link" class="navbar" id="navbar">
                <ul>
                    <li><a href="index.html">Introdução</a></li>
                    <li><a href="aplication.html">Aplicações</a></li>
                    <li><a href="ingresso.html">Como Ingressar</a></li>
                    <li><a href="mat.html">Matematica da Computação Quântica</a></li>
                    <li><a href="Qiskit.html">Qiskit</a></li>
                    <li><a href="#contato"><button>Contato</button></a></li>
                </ul>
            </div>
            <!-- cabeçalho-link -->
        </header>

        <div class="container-text">
            <div class="text">
                <h1> Qiskit <span> o que é e com usar?</span></h1>
                <p>Qiskit é um kit de ferramentas de código aberto para computação quântica útil. compilador de circuito pronto para produção.</p>

                <br>
                <!-- redes-social -->
            </div>
            <!-- text -->
        </div>
        <!-- container-text -->
    </div>
    <!-- background -->

    <script type="script.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>

    <section class="about" id="section2">
        <div>
            <h2>Primeiro passo</h2>
            <div class="column">
                <p>Em uma máquina simulada, colocaremos um qubit em superposição, em dois estados ao mesmo tempo, com a uma porta lógica quantica chamada hadamardsobreposição nas bases computacionais., criando uma conexão sem nenhuma relação com a física
                    clássica.
                </p>
            </div>
            <br>
            <h2>Segundo passo</h2>
            <div class="column">
                <p>Carregaremos nosso circuito em uma máquina Quâtica e colocaremos para fins de comparação ambos resultados.</p>
            </div>
        </div>
    </section>

    <section class="project-secction" class="content" id="section1">
        <h2>Plataforma IBM</h2>
        <div class="project-secction">
            <img src="img/dash.png" alt="Projeto 1">
            <h3>Primeiro contato</h3>
            <p> Acesse o link https://quantum-computing.ibm.com/ e registre-se. </p>
            <br>
            <p>Agora com a conta em mãos, acessaremos o IBM Quantum Lab no Menu lateral superor esquerdo.</p>
        </div>
        <br>
        <br>
        <br>

        <!-- Repita para outros projetos -->
    </section>

    <section class="project-secction2" class="content" id="section1">
        <h2>Plataforma IBM</h2>
        <div class="project-secction">
            <img src="img/pynote.png" alt="Projeto 1">
            <h3>IBM Quantum Lab</h3>
            <p> Cliclaremos na Opção Python3(ipkernel) Python notebook, para codar na pratica. </p>
            <br>
            <p>Agora mãos na massa.</p>
            <br>
            <br>
            <img src="img/import.png" alt="Projeto 1">
            <p>Importando o necessario para nosso experimento:</p>
            <p class="red">
                from qiskit import *
            </p>
            <br>
            <p>Agora criaremos dois registradores Quânticos:</p>
            <p class="red">
                qr = QuantumRegister(2)
            </p>
            <p>Agora criaremos dois registradores Classicos:</p>
            <br>
            <p class="red">
                cr = ClassicalRegister(2)
            </p>
            <br>
            <p>Criando o circuiro:</p>
            <p class="red">
                circuit = QuantumCircuit(qr , cr)
            </p>
            <br>
            <p>Para visualizarmos usaremos esse comando instrução:</p>
            <p class="red">
                %matplotlib inline
            </p>
            <br>
            <p>Plotando nosso circuito, podemos notar que temos 2 Qubits e 2 registradosres Clássicos:</p>
            <p class="red">
                circuit.draw()
                <br>
                <br>
                <img src="img/plot.png" alt="Projeto 1">

                <p>O que faremos agora e a sobreposição dos Qubits, faremos isso com a implementação de uma porta lógica quântica chamada porta Hadamard, posicionada no Qubit[0]:</p>

                <p class="red">
                    circuit.h(qr[0])
                    <br>
                    <p>Para melhor intendimento seguiremos Plotando todos os passos, usaremos muito o comando:</p>
                    <p class="red">
                        circuit.draw()

                    </p>
                    <br>
                    <img src="img/had1.jpg" alt="Projeto 1">
                    <br>
                    <p>Agora usaremos outra porta lógica Quântica chamada Controlled-Not, É como um if. Sendo o primeiro qubit o controle e o segundo a operação:</p>
                    <p class="red">
                        circuit.cx(qr[0],qr[1])

                    </p>
                    <br>
                    <p>Plotando circuito, o Primeiro Qubit se posiciona com controlador, e o segundo como o atuador:</p>
                    <p class="red">
                        circuit.draw()
                    </p>
                    <img src="img/cnot.jpg" alt="Projeto 1">
                    <br>
                    <p>Por estarmos em um espaço mátematico, podemos mensurar os valroes de nosso circuitoe assim o faremos</p>
                    <p>Medida do Qbit, armazenando o bit clássico(criando as medidas):</p>
                    <p>Em seguida simularemos usando a componente Aer (importar):</p>
                    <p>Executaremos com:</p>
                    <p class="red">
                        circuit.cx(qr[0],qr[1])
                    </p>
                    <br>
                    <p>Em seguida simularemos usando a componente Aer (importar):</p>
                    <p></p>
                    <p class="red">
                        simulator = Aer.get_backend('qasm_simulator')

                    </p>
                    <br>
                    <br>
                    <br>
                    <p>Em seguida simularemos usando a componente Aer (importar):</p>
                    <p></p>
                    <p class="red">
                        simulator = Aer.get_backend('qasm_simulator')
                    </p>
                    <br>
                    <img src="img/simulator.png" alt="Projeto 1">
                    <br>
                    <p>Exectado com:</p>
                    <p class="red">
                        execute(circuit, backend = simulator) result = execute(circuit, backend = simulator).result()
                    </p>
                    <br>
                    <p>Para importar ferramentas de visaualização:</p>
                    <p class="red">

                        from qiskit.tools.visualization import plot_histogram </p>
                    <br>
                    <p>Plotando nosso histograma:</p>
                    <p class="red">
                        plot_histogram(result.get_counts(circuit)) ou com tituto plot_histogram(result.get_counts(circuit), tittle = 'titulo do histogram')
                    </p>
                    <img src="img/add title.png" alt="Projeto 1">
                    <br>
                    <p>Plote de nosso Histograma, podemos ver que nessa simulação houveram aproximadamente 50% de resultados resultantes em ambos os Qubits:</p>
                    <img src="img/plots.png" alt="Projeto 1">
                    <br>

                    <p>Para fins de comparação agora carregaremos nosso circuito para um hardware de veracidade Quântico:</p>
                    <br>
                    <p>Importante não saia de seu arquivo .ipynb</p>
                    <br>
        </div>
        <br>
        <br>
        <br>
        <h2>Carregando maquina veracidade Quântica -> QIBM</h2>
        <h4>(no mesmo arquivo do ipynb)</h4>
        <div class="project-secction">
            <h3>Iniciando um trabalho em maquina quântica</h3>
            <p>Carregando conta:</p>
            <br>
            <p class="red">
                IBMQ.load_account()
            </p>
            <br>
            <p>Escolhendo o computador:</p>
            <br>
            <p class="red">
                provider=IBMQ.get_provider('ibm-q') qcomp = provider.get_backend('ibm_oslo') </p>
            <br>
            <p>Iniciando nosso trabalho:</p>
            <br>
            <p class="red">
                job = execute(circuit, backend=qcomp)
            </p>
            <br>
            <img src="img/jobq.png" alt="Projeto 1">
            <br>
            <p>Importando o monitoramento e rodando o job:</p>
            <br>
            <p class="red">
                from qiskit.tools.monitor import job_monitor
            </p>
            <br>
            <p class="red">
                job_monitor(job) result = job.result()
            </p>
            <br>
            <p>Plotando:</p>
            <br>
            <p class="red">
                plot_histogram(result.get_counts(circuit))
            </p>
            <br>
            <img src="img/plotq.png" alt="Projeto 1">
            <p>Podemos ver que há sim uma diferença entre o expimento em simulação e expimento em maquina Quântica.</p>
            <br>
            <p>Portanto podemos concluir que a tecnologia esta em desenvolvimento e será necessarios algoritmos de correção.</p>
            <!-- Repita para outros projetos -->
    </section>
    <br>

    <footer>
        <p class="p_footer">&copy; IMPACTA 2023</p>
    </footer>
</body>


</html>
'''
