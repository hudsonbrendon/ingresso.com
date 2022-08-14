# Ingresso.com

Um wrapper em python para o ingresso.com

[![Python package](https://github.com/hudsonbrendon/ingresso.com/actions/workflows/python-package.yml/badge.svg)](https://github.com/hudsonbrendon/ingresso.com/actions/workflows/python-package.yml)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/ingresso.com.svg?style=flat)](https://github.com/hudsonbrendon/ingresso.com/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)


![Logo](https://www.exibidor.com.br/fotos/noticias/notundefined_1544192395.png)

# Recursos Disponíveis

- [x] Cinemas de uma cidade

- [x] Sessões de um cinema

- [x] Filmes em destaques

- [x] Filmes em cartaz

- [x] Filmes que serão lançados em brevve

# Instalação

```bash
$ pip install ingresso
```
ou

```bash
$ poetry build
```

# Modo de usar

Para utilizar a classe Ingresso, primeiro você precisa pegar o ID da cidade em questão, o ingresso.com disponibiliza um endpoint que lista as cidades e seus respectivos ids. Comece acessando o endpoint abaixo passando a UF do estado:

[https://api-content.ingresso.com/v0/states/UF](https://api-content.ingresso.com/v0/states/UF)

## Tabela de UFs:
| UF        | Estate  |
| --------- |:-----:|
| AC      | Acre |
| AL      | Alagoas |
| AP      | Amapá |
| AM      | Amazonas |
| BA      | Bahia |
| CE      | Ceará |
| DF      | Distrito Federal |
| ES      | Espírito Santo |
| GO      | Goiás |
| MT      | Mato Grosso |
| MA      | Maranhão |
| MS      | Mato Grosso do Sul |
| MG      | Minas Gerais |
| PA      | Pará |
| PB      | Paraíba |
| PR      | Paraná |
| PE      | Pernambuco |
| PI      | Piauí |
| RJ      | Rio de Janeiro |
| RN      | Rio Grande do Norte |
| RS      | Rio Grande do Sul |
| RO      | Rondônia |
| RR      | Roraima |
| SC      | Santa Catarina |
| SP      | São Paulo |
| SE      | Sergipe |
| TO      | Tocantins |

## Exemplo:

https://api-content.ingresso.com/v0/states/RN

Será retornado algo semelhante a isso:

```json
{
  "name": "Rio Grande do Norte",
  "uf": "RN",
  "cities": [
    {
      "id": "48",
      "name": "Natal",
      "uf": "RN",
      "state": "Rio Grande do Norte",
      "urlKey": "natal",
      "timeZone": "America/Fortaleza"
    }
  ]
}
```

No exemplo acima, o ID da cidade é o 48, é ele que deve ser usado no parâmetro **city_id**.

O parâmetro **partnership** é o nome do cinema, por exemplo: cinepolis, cinemark, knoplex, moviecom, etc.

## Cinemas

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.theaters()
```
ou 

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.theaters(1005)
```

## Cinemas por cidade

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.teathers_by_city()
```

## Sessões por cinema

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.sessions_by_theater(1005)
```

## Destaques por cinema

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.highlights()
```

## Filmes em cartaz

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.now_playing()
```

## Filmes em breve

```python
ingresso = Ingresso(48, 'cinepolis')

ingresso.soon()
```

# Contribua

Clone o projeto repositório:

```bash
$ git clone https://github.com/hudsonbrendon/ingresso.com.git
```

Certifique-se de que o [Poetry](https://python-poetry.org/) está instalado, caso contrário:

```bash
$ pip install -U poetry
```

Instale as dependências:

```bash
$ poetry install
```

```bash
$ poetry shell
```

Para executar os testes:

```bash
$ pytest
```

# Dependências

- [Python >=3.8](https://www.python.org/downloads/release/python-3813/)

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)
