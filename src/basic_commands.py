"""Comando redis básicos"""
import redis

redis_connection = redis.Redis(host='localhost', port=6379, db=0)
#print(redis_connection)

# Chave Valor
redis_connection.set('Chave_2','Hello World')

#redis_connection.delete('Chave_2')
#redis_connection.exists('Chave_2')

#valor = redis_connection.get('chave_1').decode('utf-8')
#print(f'{valor} do tipo {type(valor)}')


#Hash
redis_connection.hset('meu_hash','Nome','Weverton')
redis_connection.hset('meu_hash','Idade', 21)
redis_connection.hset('meu_hash','Cidade','Ribeirão das Neves')

#redis_connection.hdel('meu_hash','Cidade')
#redis_connection.exists('meu_hash')
#redis_connection.hexists('meu_hash','Cidade')

# nome = redis_connection.hget('meu_hash', 'Nome').decode('utf-8')
# print(f'{nome} do tipo {type(nome)}')



