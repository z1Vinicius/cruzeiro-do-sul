Projeto Integrador Transdisciplinar em Análise e Desenvolvimento de Software II - Cruzeiro Sul Virtual
RGM: 36575739


#### Lista de Propriedades (*)
**Níveis**: [A], [B], [C], [D], [E]
* **[A]** -  Muito Alta;
* **[B]** -  Alta;
* **[C]** -  Média;
* **[D]** -  Moderada;
* **[E]** -  Baixa;

## Situação Problema
A empresa Y precisa desenvolver um aplicativo para entrega de comida, mas enfrenta um obstáculo de falta de experiência em desenvolvimento ágil. A equipe de desenvolvimento atual da empresa não está familiarizada com os métodos ágeis e, portanto, não sabe por onde começar o projeto.

## História dos Usuários

#### História 1 
> Como Product Owner, quero que ao abrir o aplicativo, seja exibida uma animação suave com a logo da empresa para reforçar a identidade visual e proporcionar uma experiência inicial agradável aos usuários. 

* [A] Criar protótipos de animação em plataformas de prototipagem (Figma);
* [A] Detalhar estilos de animação (duração, efeitos e transição);
* [A] Revisar e aprovar design final da animação com Product Owner;
* [A] Implementar a logo de animação da logo do Aplicativo;
* [A] Realizar testes de usabilidade para que a logo funcione em diferentes dispositivos e formatos de tela (Requisitos Funcionais );
* [A] Realizar testes de performance para que ele esteja de acordo com os requisitos não funcionais.

`Tempo estimado: 7 dias.`

#### História 1 
> Como Product Owner, quero que ao abrir o aplicativo, seja exibida uma animação suave com a logo da empresa para reforçar a identidade visual e proporcionar uma experiência inicial agradável aos usuários. 

* [A] Criar protótipos de animação em plataformas de prototipagem (Figma);
* [A] Detalhar estilos de animação (duração, efeitos e transição);
* [A] Revisar e aprovar design final da animação com Product Owner;
* [A] Implementar a logo de animação da logo do Aplicativo;
* [A] Realizar testes de usabilidade para que a logo funcione em diferentes dispositivos e formatos de tela (Requisitos Funcionais );
* [A] Realizar testes de performance para que ele esteja de acordo com os requisitos não funcionais.

`Pontos de História: 13`
`Tempo estimado: 7 dias.`

#### História 2 
> Como futuro usuário, quero poder explorar o catálogo de produtos e serviços antes de me registrar, para avaliar a variedade de opções disponíveis e ter uma experiência inicial com o aplicativo sem compromisso. 

* [A] Criação de sistema de registro e login;
* [A] Definir limitações para usuário não registrados (modo visualização, sem histórico de compras) ;
* [A] Definir itens de estado de login para os componentes do aplicativo;
* [A] Criar rotas de navegação específicas para usuários registrados, não registrados e também baseados em cargos e permissões.

`Tempo estimado: 8 dias.`

#### História 3 
> Como Product Owner, preciso de uma guia personalizada dentro do aplicativo onde posso acessar rapidamente o total de entregas realizadas diariamente, para monitorar o desempenho operacional e tomar decisões estratégicas. 

* [E] Criação de WebSocket para atualização de dados em tempo real; 
* [E] Criação de endpoint na API para retornar os dados relevantes de monitoramento;
* [E] Criação de Dashboard intuitivo e responsivo para visualização de dados;
* [E] Testes de requisitos de eficiência para garantir que as informações sejam atualizadas em tempo real;

`Pontos de História: 1`
`Tempo estimado: 20 dias.`

#### História 4 
> Como usuário, quero que os estabelecimentos no aplicativo sejam automaticamente ordenados por status de funcionamento (aberto ou fechado) e que eu possa aplicar filtros como "frete grátis", para facilitar minha escolha e otimizar meu tempo de compra. 

* [D] Ajuste na API para adicionar dados de estado e valor de entrega do estabelecimento;
* [D] Adicionar Badge para indicar se o estabelecimento está aberto ou fechado;
* [D] Criar Badge para indicar se o estabelecimento está com frete grátis e valor do frete. 
* [D] Ajuste na interface para filtro inicial baseado no status de funcionamento/frete; 
* [D] Criação de controle para filtragem personalizada; 

`Tempo estimado: 6 dias.`

#### História 5 
> Como usuário, quero poder acessar uma lista dos meus últimos pedidos diretamente no aplicativo, para que eu possa repetir pedidos anteriores ou rastrear minhas atividades de compra com facilidade. 

* [B] Criação de lógica de armazenamento no banco para recuperação de dados; 
* [B] Criação de rota na API para o retorno de dados de pedidos do usuário;
* [B] Criação de prototipagem de interface de visualização de pedidos;
* [B] Criar rota onde é exibido os últimos pedidos por ordem decrescente e garantir o apenas para usuários registrados;
* [B] Testes unitários e automatizados de API e Interface.

`Pontos de História: 3`
`Tempo estimado: 12 dias.`

#### História 6 
> Como administrador do aplicativo, quero ter a capacidade de aplicar descontos especiais em estabelecimentos cadastrados, para atrair mais clientes e aumentar a competitividade do marketplace.

* [C] Desenvolver a lógica no back-end para aplicar descontos aos estabelecimentos cadastrado;
* [C] Configurar o banco de dados para armazenar informações dos descontos (tipo, valor, validade).;
* [C] Desenvolver APIs para criar, editar e remover descontos;
* [C] Criar wireframes para a interface de administração onde o administrador poderá aplicar e gerenciar os descontos;
* [C] Realizar testes unitários e de integração para garantir que os descontos são aplicados corretamente e que as regras de negócio estão sendo respeitadas.

`Tempo estimado: 12 dias.`

#### História 7 
> Como usuário, quero ter a opção de aplicar cupons de desconto durante o processo de checkout, para reduzir o custo das minhas entregas e incentivar o uso contínuo do aplicativo..

- [C] Desenvolver a lógica no back-end para validar e aplicar cupons de desconto;
- [C] Adicionar na finalização do pedido caixa de texto onde poderá ser inserido cupom de desconto;
- [C] Garantir que uma imagem informativa seja exibida especificando que o usuário recebeu ou não o desconto ("Cupom aplicado com sucesso" ou "Cupom inválido");
- [C] Realizar testes unitários e de integração para garantir que os cupons são validados e aplicados corretamente.
- [C] Testar diferentes cenários (e.g., cupons válidos, cupons expirados, cupons com restrições) para assegurar a robustez da funcionalidade.

`Tempo estimado: 10 dias.`

# Product Backlog
1. Criar protótipos de animação em plataformas de prototipagem (Figma)
2. Detalhar estilos de animação (duração, efeitos e transição)
3. Implementar a animação da logo no aplicativo
4. Realizar testes de usabilidade para que a animação funcione em diferentes dispositivos e formatos de tela
5. Realizar testes de performance para garantir que a animação esteja de acordo com os requisitos não funcionais
6. Criação de sistema de registro e login;
7. Definir limitações para usuário não registrados (modo visualização, sem histórico de compras) 
8. Definir itens de estado de login para os componentes do aplicativo;
9. Criar rotas de navegação específicas para usuários registrados, não registrados e também baseados em cargos e permissões;
10. Criação de lógica de armazenamento no banco para recuperação de dados; 
11. Criação de rota na API para o retorno de dados de pedidos do usuário;
12. Criação de prototipagem de interface de visualização de pedidos;
13. Criar rota onde é exibido os últimos pedidos por ordem decrescente e garantir o apenas para usuários registrados;
14. Testes unitários e automatizados de API e Interface.
15. Desenvolver a lógica no back-end para aplicar descontos aos estabelecimentos cadastrado;
16. Configurar o banco de dados para armazenar informações dos descontos (tipo, valor, validade).;
17. Desenvolver APIs para criar, editar e remover descontos;
18. Criar Wireframes para a interface de administração onde o administrador poderá aplicar e gerenciar os descontos;
19. Realizar testes unitários e de integração para garantir que os descontos são aplicados corretamente e que as regras de negócio estão sendo respeitadas.
20. Desenvolver a lógica no back-end para validar e aplicar cupons de desconto;
21. Adicionar na finalização do pedido caixa de texto onde poderá ser inserido cupom de desconto;
22. Garantir que uma imagem informativa seja exibida especificando que o usuário recebeu ou não o desconto ("Cupom aplicado com sucesso" ou "Cupom inválido");
23. Realizar testes unitários e de integração para garantir que os cupons são validados e aplicados corretamente.
24. Testar diferentes cenários (e.g., cupons válidos, cupons expirados, cupons com restrições) para assegurar a robustez da funcionalidade.
25. Ajuste na API para adicionar dados de estado e valor de entrega do estabelecimento;
26. Adicionar Badge para indicar se o estabelecimento está aberto ou fechado;
27. Criar Badge para indicar se o estabelecimento está com frete grátis e valor do frete. 
28. Ajuste na interface para filtro inicial baseado no status de funcionamento/frete; 
29. Criação de controle para filtragem personalizada; 
30. Criação de WebSocket para atualização de dados em tempo real; 
31. Criação de endpoint na API para retornar os dados relevantes de monitoramento;
32. Criação de Dashboard intuitivo e responsivo para visualização de dados;
33. Testes de requisitos de eficiência para garantir que as informações sejam atualizadas em tempo real;

# Sprints
## Sprint 1
Objetivo Principal: Desenvolver e integrar animações no aplicativo, criar um sistema de registro e login robusto, implementar lógica de navegação baseada em permissões e otimizar a interface de visualização de pedidos, garantindo alta performance e usabilidade.

`Duração: 27 dias`

#### SPRINT BACKLOG
1. Criar protótipos de animação em plataformas de prototipagem (Figma)
2. Detalhar estilos de animação (duração, efeitos e transição)
3. Implementar a animação da logo no aplicativo
4. Realizar testes de usabilidade para que a animação funcione em diferentes dispositivos e formatos de tela
5. Realizar testes de performance para garantir que a animação esteja de acordo com os requisitos não funcionais
6. Criação de sistema de registro e login;
7. Definir limitações para usuário não registrados (modo visualização, sem histórico de compras) 
8. Definir itens de estado de login para os componentes do aplicativo;
9. Criar rotas de navegação específicas para usuários registrados, não registrados e também baseados em cargos e permissões;
10. Criação de lógica de armazenamento no banco para recuperação de dados; 
11. Criação de rota na API para o retorno de dados de pedidos do usuário;
12. Criação de prototipagem de interface de visualização de pedidos;
13. Criar rota onde é exibido os últimos pedidos por ordem decrescente e garantir o apenas para usuários registrados;
14. Testes unitários e automatizados de API e Interface.

## Sprint 2
Objetivo Principal: Implementar funcionalidades de descontos e cupons, ajustar a interface para visualização de status de estabelecimentos e desenvolver a lógica para atualização de dados em tempo real, garantindo uma experiência de usuário fluida e intuitiva.

`Duração: 28 dias`

#### SPRINT BACKLOG
1. Desenvolver a lógica no back-end para aplicar descontos aos estabelecimentos cadastrado;
2. Configurar o banco de dados para armazenar informações dos descontos (tipo, valor, validade).;
3. Desenvolver APIs para criar, editar e remover descontos;
4. Criar Wireframes para a interface de administração onde o administrador poderá aplicar e gerenciar os descontos;
5. Realizar testes unitários e de integração para garantir que os descontos são aplicados corretamente e que as regras de negócio estão sendo respeitadas.
6. Desenvolver a lógica no back-end para validar e aplicar cupons de desconto;
7. Adicionar na finalização do pedido caixa de texto onde poderá ser inserido cupom de desconto;
8. Garantir que uma imagem informativa seja exibida especificando que o usuário recebeu ou não o desconto ("Cupom aplicado com sucesso" ou "Cupom inválido");
9. Realizar testes unitários e de integração para garantir que os cupons são validados e aplicados corretamente.
10. Testar diferentes cenários (e.g., cupons válidos, cupons expirados, cupons com restrições) para assegurar a robustez da funcionalidade.
11. Ajuste na API para adicionar dados de estado e valor de entrega do estabelecimento;
12. Adicionar Badge para indicar se o estabelecimento está aberto ou fechado;
13. Criar Badge para indicar se o estabelecimento está com frete grátis e valor do frete. 
14. Ajuste na interface para filtro inicial baseado no status de funcionamento/frete; 
15. Criação de controle para filtragem personalizada; 


