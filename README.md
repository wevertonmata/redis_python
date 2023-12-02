
# Redis Python


## Imagem docker:

```
docker run --name redis_lhama -d -p 6379:6379 -it redis:3.2.5-alpine

> docker  exec -it <imagem> /bin/sh #Rodar terminal da imagem
```

## Comando CLI

``` 
# Iniciar redis no terminal

redis-cli 
```

```
127.0.0.1:6379> ping
PONG

# Setar chave-valor
set chave_1 valor_1 

OK

# Verificar todas chaves
127.0.0.1:6379> keys *

1) "chave_1"

# Obter chave
127.0.0.1:6379> get chave_1

"valor_1"

# Hash
127.0.0.1:6379> hset meuhash campo_1 valor_1

(integer) 1
127.0.0.1:6379> hset meuhash campo_2 valor_2

(integer) 1
127.0.0.1:6379> hset meuhash campo_3 valor_3

# Multiplos campos do hash de uma só vez
127.0.0.1:6379> hmset meuHash2 campo1 valor1 campo2 valor2 campo3 valor3

OK
```

## TTL
Retorna o tempo restante de vida de uma chave que tem um tempo limite. 
Esse recurso de introspecção permite que um cliente Redis verifique por quantos segundos uma determinada chave continuará fazendo parte do conjunto de dados.

## Caso de uso
1. Primeiro busca a informação no Redis
2. Se encontrou retorna ao requisitante, se não busca no banco SQL ou NoSQL
3. Carrega as informações para o Redis e enviar a informação para requisitante

![Diagrama](docs\diagram.png)