Guia de Conventional Commits
============================

Este guia descreve as convenções para mensagens de commit de código usando o padrão Conventional Commits. O objetivo é padronizar as mensagens de commit para facilitar a geração de changelogs, gerenciamento de versões e colaboração em projetos de código aberto.

O que são Conventional Commits?
-------------------------------

Conventional Commits é um padrão de nomenclatura de mensagens de commit que segue um formato específico. Ele ajuda a categorizar e descrever as mudanças feitas em um commit de maneira consistente.

Um commit convencional tem a seguinte estrutura:

```php-template
<tipo>[escopo opcional]: <descrição>
```

* **Tipo**: Indica a natureza do commit, como `feat` (nova funcionalidade), `fix` (correção de bug), `chore` (tarefas de manutenção), etc.
* **Escopo (opcional)**: Indica a área do código afetada pela mudança.
* **Descrição**: Uma breve descrição da mudança.

Exemplos:

* `feat: Adiciona um novo botão de login`
* `fix(auth): Corrige erro de autenticação`
* `chore(tests): Atualiza testes unitários`

Tipos de Commit
---------------

Aqui estão alguns tipos comuns de commits:

* `feat`: Para novas funcionalidades ou adições de recursos.
* `fix`: Para correção de erros ou bugs.
* `chore`: Para tarefas de manutenção ou limpeza de código.
* `docs`: Para atualizações na documentação.
* `style`: Para alterações de estilo, como formatação ou nomes de variáveis.
* `refactor`: Para refatorações de código, sem alterações funcionais.
* `test`: Para adição ou modificação de testes.
* `perf`: Para melhorias de desempenho.

Regras de Uso
-------------

1. **Mantenha Mensagens Curtas**: Tente manter as mensagens de commit curtas e concisas, mas suficientemente descritivas.
    
2. **Use o Presente**: Escreva as mensagens no tempo presente, como "Adiciona" em vez de "Adicionado".
    
3. **Seja Específico**: Seja o mais específico possível ao descrever a mudança.
    
4. **Use um Escopo Opcional**: Use um escopo opcional para indicar a área afetada pela mudança, quando apropriado.
    

Exemplos de Commit
------------------

Aqui estão alguns exemplos de mensagens de commit seguindo as Conventional Commits:

* `feat: Adiciona validação de entrada de usuário`
* `fix(auth): Corrige erro de validação de senha`
* `chore(tests): Atualiza biblioteca de teste`
* `docs: Atualiza documentação do API`
* `style(ui): Refatora CSS para seguir o padrão de estilo`
* `refactor: Simplifica a função de busca`
* `test(login): Adiciona teste de autenticação`
* `perf: Otimiza a consulta de banco de dados`

Considerações Finais
--------------------

O uso consistente das Conventional Commits facilita a rastreabilidade e a criação automática de changelogs. Certifique-se de seguir essas convenções ao fazer commits em projetos que adotam esse padrão.

Lembre-se de que a adoção de práticas de desenvolvimento sólidas, como testes unitários e revisões de código, é igualmente importante para manter a qualidade do código e a colaboração eficaz.

**Nota**: Este guia serve como um ponto de partida para a adoção das Conventional Commits em seus projetos. Você pode personalizá-lo conforme necessário para atender às necessidades específicas do seu projeto.