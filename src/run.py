from datetime import datetime

from models.redis.connection.redis_conn import RedisConnectionHandle
from models.redis.repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis_repo = RedisRepository(redis_conn)

# redis_repo.insert("Estou", "Aqui!!!")
# redis_repo.get('Estou')

# redis_repo.insert_hash('my_hash','Nome','Weverton')
# redis_repo.insert_hash('my_hash','Idade',18)
# valor = redis_repo.get_hash('my_hash','Nome')

data_atual = datetime.now()
data_form = data_atual.strftime('%Y-%m-%d')
print(data_form)


# Fruta em produção
redis_repo.insert_hash_ex(data_form, 'banana', 3.12, 20)
redis_repo.insert_hash(data_form, 'morango', 5.30)
redis_repo.insert_hash(data_form, 'melancia', 23.30)

# redis_repo.insert_hash(f'Clientes_{data_form}', 'Maicon', 18)
# redis_repo.insert_hash(f'Clientes_{data_form}', 'Lorena', 30)
# redis_repo.insert_hash(f'Clientes_{data_form}', 'Andre', 23)

