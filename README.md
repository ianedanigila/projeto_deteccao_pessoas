# projeto_deteccao_pessoas

# Sistema Inteligente de Monitoramento e Detecção de Pessoas (IA)

## Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema de visão computacional avançado, baseado em Redes Neurais Convolucionais (CNN), para a detecção e segmentação automática de pessoas em ambientes reais, como a sala de estudos do campus da UFC de itapajé. O objetivo principal é criar uma ferramenta capaz de identificar a presença de indivíduos em diferentes cenários de forma precisa, com múltiplas pessoas ou condições de iluminação variadas.

O sistema utiliza o framework Detectron2, desenvolvido pelo Facebook AI Research, para realizar o fine-tuning de um modelo pré-treinado Mask R-CNN R-50 FPN. Esse modelo já possui capacidades avançadas de detecção e segmentação, e com o ajuste fino no dataset específico do campus, o sistema passa a identificar exclusivamente a classe person, ignorando todos os outros objetos presentes no ambiente. Desta forma, o projeto não exige o treinamento de uma CNN do zero, garantindo maior eficiência computacional e tempo reduzido de desenvolvimento.

Além da aplicação técnica, o projeto tem foco em Segurança da Informação e Segurança Física, permitindo monitoramento de ambientes, controle de acesso, análise de ocupação de espaços, e contribuindo para a proteção de pessoas, ativos físicos e informações sensíveis.

## Ambiente Utilizado
O desenvolvimento foi realizado em um ambiente de nuvem, garantindo escalabilidade e acesso a recursos de hardware (GPU).
Plataforma: Google Colab.
Linguagem: Python.
Framework de IA: Detectron2 (Facebook AI Research).
Bibliotecas principais: PyTorch, OpenCV, NumPy e Matplotlib.
Dataset: Imagens reais da sala de estudos do campus da UFC de itapajé, rotuladas no formato COCO (JSON).

## Passo a Passo para Execução
Inicialmente, certifique-se de que as imagens estejam armazenadas em data/images/ e que as anotações estejam localizadas em data/annotations/, seguindo o formato COCO (JSON).
O script training/train.py é responsável por configurar o modelo Mask R-CNN R-50 FPN, ajustando hiperparâmetros como número de iterações, batch size e taxa de aprendizado.
Para iniciar o treinamento do modelo, execute:
python training/train.py
Ao final do treinamento, o modelo ajustado é utilizado automaticamente pelo script de inferência para realizar testes em novas imagens.
Para executar a inferência, utilize:
python inference/test_model.py

## Exemplos de Resultados
O modelo foi capaz de realizar a segmentação de instâncias com sucesso, ignorando objetos irrelevantes no cenário e focando exclusivamente na detecção de pessoas.
<p align="center">
  <img src="Datas/Annotations/Captura-de-tela-2026-01-19-110015_png.rf.a5a4fe72d2a077785ce625d48b7fa0e4.jpg" width="600"/>
</p>

## Discussão sobre a Aplicação em Segurança da Informação
A aplicação deste sistema em Segurança da Informação e Segurança Física é direta e relevante. Com o monitoramento automatizado de ambientes sensíveis, é possível identificar presenças não autorizadas, evitando situações de risco. O sistema também pode ser integrado a mecanismos de controle de acesso inteligente, acionando alertas ou bloqueios automáticos quando uma pessoa não autorizada é detectada.

Além disso, a análise de ocupação de espaços permite gerenciar melhor salas de aula, laboratórios e corredores, prevenindo aglomerações e garantindo segurança para os usuários do campus. A proteção de ativos físicos e informações é reforçada, uma vez que o sistema complementa a vigilância tradicional e permite uma resposta rápida a incidentes.

Em suma, o projeto demonstra como técnicas avançadas de Inteligência Artificial podem ser aplicadas em cenários reais, fornecendo ferramentas práticas para monitoramento, proteção e análise de ambientes, contribuindo para a segurança de pessoas, informações e recursos.
